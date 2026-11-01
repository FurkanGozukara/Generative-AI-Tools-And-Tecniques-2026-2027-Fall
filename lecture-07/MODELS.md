# Models, node packs and tools

No model weights or installers are included in this ZIP. The table lists every model the lecture loads, with the folder and file name its loaders expect. Each Hugging Face link was checked on October 27, 2026; the SHA-256 values below are the ones the links report.

## Model files

| File | Folder inside ComfyUI | Used in | Download |
|---|---|---|---|
| `z_image_turbo_bf16.safetensors` | `models/diffusion_models/` | chapters 3-6, 9, 11, 17 | [pinned file](https://huggingface.co/Comfy-Org/Z-Image-Turbo/resolve/6fc90a3b1b653e935a0d175e260736de25b84df5/split_files/diffusion_models/z_image_turbo_bf16.safetensors) (Lecture 2) |
| `qwen_3_4b.safetensors` | `models/text_encoders/` | chapters 3-6, 9, 11, 17 | [pinned file](https://huggingface.co/Comfy-Org/Z-Image-Turbo/resolve/6fc90a3b1b653e935a0d175e260736de25b84df5/split_files/text_encoders/qwen_3_4b.safetensors) (Lecture 2) |
| `ae.safetensors` | `models/vae/` | chapters 3-6, 9, 11, 17 | [pinned file](https://huggingface.co/Comfy-Org/Z-Image-Turbo/resolve/6fc90a3b1b653e935a0d175e260736de25b84df5/split_files/vae/ae.safetensors) (Lecture 2) |
| `qwen_image_2.1_int8_convrot.safetensors` | `models/diffusion_models/` | chapters 12, 13 | [pinned file](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) (Lecture 4) |
| `qwen3vl_8b_int8_convrot.safetensors` | `models/text_encoders/` | chapters 12, 13 | [pinned file](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/text_encoders/qwen3vl_8b_int8_convrot.safetensors) (Lecture 4) |
| `qwen_image_2.1_vae_bf16.safetensors` | `models/vae/` | chapters 12, 13 | [pinned file](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/vae/qwen_image_2.1_vae_bf16.safetensors) (Lecture 4) |
| `RealESRGAN_x4plus.safetensors` | `models/upscale_models/` | chapters 5, 6, 16 | [download page](https://huggingface.co/Comfy-Org/Real-ESRGAN/blob/main/RealESRGAN_x4plus.safetensors) shown at 5:23; 66,857,836 bytes |
| `seedvr2_3b_int8_convrot.safetensors` | `models/diffusion_models/` | chapters 7, 14, 15, 17 | [download page](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors) shown at 11:14; 3,458,259,704 bytes |
| `seedvr2_ema_vae_fp16.safetensors` | `models/vae/` | chapters 7, 14, 15, 17 | [download page](https://huggingface.co/Comfy-Org/SeedVR2/blob/main/vae/seedvr2_ema_vae_fp16.safetensors) shown at 11:14; 501,324,814 bytes |
| `face_yolov8m.pt` | `models/ultralytics/bbox/` | chapters 11, 17 | downloaded by the Impact Subpack installer when you choose **Install All** and **Apply Changes** (21:22-21:52) |

Keep the downloaded file names. Press **R** in ComfyUI, or restart it, after adding a file so the loaders list it.

The course workflows select the Z-Image Turbo VAE as `LectureTwo\ae.safetensors`, the copy Lecture 2 placed in a `LectureTwo` subfolder of the VAE folder. If your copy sits directly in `models/vae/`, select `ae.safetensors` in each Load VAE node. The Lecture 4 edit workflow and the face repair workflow use the three Qwen-Image 2.1 files; Real-ESRGAN, SeedVR2 and the face detector are new in this lecture.

SHA-256 of each download, as its link reports it. The lecture's own Z-Image Turbo, Real-ESRGAN, SeedVR2 and Qwen-Image 2.1 diffusion files have exactly these values:

| File | SHA-256 |
|---|---|
| `z_image_turbo_bf16.safetensors` | `2407613050b809ffdff18a4ac99af83ea6b95443ecebdf80e064a79c825574a6` |
| `qwen_3_4b.safetensors` | `6c671498573ac2f7a5501502ccce8d2b08ea6ca2f661c458e708f36b36edfc5a` |
| `ae.safetensors` | `afc8e28272cd15db3919bacdb6918ce9c1ed22e96cb12c4d5ed0fba823529e38` |
| `qwen_image_2.1_int8_convrot.safetensors` | `cb74113cb03faecd79611b01fd7fd642f0aa60d6f0b95086abee214d75eaa57d` |
| `qwen3vl_8b_int8_convrot.safetensors` | `8bfd0f6e12abf2d2d697ecc888e5e90b0d6741d6708f05799f53afa560452e8f` |
| `qwen_image_2.1_vae_bf16.safetensors` | `bb21f7473051e1ac368515dd3f2e15cd44d7a11748ee8823e1ddca3e4876b7c9` |
| `RealESRGAN_x4plus.safetensors` | `37f9a931c215f040aa6d50f711f2cb115f713c46df1d0d6469a8bd7bfe9a60bb` |
| `seedvr2_3b_int8_convrot.safetensors` | `c3dec8bcc5916843a8a858572970597462e1f2dc598d6dfd818f6cd40f53a157` |
| `seedvr2_ema_vae_fp16.safetensors` | `20678548f420d98d26f11442d3528f8b8c94e57ee046ef93dbb7633da8612ca1` |
| `face_yolov8m.pt` | `717923c19b3f4bbf5250b728f1fa6b2cb72a33aed1d236ea9caf0e21ad943e5f` (the copy the Subpack installer downloaded, 52,026,019 bytes) |

## Custom node packs

| Pack | Version recorded | Nodes used | How it was installed |
|---|---|---|---|
| [ComfyUI Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) | 8.28.3 | FaceDetailer | **Install All**, then **Apply Changes**, in the panel ComfyUI opens for the missing nodes of `face_detailer.json` (chapter 11) |
| [ComfyUI Impact Subpack](https://github.com/ltdrdata/ComfyUI-Impact-Subpack) | 1.3.5 | UltralyticsDetectorProvider | the same Install All; its installer downloads `face_yolov8m.pt` |
| [ComfyUI-Inpaint-CropAndStitch](https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch) | 3.0.17 | Inpaint Crop, Inpaint Stitch | installed in Lecture 5; needed by `qwen_face_repair.json` |

Every other node in this lecture is a ComfyUI core node of version 0.42.0: Upscale Image, Load Upscale Model, Upscale Image (using Model), Split Image into List of Tiles, Merge List of Tiles to Image, the SeedVR2 nodes of the official template, VAE Decode (Tiled), Save Latent, Load Latent, Split Image with Alpha, Transfer Color, Convert Image Color Space, Add Noise to Image and Save Image (Advanced).

## Command-line tools

| Tool | Version recorded | Download |
|---|---|---|
| ImageMagick | 7.1.1-44 Q16-HDRI x64 | Windows installer from [imagemagick.org/download](https://imagemagick.org/download/#windows); tick **Add application directory to your system path** |
| ExifTool | 13.59 | 64-bit Windows Executable zip from [exiftool.org](https://exiftool.org/); unpack and add to PATH as in [commands.md](commands.md) |
