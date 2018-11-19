compile:
	pipenv run pyinstaller --distpath bin --onefile sublime_text.py
	pipenv run pyinstaller --distpath bin --onefile sublime_pipenv.py
	pipenv run pyinstaller --distpath bin --onefile open.py

install:
	cp bin/sublime_text /usr/local/bin/sublime_text && chown michaelhollister:michaelhollister /usr/local/bin/sublime_text && chmod +x /usr/local/bin/sublime_text
	cp bin/sublime_pipenv /usr/local/bin/sublime_pipenv && chown michaelhollister:michaelhollister /usr/local/bin/sublime_pipenv && chmod +x /usr/local/bin/sublime_pipenv
	cp bin/open /usr/local/bin/open && chown michaelhollister:michaelhollister /usr/local/bin/open && chmod +x /usr/local/bin/open

clean:
	rm bin/sublime_text
	rm bin/sublime_pipenv
	rm bin/open