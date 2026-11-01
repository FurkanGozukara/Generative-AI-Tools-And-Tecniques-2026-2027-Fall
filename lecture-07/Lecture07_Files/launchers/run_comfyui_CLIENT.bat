@echo off
title ComfyUI CLIENT (no metadata)
cd /d "%~dp0"
venv\Scripts\python.exe main.py --enable-manager --port 8189 --reserve-vram 3 --disable-metadata
pause
