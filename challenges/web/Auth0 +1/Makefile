build:
	docker build -t jwt0 .
run:
	docker stop -t 0 jwt0; $(MAKE) build; docker run --rm -d --name jwt0 -p 1337:1337 -e PORT=1337 jwt0
stop:
	docker stop jwt0
test:
	cd src && node test.js
