local: ~/.local/bin/PyLuogu dirs
	sleep 0

~/.local/bin/PyLuogu: dist/main.py source/ setup.py
	pip3 install ./ --user
	cp dist/main.py ~/.local/bin/PyLuogu
	chmod +x ~/.local/bin/PyLuogu

dirs: ~/.local/share/PyLuogu/lock
	sleep 0

~/.local/share/PyLuogu/lock: 
	mkdir -p ~/.local/share/PyLuogu
	touch ~/.local/share/PyLuogu/lock
