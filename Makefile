build:
	@echo "Will install dependencies and build app"
test:
	@echo "Starting HTTP Server"
	python src/main.py & echo $$! > $@
	@echo "Running Tests"
	-pytest tests/
	kill `cat $@` && rm $@
run:
	@echo "Starting HTTP Server"
	python src/main.py

.PHONY: test run