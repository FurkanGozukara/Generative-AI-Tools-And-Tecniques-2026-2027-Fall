# Model files used in Lecture 2

The shared model configuration from Lecture 1 remains in `G:/educational_videos/ComfyUI_Week01/extra_model_paths.yaml`. Use the corresponding folder on your own machine.

| Component | Shared folder | File |
|---|---|---|
| Diffusion model | `G:/educational_videos/Shared_Models_Week01/models/diffusion_models` | `z_image_turbo_bf16.safetensors` |
| Text encoder | `G:/educational_videos/Shared_Models_Week01/models/text_encoders` | `qwen_3_4b.safetensors` |
| VAE | `G:/educational_videos/Shared_Models_Week01/models/vae` | `ae.safetensors` |

The refresh demonstration copies the existing VAE to `vae/LectureTwo/ae.safetensors` through File Explorer. The original remains in place. Press **R** in the ComfyUI graph, then open the VAE selector: the subfolder appears as part of the model name. Both files contain the same weights; this demonstration tests file discovery, not image quality.

Verified copy: 335,304,388 bytes; SHA-256 `afc8e28272cd15db3919bacdb6918ce9c1ed22e96cb12c4d5ed0fba823529e38`.

The demonstrated runtime is ComfyUI commit `c194dd00cd42aa18d9dbf27d977bf6b85d9ea565`, frontend 1.53.6. Model weights are separate dependencies; workflow JSON does not contain them.
