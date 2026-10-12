# Models and folders

Use the matching files named in each workflow. Copy source images into `ComfyUI/input`. Install Crop-and-Stitch 3.0.17 through Manager. Core node version recorded: ComfyUI 0.39.0; frontend 1.55.14.

| File | Folder | Download |
|---|---|---|
| `sam3.1_multiplex_fp16.safetensors` | `ComfyUI/models/checkpoints/` | [Pinned model file](https://huggingface.co/Comfy-Org/sam3.1/resolve/7bb8374780a725b4353ed31f3a9395c9742b5621/checkpoints/sam3.1_multiplex_fp16.safetensors) |
| `qwen_image_layered_fp8mixed.safetensors` | `ComfyUI/models/diffusion_models/` | [Pinned model file](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/02130716aaf54a36f84c9fcfa8a373ab06284e2b/split_files/diffusion_models/qwen_image_layered_fp8mixed.safetensors) |
| `qwen_image_layered_vae.safetensors` | `ComfyUI/models/vae/` | [Pinned model file](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/02130716aaf54a36f84c9fcfa8a373ab06284e2b/split_files/vae/qwen_image_layered_vae.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `ComfyUI/models/text_encoders/` | [Pinned model file](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/1405a2b738c29b890cf6d03fc038d8d3e92eeed7/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_2.1_int8_convrot.safetensors` | `ComfyUI/models/diffusion_models/` | [Pinned model file](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) |
| `qwen3vl_8b_int8_convrot.safetensors` | `ComfyUI/models/text_encoders/` | [Pinned model file](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/text_encoders/qwen3vl_8b_int8_convrot.safetensors) |
| `qwen_image_2.1_vae_bf16.safetensors` | `ComfyUI/models/vae/` | [Pinned model file](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/vae/qwen_image_2.1_vae_bf16.safetensors) |
| `z_image_turbo_bf16.safetensors` | `ComfyUI/models/diffusion_models/` | [Pinned model file](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/6fc90a3b1b653e935a0d175e260736de25b84df5/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `qwen_3_4b.safetensors` | `ComfyUI/models/text_encoders/` | [Pinned model file](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/6fc90a3b1b653e935a0d175e260736de25b84df5/split_files/text_encoders/qwen_3_4b.safetensors) |
| `ae.safetensors` | `ComfyUI/models/vae/` | [Pinned model file](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/6fc90a3b1b653e935a0d175e260736de25b84df5/split_files/vae/ae.safetensors) |

The local editing graphs reuse the Z-Image-Turbo and Qwen-Image 2.1 installation from Lectures 3 and 4. The layered model uses its separate Qwen 2.5 VL text encoder and RGBA VAE; do not substitute the editing VAE.

## Exact loader names in the recorded workflows

- `ae.safetensors`
- `qwen3vl_8b_int8_convrot.safetensors`
- `qwen_2.5_vl_7b_fp8_scaled.safetensors`
- `qwen_3_4b.safetensors`
- `qwen_image_2.1_int8_convrot.safetensors`
- `qwen_image_2.1_vae_bf16.safetensors`
- `qwen_image_layered_fp8mixed.safetensors`
- `qwen_image_layered_vae.safetensors`
- `sam3.1_multiplex_fp16.safetensors`
- `z_image_turbo_bf16.safetensors`
