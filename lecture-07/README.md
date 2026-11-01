# Lecture 7 — Upscaling, Restoration & Professional Delivery

[Download the complete companion ZIP](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/releases/download/lecture-07/Lecture_07_Companion_Files.zip) (about 118 MB) · [Lecture 7 release](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/releases/tag/lecture-07) · [Full course playlist](https://www.youtube.com/playlist?list=PLUMEJUep1hiI)

Extract the ZIP and open `lecture-07/README.md`. It includes the course notes, launchers, 19 recorded workflow recipes in editable and API forms, all required inputs and the original results. The guides, command sheets and workflows are also available here on GitHub; image inputs, saved latents and full-resolution results are supplied in the ZIP. Model files are separate downloads.

The video description and chapter list are included below as files; use the course playlist for the video. Continue from the [Lecture 6 materials](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/tree/main/lecture-06).

Companion files for **Generative AI Full Course - Lecture 7: Upscaling, Restoration & Professional Delivery**.

Turn a good generation into a file you can deliver. The lecture takes one 1024 px image to 4K with a Lanczos resize, Real-ESRGAN, tiled diffusion and SeedVR2 and compares them, measures tiled VAE decoding, installs ImageMagick and ExifTool, repairs a small face with FaceDetailer and another with Qwen-Image 2.1 plus Transfer Color, colorizes a 1961 NASA photograph and checks what changed, exports a 16-bit print master to a written specification, reads the metadata a PNG carries and ends with a complete delivery chain.

Recorded on October 26, 2026 on Windows with ComfyUI 0.42.0 (frontend 1.57.1), an NVIDIA RTX 5090, ImageMagick 7.1.1-44 and ExifTool 13.59. Newer versions can change menus and results. The times below are lecture timestamps.

## Set up

1. Start from your ComfyUI installation of Lecture 1 (the lecture's folder is `ComfyUI_Week01`) and update it with the commands in [commands.md](commands.md).
2. Copy the `Lecture07_Files` folder of this ZIP into the folder that holds `ComfyUI_Week01` (for example `C:\AI`; the lecture uses `G:\educational_videos`), so the two folders sit side by side. The commands in the course notes run in `Lecture07_Files\images` and reach the ComfyUI outputs through `..\..\ComfyUI_Week01\output\Lecture07\`. If your ComfyUI folder has another name, change that part of each command.
3. Copy `run_comfyui.bat` and `run_comfyui_CLIENT.bat` from `Lecture07_Files\launchers` into your ComfyUI folder and start ComfyUI with `run_comfyui.bat`.
4. Download the model files in [MODELS.md](MODELS.md) into the listed folders, or download Real-ESRGAN and SeedVR2 when the lecture does (chapters 5 and 7). FaceDetailer's packs are installed in chapter 11.
5. Copy `explorer_anchor.png` and `chart_orders_640.png` from `Lecture07_Files\images` into `ComfyUI\input`, or choose them with the upload button of the Load Image node.
6. Open workflows with ComfyUI's **Open** command (Ctrl+O) from `Lecture07_Files\workflows`. Copy prompts, instructions and commands from `Lecture07_Files\Lecture07_prompts.txt`, the course notes the lecture copies from.

## Chapter guide

In the table, `workflows/`, `images/` and `launchers/` are folders of `Lecture07_Files`; recorded graph names refer to `recorded_workflows/` and `recorded_results/`.

| Starts at | Chapter | Files | What to do |
|---|---|---|---|
| 0:00 | Sharp but wrong: what this lecture fixes | `recorded_results/16_chart_real_esrgan/`, the four route results | The chart label 5,862 that Real-ESRGAN turned into 5,002, and four different dials from one image. |
| 1:07 | Update ComfyUI and start it with the course launcher | [commands.md](commands.md), `Lecture07_Files/launchers/` | Activate the environment, pull, install the requirements, copy both launch files into the ComfyUI folder, start the normal one and refresh the browser page once. |
| 2:52 | Generate a 1024 pixel test image with Z-Image Turbo | `workflows/lecture02_workflow.json`, the watchmaker prompt in the course notes | Replace the prompt, keep 1024 × 1024, set the seed to 2026 and run. Recorded: `03_watchmaker_1024`. |
| 3:55 | Lanczos resize: the honest 4K baseline | built on camera; recorded `04_lanczos_4096` | Add Upscale Image (method lanczos, 4096 × 4096) after the decode and a Save Image with prefix `Lecture07/lanczos`. |
| 5:16 | GAN upscaler: download and run Real-ESRGAN 4x | [MODELS.md](MODELS.md); recorded `05_gan_4096` | Move the model into `models/upscale_models`, press R, add Load Upscale Model and Upscale Image (using Model) and a Save Image with prefix `Lecture07/gan`. The 4× factor is part of the model file. |
| 7:28 | Tiled diffusion with core tile list nodes | recorded `06_tiles_4096` | Split Image into List of Tiles (1024, overlap 128), VAE Encode, a copy of the KSampler pasted with Ctrl+Shift+V at denoise 0.3, VAE Decode, Merge List of Tiles to Image (4096 × 4096, overlap 128) and a Save Image with prefix `Lecture07/tiles`. The 25 tiles run one after another. |
| 10:46 | SeedVR2 one-step restoration from the official template | `workflows/SeedVR2_3B_image_upscale_template.json`; recorded `07_seedvr2_4096` | Download the two missing models the issues panel names, move them into `models/diffusion_models` and `models/vae`, press R, bring the watchmaker in with Copy (Clipspace) and Paste (Clipspace), keep the multiplier at 4 and run. |
| 13:58 | Compare four routes: preserve or invent? | `recorded_results/04_lanczos_4096/` to `07_seedvr2_4096/` | Open the four 4096 × 4096 results at the same zoom on the dial and on the face, and decide which one a product photo and which one a poster should get. |
| 15:16 | Tiled VAE decode: same latent, lower memory | `workflows/tiled_vae_1_save_latent.json`, `workflows/tiled_vae_2_decode.json`, `gpu_memory.bat`; recorded `09_latent_2048`, `09_decode_full`, `09_decode_tiled` | Save the 2048 px latent, move it from `output\latents` into `input`, press R and open the second workflow. Unload the models, start `gpu_memory.bat`, run the ordinary branch, then bypass it and run the tiled one (tile size 512, overlap 64). |
| 18:07 | Check ImageMagick, install exiftool, add it to PATH | [commands.md](commands.md) | `magick -version`, the ExifTool zip in a `tools` folder, the rename, the Path entry and a new Command Prompt for both version checks. |
| 21:05 | FaceDetailer: why the working size matters | `workflows/face_detailer.json`, `images/explorer_anchor.png`; recorded `11_detailer_default_sizes`, `11_detailer_max_size_512` | Install the Impact Pack and Subpack from the missing-nodes panel, load the explorer, run with the default sizes and denoise 0.4, then with max size 512, and read the console line that names the sampling size. |
| 23:52 | Qwen face repair and Transfer Color drift fix | `workflows/qwen_face_repair.json`, `recorded_inputs/`; recorded `12_face_repair`, `12_face_repair_transfer_color` | Paint the face in the mask editor (mask pen, opacity 1, thickness 40) and run. Then add Transfer Color between Split Image with Alpha and the stitch (method histogram) and run again. |
| 26:43 | Colorize a 1961 NASA photo and check what changed | `images/mercury7_nasa_s61-01250_color.jpg`, `workflows/Qwen_image_edit_lecture04.json`, [commands.md](commands.md); recorded `13_colorize` | Make the black and white copy, upload it, paste the instruction, set the resolution to 1536 and run. Compare with the recorded colours, recombine with Luminize and measure both RMSE values. |
| 29:54 | Destination spec, color space and 16-bit export | the SeedVR2 template tab; recorded `14_print_master_with_alpha`, `14_print_master_rgb`, `14_print_master_linear_mismatch` | Add Save Image (Advanced) (PNG, 16-bit) and Convert Image Color Space (sRGB to sRGB), export and check with ExifTool. Add Split Image with Alpha, export and check again, then try the linear mismatch and set it back. |
| 33:31 | What the file tells a stranger: metadata and the client launcher | `launchers/run_comfyui_CLIENT.bat`, [commands.md](commands.md); recorded `15_print_master_client` | Read the first watchmaker's metadata with `exiftool -a -G1`, restart with the client launch file, export again and read the new file. |
| 35:07 | The chart test: AI upscaler vs ImageMagick Lanczos | `workflows/chart_test.json`, `images/chart_orders_640.png`, [commands.md](commands.md); recorded `16_chart_real_esrgan` | Connect the chart to Real-ESRGAN and read every label at full size, then enlarge the chart with ImageMagick's Lanczos filter and read it again. |
| 36:40 | The complete delivery chain and final verification | `workflows/delivery_chain.json`, `workflows/delivery_chain_recipe.json`; recorded `17_delivery_chain` | Run restore, detail, colour match, grain, colour space and save on the client server, check the delivery with ExifTool, then export the workflow as your recipe. |
| 38:39 | Recap and next lecture | — | — |

## Files

| Location | Purpose |
|---|---|
| `Lecture07_Files/Lecture07_prompts.txt` | The course notes: the watchmaker prompt, the colorization instruction, every ImageMagick and ExifTool command, the print master destination and the client launch line. |
| `Lecture07_Files/workflows/` | The nine workflows the lecture opens, plus `delivery_chain_recipe.json`, the file it exports at 38:17. |
| `Lecture07_Files/images/` | The three input images: the chart, the explorer portrait from Lecture 4 and NASA photograph S61-01250 in its recorded colours. |
| `Lecture07_Files/launchers/` | `run_comfyui.bat` and `run_comfyui_CLIENT.bat`, which adds `--disable-metadata`. |
| `Lecture07_Files/gpu_memory.bat` | The GPU memory window of chapter 9. |
| `recorded_workflows/` | The exact graph of each of the 19 recorded runs: the `.json` file opens in ComfyUI, the `.api.json` file is the same run as an API prompt. `index.json` lists each run's chapter, inputs and outputs with their SHA-256. |
| `recorded_results/` | The original outputs of the recorded runs, and in `commands/` the files the ImageMagick commands wrote; bytes unchanged. |
| `recorded_inputs/` | The explorer with the face mask painted in chapter 12, which the recorded face repair graphs load. |
| [commands.md](commands.md) | Every command with its timestamp and recorded output. |
| [MODELS.md](MODELS.md) | Model files, node packs and tools with their folders, versions, links and SHA-256. |
| `file_manifest.json` | SHA-256 and size of every file in this ZIP. |

## Recorded graphs and results

- The course workflows are the starting points the lecture opens. The routes of chapters 4-6, the Transfer Color of chapter 12 and the export nodes of chapters 14-15 are added on camera; to open a graph exactly as it ran, use `recorded_workflows/`.
- A recorded graph reads its inputs by name; `index.json` lists them. Copy them into `ComfyUI\input` first: `watchmaker_2048_00001_.latent` from `recorded_results/09_latent_2048/`, `mercury7_bw.png` from `recorded_results/commands/` and the painted mask from `recorded_inputs/`. `Lecture07/watchmaker_00001_.png [output]` is the chapter 3 result in `ComfyUI\output\Lecture07\` (`recorded_results/03_watchmaker_1024/`).
- The SeedVR2 template opens with the template's own example picture named in its Load Image; replace it with your watchmaker as in chapter 7. The Lecture 4 edit workflow opens with Lecture 4's `portrait_cafe.png`; upload `mercury7_bw.png` in its place.
- The four print masters of chapters 14 and 15 are not included: they are 16-bit 4096 × 4096 PNGs of 65 to 75 MB each. Their graphs are included and rebuild them in seconds from the chapter 3 image; their ExifTool readings are in commands.md.
- The PNGs saved on the normal server carry their graph as metadata. `chart_gan_00001_.png` (chapter 16) and `delivery_00001.png` (chapter 17) were saved on the client server and carry none; their graphs are in `recorded_workflows/`.
- Your results can differ in small details on another GPU, driver or ComfyUI version even with the same seeds. Compare them with these files at the same zoom, and read numbers and letters rather than judging sharpness.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `'magick' is not recognized` | the installer's PATH option was not ticked, or the window is older than the install | run the installer again with **Add application directory to your system path** ticked, then open a new Command Prompt |
| `'exiftool' is not recognized` | its folder is not on Path, or the window is older than the change | add the folder that holds `exiftool.exe` to your Path, then open a new Command Prompt |
| A workflow reports missing nodes | the Impact Pack and Subpack, or Crop-and-Stitch, are not installed | install them from the missing-nodes panel and apply the changes ([MODELS.md](MODELS.md)) |
| Load Latent lists no file | Save Latent writes into `output\latents`, Load Latent reads `input` | move the `.latent` file into `ComfyUI\input` and press R |
| Numbers or letters changed after upscaling | a learned upscaler invents detail | enlarge text and charts with Lanczos, or render them again from the source data |
| A repaired face has a different colour | the edit drifted from the photograph's palette | add Transfer Color before the stitch, with the repaired crop as target and the original crop as reference |
| The export is much darker | Convert Image Color Space's destination differs from the saver's input colour space | set both to the same value (sRGB for this print master) |
| The export carries an alpha channel you did not want | the restoration template keeps the loaded image's alpha | Split Image with Alpha before the colour space converter |
| A client's file carries your prompt and workflow | ComfyUI writes them into every PNG by default | start ComfyUI with `run_comfyui_CLIENT.bat` (`--disable-metadata`) and check the file with ExifTool |
| A transparent asset loses its alpha as AVIF | AVIF stores 1 or 3 channels | save it as PNG |

## Before you deliver

Write the destination first (pixel size, colour space, bit depth, alpha, metadata), read every number and letter of the result at full size, label a colorized photograph as colorized, check the delivered file with ExifTool against the destination, and keep the recipe JSON beside your files when the delivered image carries no workflow.

Source photograph: NASA S61-01250 (1961), the Mercury Seven astronauts. Download model weights, ImageMagick and ExifTool from the publishers linked in MODELS.md.


## Chapters and file checks

[Chapters](chapters.txt) · [Video title](youtube_title.txt) · [Video description](youtube_description.txt) · [File checksums](SHA256SUMS.txt)
