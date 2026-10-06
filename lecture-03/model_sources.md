# Verified model downloads and filename mapping

Nine of the ten inspected Week 3 files have verified public downloads: six are byte-identical, and the three Qwen files have verified identical tensor payloads with different metadata headers. All nine download URLs returned HTTP 200 to an unauthenticated HEAD request on September 24, 2026. No model weights are included in this archive.

The local FLUX FP8 comparison file is the explicit exception below. The Week 1 Z-Image components and `ae.safetensors` remain prerequisites from Lecture 1.

Use the download links below, then choose that filename in the corresponding loader. To use the saved workflow without changing its selection, use the local name recorded in `model_manifest.json`. The reference Qwen/Klein workflows already use the longer encoder download names; the exact recorded workflows retain local aliases.

A `/resolve/` link downloads model bytes. A `/raw/` link for these large files only returns a Git LFS pointer. Repository license labels below are reported metadata, not a replacement for the model card and upstream terms. Public access does not imply unrestricted use.

## qwen_image_2.1_int8_convrot.safetensors

- Download: [qwen_image_2.1_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/diffusion_models/qwen_image_2.1_int8_convrot.safetensors)
- Model card and terms: [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1); repository label: qwen-research.
- Install folder: `ComfyUI/models/diffusion_models`.
- Source SHA256: `cb74113cb03faecd79611b01fd7fd642f0aa60d6f0b95086abee214d75eaa57d`; 7,256,783,064 bytes.
- Relationship to the recorded file: Same tensor payload verified by reconstruction; local metadata header was repacked. See qwen_tensor_verification.

## FLUX_Dev.safetensors

- Download: [flux1-dev.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/83c446ef27a6ac1e9e36ecf13257283aa12cf22a/flux1-dev.safetensors)
- Model card and terms: [Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev); repository label: flux-1-dev-non-commercial-license.
- Install folder: `ComfyUI/models/diffusion_models`.
- Source SHA256: `4610115bb0c89560703c892c59ac2742fa821e60ef5871b33493ba544683abd7`; 23,802,932,552 bytes.
- Relationship to the recorded file: Byte-identical download; use the local filename saved in the chosen workflow or change its loader selection.

## FLUX_Dev_fp8_scaled.safetensors

**Exact public download and quantization recipe unverified.** This existing local file was copied from the instructor’s SwarmUI library. Its recorded SHA256 is preserved in the manifest. The source of the BF16 model is verified above, but that alone does not establish the conversion that produced this FP8 file.

The public [scaled FP8 test model](https://huggingface.co/comfyanonymous/flux_dev_scaled_fp8_test/resolve/594059e8b11432ceaf2d7cf2e95f9eb1c0ecd3ed/flux_dev_fp8_scaled_diffusion_model.safetensors) has SHA256 `358fff9355c962532593898b10436f13e6f9bfb0389f36df03c6e55fe7c9cbfe` and is a different file. It is an optional new experiment, not an equivalent replacement for the measured output, time or memory figures.

For the verified FLUX recipe, start with `warm_flux_bf16.json` and the exact BF16 download above. Consult the [upstream model terms](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/3de623fc3c33e44ffbe2bad470d0f45bccf2eb21/LICENSE.md). Do not relabel timings or generated images from one quantization as results from another.

## FLUX-2-Klein-Base-9b-Quant-FP8.safetensors

- Download: [FLUX-2-Klein-Base-9b-Quant-FP8.safetensors](https://huggingface.co/MonsterMMORPG/Wan_GGUF/resolve/01ae33b2eabe3dd001397bff1bd84c48c64db507/FLUX-2-Klein-Base-9b-Quant-FP8.safetensors)
- Model card and terms: [MonsterMMORPG/Wan_GGUF](https://huggingface.co/MonsterMMORPG/Wan_GGUF); repository label: No separate repository license label.
- Install folder: `ComfyUI/models/diffusion_models`.
- Source SHA256: `bfc6100c448d5bb9024ff8f39076704bf51a53d1be1b9f0ea768495fe13a46d1`; 9,433,179,544 bytes.
- Relationship to the recorded file: Byte-identical download; use the local filename saved in the chosen workflow or change its loader selection.
- Upstream terms: [FLUX Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B/blob/32773329fbe7e81a90ef971740e8ba4b0364ecf3/LICENSE.md). SECourses author quantization. Public ungated file; the repository provides no separate quantization license label. Consult upstream terms.

## qwen3vl_8b.safetensors

- Download: [qwen3vl_8b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/text_encoders/qwen3vl_8b_int8_convrot.safetensors)
- Model card and terms: [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1); repository label: qwen-research.
- Install folder: `ComfyUI/models/text_encoders`.
- Source SHA256: `8bfd0f6e12abf2d2d697ecc888e5e90b0d6741d6708f05799f53afa560452e8f`; 9,350,798,360 bytes.
- Relationship to the recorded file: Same tensor payload verified by reconstruction; local metadata header was repacked. See qwen_tensor_verification.

## qwen_3_8b.safetensors

- Download: [qwen_3_8b_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/3f62d9d8ae1fec33c6e91453d5c712855b096b55/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors)
- Model card and terms: [Comfy-Org/flux2-klein-9B](https://huggingface.co/Comfy-Org/flux2-klein-9B); repository label: flux-non-commercial-license.
- Install folder: `ComfyUI/models/text_encoders`.
- Source SHA256: `abad16806e0cbabc54e0325d6565847443fe396d5f0be38bb3cd3fe75a1201d6`; 8,664,848,742 bytes.
- Relationship to the recorded file: Byte-identical download; use the local filename saved in the chosen workflow or change its loader selection.

## clip_l.safetensors

- Download: [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/6af2a98e3f615bdfa612fbd85da93d1ed5f69ef5/clip_l.safetensors)
- Model card and terms: [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders); repository label: apache-2.0.
- Install folder: `ComfyUI/models/text_encoders`.
- Source SHA256: `660c6f5b1abae9dc498ac2d21e1347d2abdb0cf6c0c0c8576cd796491d9a6cdd`; 246,144,152 bytes.
- Relationship to the recorded file: Byte-identical download; use the local filename saved in the chosen workflow or change its loader selection.

## t5xxl_enconly.safetensors

- Download: [t5xxl_fp8_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/6af2a98e3f615bdfa612fbd85da93d1ed5f69ef5/t5xxl_fp8_e4m3fn.safetensors)
- Model card and terms: [comfyanonymous/flux_text_encoders](https://huggingface.co/comfyanonymous/flux_text_encoders); repository label: apache-2.0.
- Install folder: `ComfyUI/models/text_encoders`.
- Source SHA256: `7d330da4816157540d6bb7838bf63a0f02f573fc48ca4d8de34bb0cbfd514f09`; 4,893,934,904 bytes.
- Relationship to the recorded file: Byte-identical download; use the local filename saved in the chosen workflow or change its loader selection.

## qwen_image_2.1_vae_bf16.safetensors

- Download: [qwen_image_2.1_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/9a44dbdb47cefd046be9c0a13476192f34c8db8e/vae/qwen_image_2.1_vae_bf16.safetensors)
- Model card and terms: [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1); repository label: qwen-research.
- Install folder: `ComfyUI/models/vae`.
- Source SHA256: `bb21f7473051e1ac368515dd3f2e15cd44d7a11748ee8823e1ddca3e4876b7c9`; 675,509,688 bytes.
- Relationship to the recorded file: Same tensor payload verified by reconstruction; local metadata header was repacked. See qwen_tensor_verification.

## flux2-vae.safetensors

- Download: [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/ed33133cd56476eac818c0943b6f9419b3e4a3a1/split_files/vae/flux2-vae.safetensors)
- Model card and terms: [Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev); repository label: flux-1-dev-non-commercial-license.
- Install folder: `ComfyUI/models/vae`.
- Source SHA256: `d64f3a68e1cc4f9f4e29b6e0da38a0204fe9a49f2d4053f0ec1fa1ca02f9c4b5`; 336,213,556 bytes.
- Relationship to the recorded file: Byte-identical download; use the local filename saved in the chosen workflow or change its loader selection.

## Civitai community model and adapter (chapters 14-20)

Both files were downloaded on camera from Civitai with the browser set to ask where to save each file. Civitai downloads need a
signed-in account. Check the page terms before use.

### fasciumklein9b_lastMERGE_fp8.safetensors (fine-tune)

- Page: [FasciumKLEIN9B, version LAST_MERGE](https://civitai.com/models/2387901/fasciumklein9b?modelVersionId=2955596).
  Choose the **fp8 (8-bit, smaller file)** variant in the download box, file id 2835049; the primary file is the larger fp16 variant.
- Install folder: `ComfyUI/models/diffusion_models`. It replaces only the diffusion model of the Klein 9B graph; keep the
  Qwen3 8B text encoder (`flux2` type) and `flux2-vae.safetensors`.
- SHA256 `E4AD926B9CE1CA92749D091F14ECF1A23BB48F4837AA14ACE3B16B60EC23BF8A`; 9,112,692,432 bytes.
- Author recipe from the model description (step-distilled merge): CFG 2.0, 15 steps, Euler Ancestral, 1536x1024. The lecture
  keeps seed 161803 and the product prompt from the guidance chapter.
- Terms: the page links the FLUX.1 [dev] Non-Commercial License; the base model license applies to the merge.

### Aquarelle_IV-8.safetensors (watercolor LoRA)

- Page: [Watercolor painting, version 4](https://civitai.com/models/749060/watercolor-painting?modelVersionId=1782702); version 4
  is the FLUX.1 D version (version 7 targets Z-Image Turbo).
- Install folder: `ComfyUI/models/loras`. Trigger word `AquarelleIV` at the start of the prompt.
- SHA256 `AF3102A51B4854A8EF576A0ADBE68E4F0B21EE9D8560ACA902AD68D35BC4E042`; 19,289,400 bytes.
- The tensor list holds 912 entries, all `lora_unet_*`: it changes only the diffusion model. The lecture uses the model-only
  **Load LoRA** node, so the 0.4 / 0.65 / 0.8 comparison changes model strength only.
- Author notes: weighting around 0.65, 25 steps, `dpmpp_2m` or `heunpp2` with `sgm_uniform`, guidance 3.5. The author's
  examples use the Fluxmania merge; the lecture uses the original FLUX.1 dev (`FLUX_Dev.safetensors`, BF16) with `clip_l`,
  `t5xxl_enconly` and `ae.safetensors` (SHA256 `afc8e28272cd15db3919bacdb6918ce9c1ed22e96cb12c4d5ed0fba823529e38`).
