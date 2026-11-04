# Lecture 8 — Python API examples

Keep the three scripts, `watchmaker_API.json` and `prompts.txt` together. Activate your ComfyUI Python environment, then open a Command Prompt in this `api` folder. These scripts use only the standard library.

The supplied export has prompt node `5` and saver node `10`. Its model filenames must match your installation; see [the model guide](../MODELS.md). The lecture uses port `8189`. Replace that address with your own local server's address if it uses another port.

## Inspect without running inference

```cmd
python inspect_api_workflow.py watchmaker_API.json
python submit_api_workflow.py watchmaker_API.json --prompt-node 5 --text "A lighthouse keeper polishing a brass lamp in a lantern room, evening light, photorealistic" --server http://127.0.0.1:8189 --dry-run
```

The inspector checks the node dictionary and its links. The dry run changes the selected literal prompt and prints the request without contacting a server or creating output files. Neither operation establishes that your installed nodes and models can execute the graph.

## Submit one job

Start your prepared local ComfyUI server, then run:

```cmd
python submit_api_workflow.py watchmaker_API.json --prompt-node 5 --text "A lighthouse keeper polishing a brass lamp in a lantern room, evening light, photorealistic" --server http://127.0.0.1:8189
```

Each run creates a separate folder under `course_api_outputs/`, saving the exact request, submission, completed history and downloaded files. Non-file outputs remain in the history. If a connection fails or polling times out, use the saved job ID to inspect the existing job before submitting again. The client does not automatically resubmit or cancel it.

## Queue several prompts

```cmd
python queue_api_prompts.py watchmaker_API.json --prompt-node 5 --save-node 10 --prompts prompts.txt --server http://127.0.0.1:8189 --cancel-last
```

The script gives each output a distinct prefix, submits the prompts, and checks whether the last job is still waiting before removing it from the queue. It saves the requests, histories, images and a summary. The recorded run's [outcomes](../results/queue_outcomes.json) are completed, completed and cancelled. A faster or differently loaded server may begin the last job before cancellation.

## Adapt another graph

Export it using ComfyUI's **Export (API)** control, retain the ordinary editor JSON as well, then inspect the actual node identifiers. Select an existing literal string input; a linked input needs its source string node instead. The seed and other settings remain those of the exported graph.

The examples submit local workflows and download their returned files. Prepare models, input files and custom nodes separately. Keep a teaching server local; a remote deployment needs its own authentication and access configuration.

Protocol references: [server routes](https://docs.comfy.org/development/comfyui-server/comms_routes), [server messages](https://docs.comfy.org/development/comfyui-server/comms_messages).
