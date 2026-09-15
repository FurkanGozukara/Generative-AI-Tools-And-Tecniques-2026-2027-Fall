# Z-Image Turbo models and folders

The supplied workflow uses **three separate model files**. Download them from the Comfy-Org publisher links below. Model weights are not included in the companion ZIP.

## Download the exact filenames

| Role | File and direct publisher download | Recorded file size |
|---|---|---:|
| Diffusion model | [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) | 12,309,866,400 bytes |
| Text encoder | [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) | 8,044,982,048 bytes |
| VAE | [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) | 335,304,388 bytes |

Together these are approximately **20.7 GB on disk** in decimal units. Allow additional space for downloads, packages, caches and outputs. These file sizes are the course's recorded downloads, not a GPU-memory requirement.

The [official ComfyUI tutorial](https://docs.comfy.org/tutorials/image/z-image/z-image-turbo) lists the same filenames and categories. Consult the [model repository](https://huggingface.co/Comfy-Org/z_image_turbo) and the [original Z-Image project](https://github.com/Tongyi-MAI/Z-Image) for model information and license terms. Download only from the intended publisher; do not rename an unrelated model to match one of these filenames.

## Option A — models inside ComfyUI

For the simplest installation, place the files here, relative to your `ComfyUI_Week01` folder:

```text
ComfyUI_Week01/
  models/
    diffusion_models/
      z_image_turbo_bf16.safetensors
    text_encoders/
      qwen_3_4b.safetensors
    vae/
      ae.safetensors
```

This route does not need the shared-model YAML template.

## Option B — a shared model library

This is useful when several installations need the same large files. In the public example, create:

```text
C:/AI/Shared_Models_Week01/
  models/
    diffusion_models/
      z_image_turbo_bf16.safetensors
    text_encoders/
      qwen_3_4b.safetensors
    vae/
      ae.safetensors
```

Copy [extra_model_paths.yaml](extra_model_paths.yaml) into the root of `ComfyUI_Week01`, beside `main.py`. Edit `base_path` to the folder **above** `models` on your computer. Keep the category names, forward slashes and space indentation. Save the filename as exactly `extra_model_paths.yaml`, not `.yaml.txt`.

If you already have a model-path configuration, back it up and merge this named section without replacing the existing sections. The [plain-text companion](Week01_Shared_Model_Paths.txt) contains the same YAML for easy reference. Restart ComfyUI after changing the mapping. The official [extra model paths instructions](https://docs.comfy.org/installation/manual_install#adding-extra-model-paths) explain this configuration.

Choose one storage route for these files; you do not need to keep duplicate 20.7 GB copies in both locations.

## Load and run the supplied workflow

1. Start ComfyUI with the command sheet. Open the address printed in its terminal.
2. Load [Week01_LocalModels_Proof.json](Week01_LocalModels_Proof.json) using Open, Ctrl+O or drag-and-drop onto the canvas.
3. Check the three model selections. If a name is missing, inspect the folder mapping and completed download, restart the server, and reselect the file.
4. Run the workflow and wait for the saved image. The output prefix is `z-image-turbo`; later runs may get different file numbers.

The saved lecture configuration is:

| Setting | Value |
|---|---|
| Seed submitted to the sampler | `170592213851282` |
| Width × height | `1024 × 1024` |
| Batch size | `1` |
| Steps | `8` |
| CFG | `1` |
| Sampler / scheduler | `res_multistep` / `simple` |
| Denoise | `1` |
| Flow shift | `3` |

The template groups the core nodes inside a subgraph. Its connected outer inputs supply the prompt, dimensions and seed; an unconnected-looking default inside the group is not necessarily the value sent during execution. Load the supplied JSON or original PNG instead of manually rebuilding it from a screenshot.

To save a matching JSON after a run, restore the seed that was submitted before using Save As. Follow [PNG_Workflow_Recovery.md](PNG_Workflow_Recovery.md). Keep the same models and software versions when reproducing the example; a fixed seed alone does not make different software stacks produce byte-identical images.
