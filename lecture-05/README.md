# Lecture 5 — Masks, Inpainting, Outpainting, Segmentation & Compositing

**Generative AI Full Course - Lecture 5: Select Objects with Words Using SAM3**

▶️ **[Watch Lecture 5](https://youtu.be/DJcgVASlg38)** · 📺 **[Full course playlist](https://www.youtube.com/playlist?list=PLUMEJUep1hiI)**

Choose exactly where an image changes. In this 51:51 lecture you paint hard and soft masks, repair an invented signature with Differential Diffusion, extend a scene, select objects with words using SAM3, edit a face inside a 4096-pixel photograph with Crop-and-Stitch, create a transparent asset and move an object between Qwen-Image-Layered layers.

## Download and follow along

Download the [complete companion ZIP](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/releases/download/lecture-05/Lecture_05_Companion_Files.zip) (186 MB), extract it, then open `lecture-05/README.md`. It contains 32 workflow recipes in editable UI and API forms, 48 input files, 63 saved results from the recorded runs, the model links and the commands. Because its full-resolution images are large, the ZIP is attached to the [Lecture 5 release](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/releases/tag/lecture-05) rather than the `downloads` folder. The guides and workflows are also readable here on GitHub; the `inputs/` and `results/` images are in the ZIP.

Use the ComfyUI installation from [Lectures 1–4](../lecture-04/README.md). The editing graphs reuse its Z-Image-Turbo and Qwen-Image 2.1 models.

1. Update ComfyUI, save a Manager snapshot and install **ComfyUI-Inpaint-CropAndStitch** by **lquesada** with the [recorded commands](commands.md).
2. Download the SAM3 and Qwen-Image-Layered files, and any editing model you have not installed yet, from [MODELS.md](MODELS.md). Place each file in its listed folder. Qwen-Image-Layered uses its own diffusion model, text encoder and RGBA VAE; do not substitute the editing VAE.
3. Copy all files in the ZIP's `inputs/` folder into your `ComfyUI/input` folder. Keep the supplied masks as well as the photographs: mask edges and polarity affect the comparison.
4. Open a graph from [workflows/](workflows/) with ComfyUI's **File → Open** command and select the matching installed models. Input filenames have been adapted to the supplied files. Files ending in `.api.json` describe the same executed recipes for API users.
5. Follow the [chapter list](chapters.txt) and compare your outputs with the ZIP's `results/` folder. The [video description](youtube_description.txt) lists the same chapters and resources. The [published video title](youtube_title.txt) is also included as plain text.

## Workflows by chapter

| Starts at | Workflows | What to do |
|---|---|---|
| [5:55](https://www.youtube.com/watch?v=DJcgVASlg38&t=355s) Masks | `01_Mask_Editor`, `21_Hard_Soft_Mask_Preview`, `22_Colour_Selection` | Paint hard and soft masks and select a garment by colour. Distinguish the mask pen from painting RGB pixels, and inspect what the receiving node does with the mask. |
| [10:59](https://www.youtube.com/watch?v=DJcgVASlg38&t=659s) Signature repair | `02_Signature_Hard`, `03_Signature_Graded`, `13_Signature_Hard_Denoise1`, `14_Signature_Graded_Denoise1`, `15_Signature_Final_Composite` | Repair the invented signature in the actual Lecture 3 watercolor. Compare hard and graded selections with the same model, prompt, seed and sampling settings, repeat both at denoise 1.0, then composite onto the original. |
| [20:22](https://www.youtube.com/watch?v=DJcgVASlg38&t=1222s) Grey-value ramp | `04_Ramp` | Read a grey mask as a start-time map with Differential Diffusion. |
| [22:09](https://www.youtube.com/watch?v=DJcgVASlg38&t=1329s) Outpainting | `05_Outpainting`, `16_Outpaint_Final_Composite` | Extend the workshop scene with a matched editing graph, then restore the original region. |
| [24:17](https://www.youtube.com/watch?v=DJcgVASlg38&t=1457s) SAM3 selection | `06_SAM_Car`, `06_SAM_Jacket`, `06_SAM_Windows` | Select the red car, jacket and windows with words. Inspect the actual instance masks rather than assuming the requested count was found. |
| [28:30](https://www.youtube.com/watch?v=DJcgVASlg38&t=1710s) Face edit | `23_Face_Source_Resize`, `24_Face_Selection_Mask`, `07_Face_WholeFrame`, `08_Face_Crop_Stitch`, `17_Face_Final_Composite` | Compare whole-frame and crop/stitch face edits on the same 4096-pixel-long-edge working photograph, then restore the pixels outside the edit. |
| [36:01](https://www.youtube.com/watch?v=DJcgVASlg38&t=2161s) Transparency | `09_Native_Alpha`, `25_Loader_Mask` to `30_Alpha_SAM_Comparison`, `18_Lantern_Placement`, `19_Lantern_Colour`, `20_Lantern_Saved_Checks` | Generate native alpha, composite over light and dark backgrounds, save and reopen the transparent image, then place the asset and match its colour. |
| [44:07](https://www.youtube.com/watch?v=DJcgVASlg38&t=2647s) Image layers | `10_Layer_Decomposition`, `11_Layer_Recomposition`, `12_Layer_Moved` | Inspect Qwen-Image-Layered's reconstruction and ordered layers, then move a foreground layer and inspect the newly exposed background. |

[recorded_results.json](recorded_results.json) maps each workflow to its saved results and their SHA-256 hashes.

## Files

| Location | Purpose |
|---|---|
| `inputs/` (in the ZIP) | Untouched source images. Generated sources retain their original bytes. |
| [workflows/](workflows/) | Editable ComfyUI graphs. Files ending in `.api.json` are API representations of the same recipes. |
| `results/` (in the ZIP) | Actual saved outputs from the recorded runs, including initial attempts and corrected final composites. |
| [recorded_results.json](recorded_results.json) | Workflow-to-result mapping and saved-file SHA-256 hashes. |
| [MODELS.md](MODELS.md) | Exact model loader names, download links and destination folders. |
| [commands.md](commands.md) | Update, Manager snapshot and Crop-and-Stitch installation steps. |
| [check_outside_pixels.py](check_outside_pixels.py) | Exact RGB comparison outside the accepted composite mask, at matching image dimensions. |
| [chapters.txt](chapters.txt), [youtube_description.txt](youtube_description.txt), [youtube_title.txt](youtube_title.txt) | Chapter list, video description and title. |
| [SHA256SUMS.txt](SHA256SUMS.txt) | Checksums of every extracted companion file, including the images in the ZIP. |

The crop/stitch graph needs its custom node pack. SAM3 and Qwen-Image-Layered need their own matching model files. Model weights are separate publisher downloads.

## What to inspect

The initial signature repairs at denoise 0.75 retained small dark fragments. The later denoise 1.0 runs remove more of the mark but change the local wash; the final composite limits changes to its mask support. The ramp example produces partial warmth and invented writing. These imperfect results are retained so you can inspect what actually happened.

The measured face runs took 11.448 and 12.862 seconds, but their output sizes and loading/cache conditions differ. They do not establish a controlled speed comparison. Inspect the corresponding outputs at matching source scale.

The saved transparent-image alpha differed by at most one code value on reload. The moved layered lantern reveals soft, inferred wood and leaves the original reflection behind; those areas are not recovered ground truth.

A diffusion noise mask selects where the model participates. It does not by itself prove that decoded pixels elsewhere are identical. For exact preservation, composite the edited region over the original using the intended final mask, save both images and compare the pixels where that mask is zero.

Run the comparison utility's `--help` command for its current arguments. Use the actual full-resolution mask consumed by the final composite. A small crop mask cannot establish a claim about the whole photograph, and a feathered boundary belongs to the changed support.

The optional comparison utility needs Python, NumPy and Pillow. In the Python environment you want to use, install its dependencies with `python -m pip install numpy pillow`, then run `python check_outside_pixels.py --help`. It reads the supplied images and reports differences without editing them.

With transparency, inspect the saved alpha channel and the asset over both light and dark backgrounds. A checkerboard painted into RGB pixels is not transparency. Verify the polarity of each mask output before connecting it to another node; different nodes can expose alpha or its inverse.

Layer decomposition infers occluded content. Preserve the generated layer order, compare the reconstruction with the original, and inspect newly exposed areas after moving an object. Do not assume those areas are recovered ground truth.

## Source credits

- The watercolor is the accepted Lecture 3 Z-Image-Turbo / watercolor LoRA result, retained unchanged with its source workflow provenance.
- The workshop scene and lantern product photograph were created with native image generation for this lecture; full prompts and original file hashes are retained in the production provenance.
- Portrait photograph: [Toàn Văn on Pexels](https://www.pexels.com/photo/man-wearing-jean-jacket-standing-on-street-17894651/), under the [Pexels license](https://www.pexels.com/license/). The original is 5304 × 7952 pixels; the lesson explicitly creates its 4096-pixel-long-edge working image. No endorsement is implied.
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) supplies the core nodes. [lquesada's Crop-and-Stitch pack](https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch) supplies the local crop/stitch operations. Model and algorithm authors retain credit; the lesson's original contributions are its teaching examples, graph recipes and verification utilities.

[SHA256SUMS.txt](SHA256SUMS.txt) lists the companion-file checksums.
