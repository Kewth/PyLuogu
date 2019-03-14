~/.local/bin/PyLuogu: PyLuogu.py source/
	pip3 install ./ --user
	cp PyLuogu.py ~/.local/bin/PyLuogu
	chmod +x ~/.local/bin/PyLuogu
