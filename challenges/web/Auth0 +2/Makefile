build:
	docker build -t jwt1 .
run:
	docker stop -t 0 jwt1; $(MAKE) build; docker run --rm -d --name jwt1 -p 1337:1337 -e PORT=1337 jwt1
stop:
	docker stop jwt1
test:
	cd src && node test.js
