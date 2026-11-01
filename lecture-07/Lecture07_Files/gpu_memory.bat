@echo off
title GPU memory
rem Lecture 7: prints the used memory of the first NVIDIA GPU five times per second.
rem Change -i 0 to -i 1 to watch a second GPU. Close this window to stop.
nvidia-smi -i 0 --query-gpu=memory.used,memory.total --format=csv -lms 200
