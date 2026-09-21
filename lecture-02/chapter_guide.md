# Lecture 2 chapter guide

| Time | Topic | Materials |
|---|---|---|
| 00:00 | From the first image to its workflow | [starting_workflow.png](starting_workflow.png) |
| 01:06 | Update ComfyUI and its matching Python dependencies | [update_commands.txt](update_commands.txt) |
| 03:53 | Open the packaged workflow and trace its stages | [starting_workflow.png](starting_workflow.png) |
| 05:21 | Refresh model files without restarting the server | [model_paths.md](model_paths.md) |
| 06:35 | Load the three models and connect their roles | [lecture02_workflow.json](lecture02_workflow.json) |
| 08:41 | Turn the prompt into conditioning for the model | [lecture02_workflow.json](lecture02_workflow.json) |
| 10:00 | Connect the latent and choose the sampling settings | [lecture02_workflow.json](lecture02_workflow.json) |
| 12:50 | Decode the sampled latent and save the image | [lecture02_workflow.json](lecture02_workflow.json) |
| 14:21 | Run the complete graph and inspect the result | [lecture02_result.png](lecture02_result.png) |
| 15:40 | Change the prompt and watch cached stages | [reference_prompt.txt](reference_prompt.txt) |
| 16:44 | Compare resolution and the actual computation cost | [generation_cost.md](generation_cost.md) |
| 20:07 | Test fixed seeds and explore with random seeds | [reference_settings.md](reference_settings.md) |
| 23:00 | Compare sampling steps on the Turbo model | [reference_settings.md](reference_settings.md) |
| 25:21 | Inspect guidance changes on this distilled model | [reference_settings.md](reference_settings.md) |
| 27:33 | Test the negative branch at guidance one | [reference_settings.md](reference_settings.md) |
| 29:19 | Change one variable and explain the difference | [README.md](README.md) |
| 30:41 | Recover the workflow from PNG and export JSON | [lecture02_result.png](lecture02_result.png) |
| 33:02 | Follow the restored graph to the saved image | [lecture02_workflow.json](lecture02_workflow.json) |
