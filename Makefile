#set noexpandtab

.PHONY: run clean

all: run

run:
	./run.sh

clean:
	@echo "Cleaning up..."
	-rm -f *.txt
	-rm -f *.pyc
	-rm -f *.json
	-rm -rf imgur/
	-rm -rf __pycache__/
	mkdir -p imgur/
