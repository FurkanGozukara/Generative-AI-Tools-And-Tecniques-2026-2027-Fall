# Commands used in Lecture 7

Type or paste each command on its own and wait for the prompt to return before the next one. The times in brackets are lecture timestamps. The outputs quoted below are the ones the lecture recorded on October 26, 2026; versions, file numbers and sizes on your computer can differ.

## Update ComfyUI (chapter 2, 1:07)

Open your ComfyUI installation folder in File Explorer, type `cmd` in its address bar and press Enter. The Command Prompt opens in that folder.

```bat
venv\Scripts\activate
```

```bat
git pull --ff-only
```

```bat
python -m pip install -r requirements.txt
```

After activation the prompt starts with `(venv)`, so the packages go into this installation. If Git reports a conflict, solve that conflict first and run the update again. Keep the window open until the prompt returns without red error lines. The recorded update moved ComfyUI from commit `c06bf5f5` to `fe298e4e`; the restarted server reported ComfyUI 0.42.0 with frontend package 1.57.1.

## The course launch files (chapter 2, 2:07)

Copy both files from `Lecture07_Files\launchers` into your ComfyUI folder, then double-click `run_comfyui.bat` (2:32). It runs:

```bat
venv\Scripts\python.exe main.py --enable-manager --port 8189 --reserve-vram 3
```

`run_comfyui_CLIENT.bat` runs the same line with one extra flag, `--disable-metadata` (chapter 15, 34:01):

```bat
venv\Scripts\python.exe main.py --enable-manager --port 8189 --reserve-vram 3 --disable-metadata
```

Open `http://127.0.0.1:8189` in the browser. `--reserve-vram 3` keeps 3 GB of GPU memory free for other programs. Close the console window to stop the server; only one of the two files can use port 8189 at a time.

## GPU memory window (chapter 9, 16:38)

Double-click `Lecture07_Files\gpu_memory.bat`. It runs:

```bat
nvidia-smi -i 0 --query-gpu=memory.used,memory.total --format=csv -lms 200
```

It prints the used and total memory of the first NVIDIA GPU five times a second, for every program on that GPU. Change `-i 0` to `-i 1` to watch a second GPU, and close the window to stop it. Recorded on an RTX 5090 (32,607 MiB in total): 1,509 MiB in use at rest, a peak of 12,261 MiB while VAE Decode decoded the latent of the 2048 × 2048 watchmaker, and a peak of 3,338 MiB with VAE Decode (Tiled) at tile size 512 and overlap 64.

## Check ImageMagick (chapter 10, 18:19)

Open a Command Prompt and type:

```bat
magick -version
```

Recorded first line: `Version: ImageMagick 7.1.1-44 Q16-HDRI x64 76f853c:20250222 https://imagemagick.org`. Yours may be newer. If Windows reports that `magick` is not recognized, download the Windows installer from [imagemagick.org/download](https://imagemagick.org/download/#windows) and tick **Add application directory to your system path** on the additional tasks page (18:35), then open a new Command Prompt.

## Install ExifTool and add it to PATH (chapter 10, 18:50)

1. On [exiftool.org](https://exiftool.org/), download the 64-bit **Windows Executable** zip. The recorded file was `exiftool-13.59_64.zip` (11,183,675 bytes, SHA-256 `44b512b25af500724ba579d0a53c8fc5851628b692dd5e5d94ae4a15c2cba9ec`). It needs no installer.
2. Create a folder named `tools` next to your course folders and move the zip into it (19:12).
3. Right-click the zip, choose **Extract All** and open the extracted folder (19:32). Select the readme and press **Alt+P** to show its text in the preview pane: it names the file to use from the command line (19:42).
4. Rename `exiftool(-k).exe` to `exiftool.exe` and keep the `exiftool_files` folder beside it (19:54). The `(-k)` version waits for a key press, which blocks automated use.
5. Copy the address of the folder that now holds `exiftool.exe`. Search the Start menu for **environment variables** and open the variables of your own account (20:06). Select **Path**, choose **Edit**, then **New**, paste the address and confirm every window with **OK** (20:23).
6. Open a **new** Command Prompt, for example by typing `cmd` in the address bar of `Lecture07_Files` (20:36). Only windows opened after the change read the new Path.

```bat
magick -version
```

```bat
exiftool -ver
```

Recorded answers (20:45): the ImageMagick version line above and `13.59`. If one is not recognized, check the Path entry for a typo and open another window.

## Colorization commands (chapter 13)

Open a Command Prompt in `Lecture07_Files\images` (type `cmd` in its address bar). Copy each command from `Lecture07_Files\Lecture07_prompts.txt`, the course notes, and paste it. The part `..\..\ComfyUI_Week01\output\Lecture07\` reaches ComfyUI's output folder when `Lecture07_Files` and `ComfyUI_Week01` sit in the same parent folder; change it if your folders have other names.

Black and white version of the NASA photograph (26:56):

```bat
magick mercury7_nasa_s61-01250_color.jpg -colorspace Gray mercury7_bw.png
```

Upload `mercury7_bw.png` into the Lecture 4 edit workflow and paste the colorization instruction from the course notes (27:25); the run saves `ComfyUI\output\Lecture07\colorized_00001_.png`.

The colours of the colorized image on the original brightness, Luminize compose (29:11):

```bat
magick ..\..\ComfyUI_Week01\output\Lecture07\colorized_00001_.png -alpha off -resize 3000x2398! mercury7_bw.png -compose Luminize -composite mercury7_recombined.png
```

Brightness difference from the black and white original, first for the recombined file, then for the regenerated image (29:11 and 29:27):

```bat
magick ( mercury7_recombined.png -colorspace Gray ) mercury7_bw.png -metric RMSE -compare -format "%[distortion]\n" info:
```

```bat
magick ( ..\..\ComfyUI_Week01\output\Lecture07\colorized_00001_.png -alpha off -resize 3000x2398! -colorspace Gray ) mercury7_bw.png -metric RMSE -compare -format "%[distortion]\n" info:
```

Each prints one normalized root mean square error, where 0 means identical brightness. Recorded: `0.00993996` for the recombined file and `0.0925738` for the regenerated image. Your colorization will differ from ours, and so will your two numbers; to reproduce these values, point the commands at the recorded `recorded_results\13_colorize\colorized_00001_.png` instead of your own file.

## Check the print master (chapter 14, 31:23)

The destination written in the course notes: `4096 x 4096 px, sRGB, 16-bit PNG, no alpha, no workflow in the file`.

```bat
exiftool -f -ImageSize -BitDepth -ColorType -ProfileDescription ..\..\ComfyUI_Week01\output\Lecture07\print_master_*.png
```

`-f` prints a tag the file lacks as `-`. Recorded for the first export: `Image Size: 4096x4096`, `Bit Depth: 16`, `Color Type: RGB with Alpha`, `Profile Description: -`. After Split Image with Alpha was placed before the colour space converter and the export ran again, the same command (32:13) read `print_master_00002.png` as `Color Type: RGB`. `Profile Description: -` means no colour profile is embedded; ComfyUI writes none, so attach one afterwards when a print client asks for it.

## What the file tells a stranger (chapter 15)

```bat
exiftool -a -G1 ..\..\ComfyUI_Week01\output\Lecture07\watchmaker_00001_.png
```

Recorded (33:31): after the file and image rows, `[PNG] Prompt` holds the complete prompt as JSON, starting with the `UNETLoader` and `z_image_turbo_bf16.safetensors`, and `[PNG] Workflow` holds the whole graph with every model file name.

Close the server's console window, double-click `run_comfyui_CLIENT.bat` (34:14) and run the export again; it saved `print_master_00004.png` in the lecture (use your newest number). Then:

```bat
exiftool -a -G1 ..\..\ComfyUI_Week01\output\Lecture07\print_master_00004.png
```

Recorded (34:40): only technical rows (the ExifTool version, file system, PNG, pHYs and composite rows: 4096 × 4096, 16-bit, RGB); no Prompt and no Workflow row.

## Enlarge the chart with Lanczos (chapter 16, 36:04)

In the same Command Prompt in `Lecture07_Files\images`:

```bat
magick chart_orders_640.png -filter Lanczos -resize 400% chart_lanczos_400.png
```

It writes a 2560 × 1600 copy and prints nothing. The copy is softer, but its Online Q4 label still reads 5,862; in `recorded_results\16_chart_real_esrgan\chart_gan_00001_.png` Real-ESRGAN turned the same label into 5,002.

## Check the delivery (chapter 17, 37:52)

```bat
exiftool -f -ImageSize -BitDepth -ColorType -Prompt -Workflow ..\..\ComfyUI_Week01\output\Lecture07\delivery_00001.png
```

Recorded, with the server started by the client launch file: `Image Size: 2688x1536`, `Bit Depth: 8`, `Color Type: RGB`, `Prompt: -`, `Workflow: -`.
