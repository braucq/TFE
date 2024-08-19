# Aioquic server for client performance evaluation
###### Benoit Raucq

This project's goal is to provide an easy to use aioquic server to perform client analysis such as latency or lost packets recovery policies.

### V0.1 - MacOS only
This is a working version which uses aioquic quic server example [Github page](https://github.com/aiortc/aioquic/tree/main/examples) with a basic TCP server advertising HTTP/3 compatibility on a second port.
In order to access the quic server :
+ Check ssl key and certificate
+ Modify Users/etc/host file in order to enable the clients to find the host (e.g.localhost)
```bash
sudo nano etc/host
```
Add at the end '127:0:0:1	aio.test'; type '^X' then 'y' then 'Enter'.
+ Launch both tcp and quic servers (from root on different terminals)
```bash
make
```

```bash
make tcp
```
You can use 'make' and 'make tcp' commands as shortcut (obselete)
+ Open your favorite browser supporting quic. Those have been tested :
	[x] Firefox
	[x] Google Chrome - Does connect to TCP server but fail to redirect to Quic port :4433
	[ ] Safari - Does connect to TCP server but fail to redirect to Quic port :4433
+ Type 'aio.test:4430' on the navigation bar. This normally shows a (relatively ugly) welcome message. If you reload the page, it should correctly connect to the HTTP/3 server with the aioquic example interface.

_Note that this is more a reminder for future work then a real tutorial._
What is happening is that browser usually try HTTP/2 and HTTP/1.1 connection when they try to connect for the first time to an unkown server. The latest need to be HTTP/1.1 or HTTP/2 compatible in order to advertise its HTTP/3 compatibility with **[Alt-Svc](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Alt-Svc) HTTP header**. A way around that is to have a DNS ad which requires steps I did not even look at as I was working locally with low/none internet connection.
For TSL compatibility a self-certified key was generated. It is not recognized by authority so browser may inform you of a security threat. If you did add a malware directly to your .py files, you SHOULD NOT continue with the procedure (this might not happen, why would you attack yourself?). If you want to genereate new key, simply use this command and follow the steps :
```bash
make new_ssl_key
```

### Make commands
- default : run
- run : launch aioquic server with args -c tests/ssl_cert.pem -k tests/ssl_key.pem
- tcp : launch tcp server (with no args needed)
- new_ssl_key : generate new self-signed ssl certificate and key
Manually launch aioquic server :
```bash
python src/server.py --host address[::1] --port port[4433] --certificate path/to/certificate.pem --private-key path/to/key.pem --secret-log /logfile
```
Other args are displayed in source file.
