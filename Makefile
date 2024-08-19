default: run

run:
	python3 src/server.py --certificate braucq.certs.inl.ovh/fullchain.pem --port=4433 --private-key braucq.certs.inl.ovh/privkey.pem

tcp:
	python3 src/tcp_server.py

clean:
	rm default_logfile/*
	
clear:
	find . -name *.pyc -exec rm {} \;

mod:
	python3 src/server_modified.py --certificate braucq.certs.inl.ovh/fullchain.pem --port=4433 --private-key braucq.certs.inl.ovh/privkey.pem
	
compile_cmodule:
	sudo python3 setup.py install
	
curl:
	curl --http3-only https://braucq.certs.inl.ovh:4433/
