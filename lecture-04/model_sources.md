# Model downloads (Qwen Image 2.1)

The same three files as Lecture 3; downloads verified on September 24, 2026 (HTTP 200, hashes below). No model weights are included in this archive.

## qwen_image_2.1_int8_convrot.safetensors

- Download: [qwen_image_2.1_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/diffusion_models/qwen_image_2.1_int8_convrot.safetensors)
- Model card and terms: [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1); repository label: qwen-research.
- Install folder: `ComfyUI/models/diffusion_models`.
- Source SHA256: `cb74113cb03faecd79611b01fd7fd642f0aa60d6f0b95086abee214d75eaa57d`; 7,256,783,064 bytes.

## qwen3vl_8b_int8_convrot.safetensors

- Download: [qwen3vl_8b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/text_encoders/qwen3vl_8b_int8_convrot.safetensors)
- Model card and terms: [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1); repository label: qwen-research.
- Install folder: `ComfyUI/models/text_encoders`.
- Source SHA256: `8bfd0f6e12abf2d2d697ecc888e5e90b0d6741d6708f05799f53afa560452e8f`; 9,350,798,360 bytes.

## qwen_image_2.1_vae_bf16.safetensors

- Download: [qwen_image_2.1_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/vae/qwen_image_2.1_vae_bf16.safetensors)
- Model card and terms: [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1); repository label: qwen-research.
- Install folder: `ComfyUI/models/vae`.
- Source SHA256: `bb21f7473051e1ac368515dd3f2e15cd44d7a11748ee8823e1ddca3e4876b7c9`; 675,509,688 bytes.

Keep the downloaded filenames. The supplied CLIP Loader selects `qwen3vl_8b_int8_convrot.safetensors`; select that name after placing it in `ComfyUI/models/text_encoders`. The diffusion-model and VAE loaders use the filenames shown above. Refresh the model lists or restart ComfyUI after adding files.
