~/.local/bin/PyLuogu: dist/main.py source/ setup.py
	pip3 install ./ --user
	cp dist/main.py ~/.local/bin/PyLuogu
	chmod +x ~/.local/bin/PyLuogu
