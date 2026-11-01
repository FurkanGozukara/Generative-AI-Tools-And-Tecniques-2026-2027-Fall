@echo off
title ComfyUI
cd /d "%~dp0"
venv\Scripts\python.exe main.py --enable-manager --port 8189 --reserve-vram 3
pause
