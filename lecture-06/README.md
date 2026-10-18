# Lecture 6 — Structure, composition and ComfyUI in Colab

**Week 6 learner materials are available. The video link will be added after publication.**

[Download the complete companion ZIP](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/raw/refs/heads/main/downloads/Lecture_06_Companion_Files.zip) · [Open the latest notebook in Colab](https://colab.research.google.com/github/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/blob/main/lecture-06/colab/Qwen-Image-2.1_ComfyUI_Colab.ipynb) · [Download notebook](colab/Qwen-Image-2.1_ComfyUI_Colab.ipynb)

The 69:13 lecture covers the complete Colab T4 route, A100 differences, depth/edge/pose control, combined conditioning and independent masked composition. Extract the ZIP and open `lecture-06/README.md`. The same latest notebook is included here and in the ZIP; it has no saved runtime outputs. In Colab, save your own copy before editing. Follow [the Colab guide](colab/README.md) for the demonstrated upload route and runtime steps.

The [80 chapters](chapters.txt), [prepared video description](youtube_description.txt) and [prepared title](youtube_title.txt) are included. Model weights and the video are separate. Check individual file hashes in [SHA256SUMS.txt](SHA256SUMS.txt).

Start with [the Colab guide](colab/README.md) for the cloud route, or use your working local ComfyUI installation from earlier lectures. The recorded local application was ComfyUI 0.41.0 on October 18, 2026. These files preserve that demonstration; newer software may change menus or results.

## Open a recorded workflow

1. Extract this whole ZIP. In ComfyUI, use the normal workflow Open command and choose a `.json` file from `recorded_workflows/`. The paired `.api.json` files are API prompt dictionaries, not the normal canvas-opening route.
2. Install the graph's models using [Model Download Links](workflows/Model_Download_Links.html) and the additional dependencies below. Refresh the model lists and inspect every loader.
3. Copy the supplied `inputs/` files into your ComfyUI input directory, or upload and select them in the matching Load Image nodes. Keep the filenames. For the demonstrated video upload, use `street_walk_5s.mp4` in a compatible video loader; it is an input demonstration, not a video-generation workflow.
4. Read the prompt, seed, dimensions and controls before running. Compare against the original files in `recorded_results/`. Change one variable at a time and save your graph with the result.

`recorded_workflows/index.json` maps 31 successful runs to their exact graph, API dictionary and 37 output files. The original output bytes are unchanged. Some entries are intermediate experiments with visible limitations; they are included to explain the decisions, not presented as ideal results. `qwen21_background_clean` was prepared before the composition demonstration. Other recorded outputs retain their observed status.

## Useful starting points

| Goal | Workflow in recorded_workflows/ |
|---|---|
| Colab T4 workshop image | `colab_t4_workshop_first.json` |
| Inspect depth | `depth_map_first.json` |
| Compare no control with depth | `qwen_baseline_first.json`, `qwen_depth_0p8_first.json` |
| Compare strength | `qwen_strength_0p5_first.json`, `qwen_depth_0p8_first.json`, `qwen_strength_1p0_first.json` |
| Compare when control stops | `qwen_end_0p3_first.json`, `qwen_end_0p65_first.json` |
| Extract edges, line detail and pose | `canny_map_first.json`, `anyline_map_first.json`, `pose_map_first.json` |
| Inspect threshold tradeoffs | `canny_threshold_low.json`, `canny_threshold_high.json` |
| Combine controls | `qwen_chain_strong.json`, `qwen_chain_balanced.json` |
| Prompt the whole scene | `qwen21_spatial_first.json` |
| Generate and select separate subjects | `qwen21_explorer.json`, `qwen21_robot.json`, `explorer_mask.json`, `robot_mask.json` |
| Continue the final editable composition | `composition_contact_final.json` |

The friendly names in `workflows/` are the saved graphs shown near the end of the lecture. The recorded-run index is the detailed source for comparisons. `Comparison_Settings.json` preserves the comparison values. Image metadata may also contain the graph.

## Dependencies and model families

The depth/edge/pose control experiments use **original Qwen-Image + InstantX Union ControlNet**, with the matching original text encoder and VAE. The Colab starter and separate subject generation use **Qwen-Image 2.1**, its own encoder and its own VAE. Do not substitute the 2.1 model into the original InstantX graph.

| Used component | Filename | Standard folder | Official files |
|---|---|---|---|
| Qwen-Image 2.1 diffusion | `qwen_image_2.1_int8_convrot.safetensors` | `models/diffusion_models/` | [Comfy-Org Qwen-Image 2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/tree/main/diffusion_models) |
| T4 text encoder | `qwen3vl_8b_w4a8.safetensors` | `models/text_encoders/` | [Text encoders](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/tree/main/text_encoders) |
| Local 2.1 text encoder | `qwen3vl_8b_int8_convrot.safetensors` | `models/text_encoders/` | [Text encoders](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/tree/main/text_encoders) |
| Qwen-Image 2.1 VAE | `qwen_image_2.1_vae_bf16.safetensors` | `models/vae/` | [VAEs](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/tree/main/vae) |
| Pose extraction | `sdpose_wholebody_fp16.safetensors` | `models/checkpoints/` | [SDPose](https://huggingface.co/Comfy-Org/SDPose/tree/main/checkpoints) |
| Subject segmentation | `sam3.1_multiplex_fp16.safetensors` | `models/checkpoints/` | [SAM3.1](https://huggingface.co/Comfy-Org/sam3.1/tree/main/checkpoints) |

The original Qwen model, InstantX control file, original encoder/VAE and Depth Anything 3 paths are listed in the linked HTML guide. The saved pose graph uses SDPose directly; it does not require the separate optional RT-DETR detector. AnyLine needs [ComfyUI ControlNet Auxiliary Preprocessors](https://github.com/Fannovel16/comfyui_controlnet_aux); install it through ComfyUI-Manager, follow its dependency instructions and restart. Its first use can download preprocessor weights. The recorded depth, pose and SAM3 nodes are core nodes in the recorded ComfyUI build. `recorded_workflows/index.json` lists all used node classes.

## What to inspect

Depth retains spatial layers; edges retain boundaries; pose retains joints. The saved comparisons demonstrate different constraints, not a universal quality ranking. Stronger control can impose unwanted structure. Inspect the source map, resize/crop and conditioning schedule before increasing strength. Combined strengths do not have to sum to 1.

The final composition lets the explorer and robot move independently through separate masks and placements. Inspect mask polarity, detached specks, padding, contact and the revealed background. The final image still has lighting and integration limitations discussed in the lecture. Keep the intermediate images when comparing the repair steps.

The Colab notebook saves its document separately from its temporary runtime. Export results, inputs you need and workflow JSONs before terminating or changing runtimes. The included notebook is the canonical copy whose code cells were checked against the downloaded demonstration copy. Use the detailed guide for setup, model downloads, cloudflared access, individual downloads, ZIP export and termination.

Model weights are not bundled. Follow the linked owners' download and license terms. GPU allocation and free-runtime eligibility can change; the observed T4 session is not a promise of future availability.
