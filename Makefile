
install:
	@python3 -m pip install --upgrade pip
	@pip3 install -r requirements.txt
	
run:
	@python3 app/finans_app.py
	
