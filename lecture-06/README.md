# Lecture 6 — Structure, composition and ComfyUI in Colab

**Generative AI Full Course - Lecture 6: Stack Depth + Pose for Structural Control**

▶️ **[Watch Lecture 6](https://www.youtube.com/watch?v=h4-F5Jx-HQo)** · 📺 **[Full course playlist](https://www.youtube.com/playlist?list=PLUMEJUep1hiI)**

[Download the complete companion ZIP](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/raw/refs/heads/main/downloads/Lecture_06_Companion_Files.zip) · [Open the latest notebook in Colab](https://colab.research.google.com/github/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/blob/main/lecture-06/colab/Qwen-Image-2.1_ComfyUI_Colab.ipynb) · [Download notebook](colab/Qwen-Image-2.1_ComfyUI_Colab.ipynb)

The 69:13 lecture covers the complete Colab T4 route, A100 differences, depth/edge/pose control, combined conditioning and independent masked composition. Extract the ZIP and open `lecture-06/README.md`. The same latest notebook is included here and in the ZIP; it has no saved runtime outputs. In Colab, save your own copy before editing. Follow [the Colab guide](colab/README.md) for the demonstrated upload route and runtime steps.

The [80 chapters](chapters.txt), [video description](youtube_description.txt) and [video title](youtube_title.txt) are included. Model weights and the video are separate. Check individual file hashes in [SHA256SUMS.txt](SHA256SUMS.txt).

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

Download model weights from the linked publishers. GPU allocation and free-runtime eligibility can change; the observed T4 session is not a promise of future availability.


## Watch by chapter

| Time | Chapter |
|---|---|
| [0:00](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=0s) | ComfyUI in Colab and structural control |
| [0:58](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=58s) | Upload, rename and save the notebook |
| [1:30](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=90s) | Notebook saving versus temporary runtime files |
| [2:30](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=150s) | Select a GPU and connect the runtime |
| [3:03](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=183s) | Notebook forms, code and cell controls |
| [3:44](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=224s) | Install ComfyUI and inspect detected hardware |
| [4:19](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=259s) | Match diffusion model, encoder and VAE |
| [4:49](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=289s) | Download models and inspect automatic choices |
| [6:05](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=365s) | System RAM and GPU memory are separate |
| [6:20](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=380s) | Choose direct model links and destination folders |
| [7:02](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=422s) | Run an optional download and inspect its file |
| [7:26](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=446s) | Start ComfyUI and open the temporary URL |
| [8:05](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=485s) | Open the matched starter workflow and prompt |
| [8:32](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=512s) | Generate remotely and watch the live progress |
| [9:05](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=545s) | Inspect and download the completed image |
| [9:44](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=584s) | Save and export the editable workflow JSON |
| [10:16](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=616s) | Upload a reference image to the runtime |
| [10:59](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=659s) | Upload a video into the input folder |
| [11:17](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=677s) | Refresh the loader and inspect video playback |
| [11:39](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=699s) | Reopen a workflow and reconnect its inputs |
| [11:57](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=717s) | Stop the server before exporting a folder |
| [12:13](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=733s) | Choose output subfolders and include inputs |
| [12:46](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=766s) | Create and download the complete result ZIP |
| [13:18](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=798s) | Inspect ZIP outputs, graphs and the manifest |
| [14:20](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=860s) | Restart ComfyUI on the same runtime |
| [15:35](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=935s) | Understand reset, disconnect and file persistence |
| [16:03](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=963s) | Select and verify a paid A100 allocation |
| [16:46](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1006s) | Compare automatic model choices across runtimes |
| [17:02](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1022s) | Terminate the session and verify it ends |
| [17:40](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1060s) | Update the local environment and restart ComfyUI |
| [18:51](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1131s) | From references and masks to structural control |
| [19:24](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1164s) | Trace ControlNet through the conditioning path |
| [19:41](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1181s) | Distinguish model patches, LoRAs and references |
| [20:48](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1248s) | Match original Qwen with InstantX Union |
| [21:05](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1265s) | Download matched model and control weights |
| [21:44](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1304s) | Install Depth Anything 3 and refresh loaders |
| [22:35](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1355s) | Fix seed, steps and sampling conditions |
| [23:17](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1397s) | Inspect the source and align its working size |
| [24:05](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1445s) | Connect Depth Anything 3 and inference |
| [25:12](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1512s) | Render grayscale depth before connecting generation |
| [25:54](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1554s) | Inspect spatial layers and save the map |
| [26:40](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1600s) | Load the compatible Qwen model family |
| [26:56](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1616s) | Write the prompt and conditioning branches |
| [28:02](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1682s) | Connect the union loader and apply node |
| [29:20](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1760s) | Connect the matching VAE and output path |
| [30:20](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1820s) | Generate the baseline without structural control |
| [31:07](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1867s) | Restore depth control with unchanged settings |
| [31:33](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1893s) | Compare source, depth and both generated images |
| [32:31](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=1951s) | Understand the VAE input and diagnose failures |
| [33:45](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2025s) | Compare control strengths 0.5, 0.8 and 1 |
| [35:05](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2105s) | Inspect geometry and prompt adherence separately |
| [36:03](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2163s) | Separate control strength from start and end |
| [36:47](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2207s) | Generate end 0.3 and end 0.65 |
| [37:51](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2271s) | Compare early release with full-schedule control |
| [38:49](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2329s) | Choose edges, line detail, depth or pose |
| [39:50](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2390s) | Install the auxiliary package and run AnyLine |
| [41:22](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2482s) | Set up SDPose and choose joint drawing |
| [43:37](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2617s) | Inspect all four maps at the same scale |
| [43:57](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2637s) | Generate with each structural map type |
| [46:12](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2772s) | Compare the results against their actual maps |
| [47:13](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2833s) | Enlarge Canny and adjust its thresholds |
| [48:24](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2904s) | Compare detailed and simplified edge maps |
| [48:59](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2939s) | Inspect pose joints against the source photograph |
| [49:57](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=2997s) | Chain depth and pose conditioning correctly |
| [50:56](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3056s) | Test both controls at full strength |
| [51:40](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3100s) | Balance depth 0.5 with pose 0.6 |
| [52:23](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3143s) | Compare results and diagnose competing constraints |
| [53:45](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3225s) | Prompt an explorer and robot in one scene |
| [54:40](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3280s) | Inspect placement, attributes and editability |
| [55:50](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3350s) | Generate separate subjects and inspect their quality |
| [57:16](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3436s) | Extract masks and place the subjects independently |
| [59:13](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3553s) | Match scale, perspective and contact points |
| [1:01:14](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3674s) | Repair the visible contact-layer rectangle |
| [1:01:29](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3689s) | Pad the soft mask with empty space |
| [1:02:35](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3755s) | Match image and mask sizes before repositioning |
| [1:03:56](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3836s) | Move the robot while keeping the explorer fixed |
| [1:04:41](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3881s) | Repair the boot contact and inspect grounding |
| [1:05:25](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3925s) | Compare single generation with editable composition |
| [1:06:09](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=3969s) | Export subjects, masks and the final graph |
| [1:07:11](https://www.youtube.com/watch?v=h4-F5Jx-HQo&t=4031s) | Reopen saved projects and use the learner files |
