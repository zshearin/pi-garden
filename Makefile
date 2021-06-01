.PHONY: test
test:
	python3 test_script.py

.PHONY: run_server
run_server:
	python3 server.py

.PHONY: install
install:
	pip3 install adafruit-blinka
	sudo pip3 install adafruit-circuitpython-seesaw
