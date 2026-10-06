# Commands and shortcuts used in Lecture 3

These timings refer to the complete 40:42 lecture.

## Update (01:01)

Open your ComfyUI installation folder in File Explorer. Open Command Prompt in that folder, then run each command separately:

```bat
venv\Scripts\activate
git pull --ff-only
python -m pip install -r requirements.txt
```

The recording shows activation and completed commands, followed by a browser refresh. The backend was not restarted in this recording. After `git pull --ff-only` and `python -m pip install -r requirements.txt`, restart ComfyUI using the startup route from Lecture 2, then refresh the browser. A browser refresh alone does not load updated backend code. The demonstrations here ran on the already-open server at commit `3b4c0b0e457cf0a51cf3038e0a6750d8f96ce251`, frontend 1.53.6. An exact post-install package freeze was not captured, so this is a source/version record rather than a complete environment lock.

## Prompt and tokenizer (02:30–05:31)

The example sentence is `A copper robot carries a blue umbrella.` The displayed tokenizer mode is `GPT-5.x & O1/3`; the unedited sentence shows 8 tokens and 39 characters. These values refer to that visible web-tokenizer example only. The official web tokenizer is illustrative: its count and pieces do not establish how an image model tokenizes the same text. Inspect the matching encoder and conditioning connection in the graph.

## Loading and saving

- Ctrl+O opens a workflow JSON. Paste the complete path in File name, hold to inspect it, then choose Open.
- The graph menu's Export command writes an ordinary workflow JSON. Save it in your lesson folder.
- Use the plus button for a blank workflow, then Ctrl+O to reopen the saved JSON and inspect the model, prompt, seed and connections.
- JSON contains the recipe, not the model weights. Preserve exact source links, filenames, revisions, hashes, prompt, seed, dimensions, sampler, scheduler and guidance with the recipe.

The exact exported file is `workflows/Lecture03_FLUX_product_workflow.json`. Save your exported graph in a lesson folder of your choice.

## Civitai downloads (chapters 14-17)

- Find a site: search Google for `civitai` and open the official address `civitai.com`, or type the address.
- Filter searches by **Base Model** (Flux.2 Klein 9B for the fine-tune, Flux.1 D for the adapter) and by model type (LoRA).
- With the browser set to ask where to save each file, paste the complete destination in the Save As **File name** field:
  - `...\ComfyUI\models\diffusion_models\fasciumklein9b_lastMERGE_fp8.safetensors`
  - `...\ComfyUI\models\loras\Aquarelle_IV-8.safetensors`
  Otherwise move the file from Downloads into that folder afterwards.
- The browser's download button lists the download; **Show in folder** opens it in File Explorer.

## ComfyUI graph editing (chapters 15-20)

- **R** refreshes the model lists after new files arrive while ComfyUI is running.
- Double-click empty canvas to search for a node (for example **Load LoRA**); the new node follows the pointer until a click places it.
- Drag from an output dot to an input dot to connect; a new connection into an input replaces the old one.
- Select a node and press **Ctrl+B** to bypass it (purple); press Ctrl+B again to enable it.
- Double-click a number or text widget to type an exact value, for example strength `0.65` or a filename prefix.
