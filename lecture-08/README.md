# Lecture 8 — Workflow Engineering, Automation, APIs and Custom Nodes

[Download the complete companion ZIP](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/raw/refs/heads/main/downloads/Lecture_08_Companion_Files.zip) · [Full course playlist](https://www.youtube.com/playlist?list=PLUMEJUep1hiI) · [Course overview](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall)

Turn a crowded graph into a reusable delivery workflow, expose its controls as an app, and submit jobs from Python. Then inspect custom-node behavior and recover through an isolated installation. These are the files used in the recorded lecture, including the original images, API clients and environment records. The Lecture 8 video link will be added when it is public.

Extract the ZIP and open `lecture-08/README.md`. Keep this companion folder separate from your ComfyUI installation. The command examples use Windows Command Prompt. The API client scripts use Python's standard library and can inspect the export without a running server.

## Choose a starting point

| File | What you can do with it |
|---|---|
| [Crowded starting graph](workflows/seven_weeks_everything.json) | Follow the organization exercise, compare branches, and practice partial execution, bypass and mute. Its old notes and unused branches are intentional examples for cleanup. |
| [Delivery workflow](workflows/watchmaker_delivery.json) | Open the smaller Z-Image Turbo workflow. Its upscaling and resize chain is already a subgraph with exposed model, width and height controls. |
| [Exported app](exports/watchmaker%20app.json) | Import the saved app configuration and inspect its prompt input and image output. Switch to the node graph to follow the underlying connections. |
| [API export](api/watchmaker_API.json) | Inspect the executable node dictionary or submit it with the supplied Python client. Subgraph nodes have flattened identifiers such as `11:14`. |
| [Python client guide](api/README.md) | Inspect a graph, print a dry-run request, submit one job, or queue three prompts and attempt to cancel the final waiting job. |
| [Commands](commands.md) | Follow the API, source-inspection, dependency-record and isolation examples. |
| [Models and compatibility](MODELS.md) | Match model folders and the recorded ComfyUI state. |
| [Environment records](environment/README.md) | Compare the actual core commit, installed dependency list and Manager snapshot. |
| [Original results](results/README.md) | Inspect the app, API and queue outputs without rerunning inference. |

## Open a workflow

1. Start your course ComfyUI installation and open `workflows/watchmaker_delivery.json` through its workflow open/import control.
2. Match the four model selections in [MODELS.md](MODELS.md). The delivery workflow uses `LectureTwo\ae.safetensors`; select `ae.safetensors` instead if your VAE is directly in `models/vae/`.
3. Inspect the exposed prompt and upscale/resize controls. The recorded generation starts at 1024 × 1024 and saves a 2048 × 2048 result, with seed 2026, eight steps and CFG 1.
4. For the larger organization exercise, copy the two files in `inputs/` to ComfyUI's input folder and open `workflows/seven_weeks_everything.json`. Its `Load Image` nodes expect the supplied filenames. Other branches reuse models and node packs from the earlier lectures; see [MODELS.md](MODELS.md).

The delivery and API examples use core nodes. The crowded exercise also includes custom nodes from the earlier course. A missing-node prompt in that exercise does not mean the smaller delivery graph needs every pack. Model weights, software installations and GPU capacity are separate from the companion.

## Work through the lecture

| Time | Topic | Companion material |
|---|---|---|
| 0:00 | Why organize the accumulated graph? | `workflows/seven_weeks_everything.json` |
| 0:47 | Update and start ComfyUI | `environment/` records the version used |
| 1:33 | Four questions about the graph | The starting graph and its grouped branches |
| 2:27 | Create and expose a subgraph | `workflows/watchmaker_delivery.json` |
| 4:28 | Partial execution, bypass, mute and caching | The watercolor branch in the starting graph |
| 5:52 | Create an app form | `exports/watchmaker app.json` |
| 8:22 | Export and read API format | `api/watchmaker_API.json` |
| 9:34 | Python dry run and one real job | `api/inspect_api_workflow.py`, `api/submit_api_workflow.py` |
| 13:43 | Queue three prompts and cancel one | `api/queue_api_prompts.py`, `api/prompts.txt`, `results/queue_outcomes.json` |
| 15:35 | Inspect live schemas and SDK versions | `commands.md` |
| 17:25 | Inspect custom-node behavior | `commands.md`, `environment/L08_snapshot.json` |
| 22:04 | Read errors and isolate a node pack | `launchers/`, `commands.md` |
| 25:04 | Recap | The delivery workflow and [chapter list](chapters.txt) |

## Continue from a successful request

The API export's prompt is node `5`, input `text`; its saver is node `10`, input `filename_prefix`. Inspect these before adapting another graph because identifiers can change. A submission returns a job ID. The client then polls the completed history and downloads output files into a new run folder.

The recorded queue completed jobs 1 and 2 and removed job 3 while it was waiting. Your cancellation depends on when the server starts the job; it cannot remove a job that has already begun through the waiting-queue operation. After a timeout, inspect the saved job ID before submitting again.

[Chapters](chapters.txt) · [File checksums](SHA256SUMS.txt) · [Previous lecture](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/tree/main/lecture-07)
