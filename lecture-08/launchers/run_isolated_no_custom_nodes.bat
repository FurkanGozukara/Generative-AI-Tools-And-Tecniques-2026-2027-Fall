@title ComfyUI isolated test
@cd /d "%~dp0"
venv\Scripts\python.exe main.py --port 8190 --disable-all-custom-nodes
@pause
