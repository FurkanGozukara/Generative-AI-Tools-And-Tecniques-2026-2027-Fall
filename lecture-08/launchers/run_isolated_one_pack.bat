@title ComfyUI isolated test, one pack
@cd /d "%~dp0"
venv\Scripts\python.exe main.py --port 8190 --disable-all-custom-nodes --whitelist-custom-nodes comfyui-inpaint-cropandstitch
@pause
