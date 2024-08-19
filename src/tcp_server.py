""" 
# BENOIT RAUCQ 
# TCP-SERVER MAIN
# DECEMBER 2022
"""

import socket
import sys
import ssl


MAX_CONNECTIONS = 10
HOST_NAME = 'aio.test'

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('braucq.certs.inl.ovh/fullchain.pem', 'braucq.certs.inl.ovh/privkey.pem')

def content():
    # content shown in the site - here is some simple html stuff
    rval  = b"<html><body>"
    rval += b"<h1>Aioquic server test</h1>"
    rval += b"<h2>This is HTTP/1.1 server</h2>"
    rval += b"<p>For the 1st connection browsers usually try HTTP/1.1 and HTT/2 requests. "
    rval += b"HTTP/3 is only enabled when the client knows it is. "
    rval += b"Please reload the page to access the actual web page. </p>"
    #rval += b"<img source="">"
    rval += b"</body></html>"
    return rval

def main() -> None:
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server_addr = ('127.0.0.1', 4430)
        sock.bind(server_addr)
        sock.listen(MAX_CONNECTIONS)
        
        with context.wrap_socket(sock, server_side=True) as ssock:
            while True:
                try:
                    connection, client_addr = ssock.accept()
                    try:
                        data = ''
                        length = 0
                        while True:
                            data += str(connection.recv(1024))
                            if length != len(data): 
                                length = len(data)
                                break
                            else :
                                break
                        print("received : {}...\n".format(data[:20]))
                    finally: 
                        http_header =  b"HTTP/1.1 200 OK\r\nAlt-Svc: h3=\":4433\"; ma=6000,h3-29=\":4433\"; ma=6000,h3-Q050=\":4433\"; ma=6000,h3-Q046=\":4433\"; ma=6000,h3-Q043=\":4433\"; ma=6000,quic=\":4433\"; ma=6000\r\n"
                        http_header += b"content-type: text/html; charset=UTF-8\r\n"
                        http_header += b"\r\n" # end of header
                        connection.send(http_header)
                        print("Header sent...")
                        connection.send(content())
                        print("Content sent")
                        connection.close()

                except (InterruptedError,TimeoutError,ValueError,OSError):
                    print('Error with ssl protocol')
                    pass
            ssock.close()
        sock.close()
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

