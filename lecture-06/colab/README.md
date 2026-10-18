# Lecture 6: ComfyUI in Google Colab

[Open this notebook in Colab](https://colab.research.google.com/github/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/blob/main/lecture-06/colab/Qwen-Image-2.1_ComfyUI_Colab.ipynb) · [Download the notebook](Qwen-Image-2.1_ComfyUI_Colab.ipynb)

Download `Qwen-Image-2.1_ComfyUI_Colab.ipynb`, open [Google Colab](https://colab.research.google.com/), and choose **Upload notebook → Browse**. Rename your Drive copy. The notebook document and the temporary runtime are separate: saving the document does not save the runtime's model weights, inputs or outputs.

## Start a runtime

1. Select **Runtime → Change runtime type**, choose an available GPU, and connect. Check the actual GPU in step 1's output. GPU memory and system RAM are separate limits.
2. Run **1 · Install ComfyUI + ComfyUI-Manager**. Keep the default latest stable release unless you are deliberately reproducing a saved environment.
3. Run **2 · Download required models**. Auto selects from the detected hardware; inspect the printed filenames. The starter uses Qwen-Image 2.1. The original Qwen-Image InstantX ControlNet example later in Lecture 6 needs its own matched base model and control file.
4. Step 3 is optional. Keep tokens empty for public files. Use a direct file link, choose the destination by the loader's requirements, and leave unwanted link fields empty. A `.safetensors` extension alone does not tell you which loader can use it.
5. Run **4 · Start ComfyUI**. Keep this cell running, open its printed cloudflared URL, and use the provided starter workflow in ComfyUI. Change the prompt and generate there. A new start may print a different URL.

Use the run button beside one cell at a time. The square interrupts a running cell. **Run all** also includes optional downloads and waits at the long-running server cell. After changing a form field, click away, inspect its value and save the notebook.

## Bring your workflow and media

Open a saved workflow JSON through ComfyUI's normal Open route. The graph contains settings and connections; it does not bundle models, custom nodes or input media. Install its actual dependencies and reconnect the intended filenames.

For an image, use **Load Image → choose file to upload**. For video or several files, use Colab's Files panel and upload into `/content/ComfyUI/input`, then select the filename in a compatible loader. A path on your local Windows drive does not point to a file on the remote Linux machine.

If a newly uploaded file is absent from the loader list, save the workflow and reload the ComfyUI page, then check the filename and preview. This recovered the video list in the recorded T4 session without uploading the file again.

An initial image, reference image, reference video or control map is a role assigned by the workflow. Uploading a file does not turn a text-to-image graph into an image-editing or video graph. Check the model and loader before running it. Colab's temporary tunnel serves this runtime; keep private credentials out of screenshots and saved public workflows.

## Save results before leaving

- **One image:** use the output image's save/download control in ComfyUI, then open the downloaded file locally.
- **Workflow:** save it in ComfyUI's Workflows panel and export a local JSON copy. A saved image may also carry workflow metadata, but a separately exported JSON is useful for sharing.
- **Whole result folder:** save the workflow first, stop step 4, and wait for its cleanup message. Run step 5. Leave the subfolder empty for all outputs or enter a relative output subfolder. Inputs are optional; model weights are excluded. In Colab Files, expand `/content/exports`, open the printed ZIP's menu and choose **Download**. Complete the browser's Save As dialog if it appears. Open the ZIP locally and inspect its output, workflow and manifest entries.

| Action | What to expect |
|---|---|
| Close and reopen the ComfyUI tab while its server cell is running | Reopen the active URL; the runtime may still be alive. |
| Stop and restart step 4 on the same runtime | Runtime files normally remain; use the newly printed URL and reopen your saved workflow. |
| Disconnect the browser | This is not a durable backup or a promise that the runtime will remain allocated. |
| Change GPU, reset, delete or terminate a runtime | Treat `/content` as disposable; export first and be ready to repeat setup. |
| Save the notebook in Drive | Saves the document, not all runtime files. This notebook does not silently mount or back up Drive. |

When finished, stop step 4 and use **Runtime → Manage sessions** to terminate your session. Verify that it is gone. A free-account T4 and a paid-account A100 were exercised during preparation on October 18, 2026; availability and eligibility can change. Google's [Colab FAQ](https://research.google.com/colaboratory/faq.html) explains restrictions on external web interfaces in free managed runtimes. An observed successful run is not a guarantee that a future session will be allocated or retained.

For a failed cell, read its actual error. Fix the named dependency, file, memory limit or runtime issue before retrying. Keep the exported outputs and the local course route available if Colab cannot provide a suitable session.
