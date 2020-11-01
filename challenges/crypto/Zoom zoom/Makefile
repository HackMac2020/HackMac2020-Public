IMAGE_NAME = zoom_zoom

build:
	docker build -t $(IMAGE_NAME) .
run:
	docker stop -t 0 $(IMAGE_NAME); $(MAKE) build; docker run --rm -d -p 1337:1337 \
	--name $(IMAGE_NAME) $(IMAGE_NAME) 
stop:
	docker stop $(IMAGE_NAME)
