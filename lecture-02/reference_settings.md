# Lecture 2 baseline

Use the prompt in `reference_prompt.txt` and the model files listed in `model_paths.md`.

| Setting | Value |
|---|---|
| Diffusion model | Z-Image-Turbo BF16 |
| Text encoder | Qwen 3 4B; Load CLIP type `lumina2` |
| VAE | `ae.safetensors`, also discovered as `LectureTwo/ae.safetensors` |
| ModelSamplingAuraFlow | shift `3`, sampling `flow` |
| EmptySD3LatentImage | width `1024`, height `1024`, batch size `1` |
| Seed | `170592213851282` |
| Control after generate | `fixed` |
| Steps | `8` |
| CFG | `1` |
| Sampler | `res_multistep` |
| Scheduler | `simple` |
| Denoise | `1` |
| Negative branch | `ConditioningZeroOut` from the prompt conditioning |

These values reproduce the lesson's starting recipe. Keep the model files, prompt and all other settings fixed when comparing one control. An unchanged graph can reuse cached output; a repeatability test must actually run sampling again.
