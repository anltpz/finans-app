

install:
	@python3 -m pip install --upgrade pip
	@pip install -r requirements.txt
	
run:
	@python3 finans-app.py
	

test:
	@echo "test"


