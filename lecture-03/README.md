# Lecture 3 — text-to-image experiments

Companion files for the completed 40:42 lecture, including the Civitai fine-tune and watercolor LoRA chapters 14–20.

Download the [companion ZIP](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/raw/refs/heads/main/downloads/Lecture_03_Companion_Files.zip), extract it and open `lecture-03/README.md`. Follow [Lecture 1](../lecture-01/README.md) and [Lecture 2](../lecture-02/README.md) for setup and graph fundamentals. The [chapter list](chapters.txt), [commands and shortcuts](commands_and_shortcuts.md) and [video description](youtube_description.txt) follow the completed lecture.

Open an ordinary JSON file from [workflows/](workflows/) using ComfyUI **File → Open**. The 22 editable graphs preserve the demonstrated prompts, seeds, settings and connections. Install the matching model components before running, then refresh model definitions. Keep each seed fixed for comparisons and generate your own outputs.

## Experiments

| Workflow | Purpose | Variables to preserve |
|---|---|---|
| `z_vague`, `z_concrete` | Replace a vague request with a concrete visual brief | Seed 314159, model, size and sampling |
| `z_layout` | Add one instruction placing the funicular in the lower half | Same seed and complete original prompt |
| `z_seed2_original`, `z_seed2_layout` | Repeat that prompt comparison at seed 271828 | The two members of each pair share a seed |
| `z_seed3_original`, `z_seed3_layout` | Repeat at seed 161803 | Treat three pairs as examples, not a universal guarantee |
| `qwen_typography` | Request the title `HILL AND SEA` and exact line `Tickets $12.99!` | Qwen-specific encoder, VAE and prompt node |
| `warm_klein_cfg5`, `warm_klein_cfg1` | Compare conventional CFG 5 versus 1 on Klein **Base** | Seed 161803, 20 steps, Euler, dimensions and empty negative prompt |
| `warm_flux_bf16`, `warm_flux_fp8` | Compare BF16 and scaled FP8 diffusion weights | Seed 271828, both text encoders, VAE, prompt and sampling |
| `flux_water_bypass` | Record FLUX.1 Dev's watercolor-style baseline | No watercolor adapter is loaded in this workflow |
| `Fascium_fine_tune_teapot` | Run the community fine-tune with its author recipe | Klein 9B encoder and VAE; CFG 2, 15 steps, euler_ancestral; seed 161803 |
| `Watercolor_bypass`, `Watercolor_LoRA_040`, `_065`, `_080` | Compare the adapter bypassed and at three model strengths | Prompt with `AquarelleIV`, seed 271828, 25 steps, FluxGuidance 3.5; only the strength changes |

The Qwen result spells both requested lines correctly. Editable, guaranteed text remains a separate layout requirement; this example is not evidence of a spelling failure. The lower-half instruction moved the funicular lower in all three recorded Z-Image pairs, while other details also changed.

## Model components

The filenames below are the selections saved in these workflows. A matching family alone does not establish the same precision, revision or sampling recipe. [Model sources and download mapping](model_sources.md) supplies pinned download links, access checks and license references. `model_manifest.json` records inspected local hashes and verified Qwen tensor equivalence. The local FLUX FP8 file has no verified matching public source; use the documented BF16 route when reproducing the recipe and treat another FP8 variant as a new experiment.

| Family | Diffusion model | Text encoder(s) | VAE |
|---|---|---|---|
| Z-Image Turbo | `z_image_turbo_bf16.safetensors` | `qwen_3_4b.safetensors` (`lumina2`) | `ae.safetensors` |
| Qwen-Image 2.1 | `qwen_image_2.1_int8_convrot.safetensors` | `qwen3vl_8b_int8_convrot.safetensors` (`qwen_image`) | `qwen_image_2.1_vae_bf16.safetensors` |
| FLUX.2 Klein Base 9B | `FLUX-2-Klein-Base-9b-Quant-FP8.safetensors` | `qwen_3_8b_fp8mixed.safetensors` (`flux2`) | `flux2-vae.safetensors` |
| FLUX.1 Dev | `FLUX_Dev.safetensors` or `FLUX_Dev_fp8_scaled.safetensors` | `clip_l.safetensors` and `t5xxl_enconly.safetensors` (`flux`) | `ae.safetensors` |

Model placement uses ComfyUI's `models/diffusion_models`, `models/text_encoders` and `models/vae` folders. Filename aliases used for the Qwen encoders point to the same verified model payloads. No model weights are included here. Check the source license for each model and its intended use.

Qwen sources: [official Comfy-Org files](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/tree/main). Klein components and the distinction between base and distilled variants: [official ComfyUI guide](https://docs.comfy.org/tutorials/flux/flux-2-klein).

## Measured comparison

These warm runs used one RTX 5090. Loaders and text encoders were cached; the sampler executed. Times and sampled device-memory peaks describe these particular runs and include the effects of this installation. They are not minimum VRAM requirements or general benchmarks.

| Run | Sampler time | End-to-end time | Sampled device-memory peak |
|---|---:|---:|---:|
| Klein Base, CFG 5 | 24.000 s | 24.672 s | 20,885 MiB |
| Klein Base, CFG 1 | 11.969 s | 12.531 s | 21,173 MiB |
| FLUX.1 Dev, BF16 | 16.593 s | 17.187 s | 29,749 MiB |
| FLUX.1 Dev, scaled FP8 | 16.938 s | 17.594 s | 16,469 MiB |

At the measured seed, CFG 5 followed the teapot, cup and wooden-table brief more closely. CFG 1 sampled faster but introduced unwanted changes. Scaled FP8 reduced measured device memory and was slightly slower here; its image details differed from BF16. Both FLUX runs kept the same CLIP-L and FP8 T5 text encoders. Their KSampler CFG stays at 1 while the separate FluxGuidance node is 3.5. The 25-step `dpmpp_2m` / `sgm_uniform` combination is the selected lesson recipe, not a claim about an official default.

The reference installation used ComfyUI commit `3b4c0b0e457cf0a51cf3038e0a6750d8f96ce251` and frontend 1.53.6. Hardware, software, model revision or precision changes can change outputs even with a fixed seed.


## Exact recorded checkpoints

`recorded_workflows.json` identifies the nine JSON checkpoints opened, exported or embedded in the recorded outputs in the retained recording. The reference workflows retain local FLUX/Klein diffusion filenames; only the Qwen and Klein encoder aliases were normalized to their download names. Follow `model_sources.md` and choose the actual filename in each loader. The recorded Klein encoder name `qwen_3_8b.safetensors` is byte-identical to the official `qwen_3_8b_fp8mixed.safetensors` (SHA256 in `model_manifest.json`). Select the matching local filename if yours differs. Qwen aliases have verified identical tensor payloads; metadata headers differ from the official files.


## Civitai chapters (14-20)

- **Fine-tune:** FasciumKLEIN9B `LAST_MERGE`, fp8 file, in `models/diffusion_models`, used on the Klein 9B graph with the author
  recipe (CFG 2, 15 steps, euler_ancestral). Open `workflows/Fascium_fine_tune_teapot.json` to run it.
- **Adapter:** Aquarelle_IV-8 (version 4, FLUX.1 D) in `models/loras`, connected with the model-only **Load LoRA** node
  between the diffusion model and the sampler. The `Watercolor_bypass` and `Watercolor_LoRA_040`, `_065`, `_080` workflows reproduce the four recipes. In the recorded result at 0.8 a
  handwritten signature appears in the lower right; for this brief 0.65 keeps clear watercolor washes without it.
- The workflows are the exact recipes the recorded runs executed (extracted from each PNG's embedded metadata).
  Community weights are not included; see `model_sources.md` for pages, files, hashes and terms.

[SHA256SUMS.txt](SHA256SUMS.txt) lists the companion-file checksums. Model weights are separate publisher downloads.
