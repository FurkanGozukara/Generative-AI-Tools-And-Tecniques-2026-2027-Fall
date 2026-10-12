# Update and custom-node commands

These steps prepare the Lecture 1 installation for Lecture 5. Recorded versions: ComfyUI 0.39.0, frontend 1.55.14 and Crop-and-Stitch 3.0.17. Versions will change.

## Update ComfyUI ([0:59](https://www.youtube.com/watch?v=DJcgVASlg38&t=59s))

Open your ComfyUI installation folder in File Explorer, type `cmd` in its address bar and press Enter. Check that the prompt shows your ComfyUI folder, then run each command separately:

```bat
venv\Scripts\activate
```

```bat
git pull --ff-only
```

```bat
python -m pip install -r requirements.txt
```

After activation, the prompt starts with `(venv)`, so the package command uses this installation's Python. If Git reports a local conflict, resolve that conflict before installing the requirements. Keep the installation output visible until the command finishes. Then restart ComfyUI with your usual startup command and refresh its browser page. Your configured model folders remain available.

## Save a Manager snapshot ([2:26](https://www.youtube.com/watch?v=DJcgVASlg38&t=146s))

Save the installation state before adding a custom node pack. With ComfyUI running, open Command Prompt in the same folder and run:

```bat
curl --fail --request POST http://127.0.0.1:8189/v2/snapshot/save
```

The address is the one ComfyUI prints at startup; Lecture 1 starts the server with `--enable-manager --port 8189`. The snapshot is saved as a dated JSON file in `user\__manager\snapshots` inside your ComfyUI folder. Inspect the newest file, for example:

```bat
more "user\__manager\snapshots\YYYY-MM-DD_HH-MM-SS_snapshot.json"
```

A snapshot records application and pack versions. Keep your workflows and model files as well; they are separate assets you need when restoring a complete working setup on another computer.

## Install Crop-and-Stitch ([3:30](https://www.youtube.com/watch?v=DJcgVASlg38&t=210s))

In ComfyUI, open **Extensions** and search for `Crop and Stitch`. Choose **ComfyUI-Inpaint-CropAndStitch** by **lquesada**; check the pack name and version before installing, because several packs contain similar words. Select **Install** for that Registry entry and wait for the installation to finish.

Restart ComfyUI: new Python nodes load only when the server starts, so refreshing the browser alone is not enough. After the restart, press **R** to refresh the node definitions, open the node search and look for **Inpaint Crop**. The pair is **Inpaint Crop** and **Inpaint Stitch**, marked with a scissors symbol. The supplied workflows keep their class and version information, which distinguishes them from older examples with similar display names.
