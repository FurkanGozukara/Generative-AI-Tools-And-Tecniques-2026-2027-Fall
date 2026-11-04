# Lecture 8 models and compatibility

The files retain the recorded model selections. The smaller delivery graph, exported app and API example use the four models below. The [Lecture 7 model guide](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/blob/main/lecture-07/MODELS.md) gives their publisher download links and recorded hashes.

| File | Folder inside ComfyUI | Purpose |
|---|---|---|
| `z_image_turbo_bf16.safetensors` | `models/diffusion_models/` | Z-Image Turbo diffusion model |
| `qwen_3_4b.safetensors` | `models/text_encoders/` | Prompt encoder, using the recorded `lumina2` selection |
| `ae.safetensors` | `models/vae/LectureTwo/` | VAE; delivery and API examples select `LectureTwo\ae.safetensors` |
| `RealESRGAN_x4plus.safetensors` | `models/upscale_models/` | Upscaling inside the exposed subgraph |

If your VAE is directly in `models/vae/`, select `ae.safetensors` in the editor or change node `4`'s `vae_name` in a working copy of the API export. Keep the unchanged supplied export for comparison. The initial crowded graph selects `ae.safetensors` directly, so match its VAE loaders to your own folder as well.

The crowded `seven_weeks_everything.json` is the organization exercise assembled from earlier lectures. Its watercolor branch selects `FLUX_Dev_fp8_scaled.safetensors`, `Aquarelle_IV-8.safetensors`, `clip_l.safetensors` and `t5xxl_enconly.safetensors`; see the [Lecture 3 model notes](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/tree/main/lecture-03). Its face-detailing branch selects `bbox/face_yolov8m.pt` and uses Impact Pack and Impact Subpack. Its inpainting branch uses Inpaint CropAndStitch. These branches are independent of the smaller API example. The two image inputs used by the starting graph are included in `inputs/` with their original filenames.

Recorded core commit: `6d352802d8f8b9133f664a1757d6c6d26390c335`. Recorded frontend: `1.57.6`. The full dependency list and Manager snapshot are in [environment/](environment/README.md). They describe the recorded state, rather than a requirement to overwrite another working installation. No model weights or installers are included.
