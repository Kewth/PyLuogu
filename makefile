~/.local/bin/PyLuogu: dist/PyLuogu.py source/
	pip3 install ./ --user
	cp dist/PyLuogu.py ~/.local/bin/PyLuogu
	chmod +x ~/.local/bin/PyLuogu
