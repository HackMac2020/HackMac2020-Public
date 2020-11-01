IMAGE_NAME = ok-boomer

build:
	docker build -t $(IMAGE_NAME) .
run:
	docker stop -t 0 $(IMAGE_NAME); $(MAKE) build; docker run --privileged --rm -d -p 1337:1337 \
	--name $(IMAGE_NAME) $(IMAGE_NAME) 
exec:
	docker exec -it ok-boomer bash
stop:
	docker stop -t -0 $(IMAGE_NAME)