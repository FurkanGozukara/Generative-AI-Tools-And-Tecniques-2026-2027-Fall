# Save and recover ComfyUI settings

After generating an image, the displayed seed may change for the next run. Restore the submitted seed before saving a workflow JSON. Use fixed seed control when your sampler exposes it.

Keep original generated PNG files. In ComfyUI, press Ctrl+O and select an original PNG to load its embedded workflow. Dragging the PNG onto the canvas is another supported route. Check the prompt, models, dimensions and seed after loading. Converted images and copies shared through some services may lose metadata.

The included z-image-turbo_00002_.png loads seed 170592213851282, width and height 1024, eight steps, z_image_turbo_bf16.safetensors, qwen_3_4b.safetensors and ae.safetensors. The saved Week01_LocalModels_Proof.json uses the same seed. Keep the same software and model versions when reproducing results.
