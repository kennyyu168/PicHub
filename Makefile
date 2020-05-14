#set noexpandtab

.PHONY: run install clean

all: run

run:
	./run.sh

install:
	pip install -r requirements.txt

clean:
	@echo "Cleaning up..."
	-rm -f *.pyc
	-rm -rf imgur/
	-rm -rf __pycache__/
	-rm -rf ./frontend/static/h_images/fulls/*.jpg
	-rm -rf ./frontend/static/h_images/thumbs/*.jpg
	mkdir -p imgur/
