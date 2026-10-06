# Lecture 4 — Image Editing and Instruction Models

Companion files for the completed 30:48 lecture: image-to-image denoise, instruction edits, preservation, difference maps, text replacement, two references, character consistency, sequential edits and relighting.

Download the [companion ZIP](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/raw/refs/heads/main/downloads/Lecture_04_Companion_Files.zip), extract it and open `lecture-04/README.md`. Use the ComfyUI installation from [Lectures 1–3](../lecture-03/README.md).

## Start here

1. Follow [the update and restart commands](commands.md). Download the three matching Qwen Image 2.1 files from [model sources](model_sources.md), place them in the listed folders and select their exact filenames in the loaders.
2. Upload the eight pictures from [inputs/](inputs/) through Load Image, or copy them to your installation's `ComfyUI/input` folder.
3. Open [Qwen_text_to_image_start.json](workflows/Qwen_text_to_image_start.json) for the starting graph. It retains Lecture 3's travel-poster prompt and output prefix; chapter 3 converts it to image-to-image.
4. Open [Qwen_image_edit_lecture04.json](workflows/Qwen_image_edit_lecture04.json) for the final graph exported in chapter 15. It opens on portrait relighting with `portrait_cafe.png` selected. It also contains the difference-map branch and a second Load Image node. Change the image selections and instruction for another chapter.
5. Follow the [chapter list](chapters.txt) and copy the matching text from [instructions.md](instructions.md). The [video description](youtube_description.txt) also lists the chapters and resources.

The package contains two visual-editor workflows, 24 API graphs with the intermediate recipes, eight input images and seven result images used as inputs or continuation assets. Model weights are separate publisher downloads.

## Intermediate recipes and image dependencies

The files in [workflows/api/](workflows/api/) are API payloads. Inspect their node values to reproduce an intermediate graph, or use them through the ComfyUI API if you already know that interface. Open the two ordinary JSON workflows above in the visual editor.

Each API graph's original image names must resolve in your installation. For names ending in `[output]`, [api_image_paths.json](api_image_paths.json) maps the expected `ComfyUI/output/Lecture04/...` location to an included image. Copy the image to that location before queuing the exact payload, or update its Load Image selection. The five dependency images support the sequential-edit chain. The platform, hilltop and workshop storyboard frames in [images/](images/), together with `inputs/explorer_anchor.png`, are also the continuation assets for the later video lectures.

## Settings and comparisons

The main recipe uses seed 314159 (fixed), 25 steps, CFG 1, Euler/simple and a 1024 pixel budget. Instruction edits use denoise 1; the image-to-image sweep uses 0.2, 0.4, 0.6 and 0.8. Chapter 8 compares that budget with the full 2048 input. Each API graph preserves its exact settings and connections.

The difference branch is a one-sided green-channel comparison with threshold 0.04. It does not measure every RGB change or certify identity preservation. Compare its VAE round-trip baseline, then inspect the images themselves. Chapter 13 contrasts five sequential edits with a clean one-pass rollback.

[measurements.json](measurements.json) identifies the RTX 5090, software versions, model, settings and compared run conditions. These are the recorded measurements, not minimum VRAM requirements or a general benchmark. Other hardware, versions or settings can produce different images and timings.

[SHA256SUMS.txt](SHA256SUMS.txt) lists the companion-file checksums.
