Tools for Windows Subsystem Linux (WSL)<br/>
Deprecated: Use https://github.com/mike-seagull/wsl_tools
<h4>sublime_text</h4>
<h5>To open sublime text to the directory or file</h5>
<code>python sublime_text.py $FILE_OR_DIRECTORY</code>
<h5>To compile it into a binary</h5>
<code>pyinstaller --distpath bin --onefile src/sublime_text.py</code>
<h4>open</h4>
<p>opens file explorer to the directory or file</p>
<code>python open.py $FILE_OR_DIRECTORY</code>
<h5>To compile it into a binary</h5>
<code>pyinstaller --distpath bin --onefile src/open.py</code>
