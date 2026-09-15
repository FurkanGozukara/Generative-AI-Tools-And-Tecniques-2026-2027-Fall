# Week 01 backup and recovery

Stop the ComfyUI server with Ctrl+C and save your workflow before maintenance.
Create a dated backup folder beside the application. Copy `user` and `output`
and keep the saved workflow JSON with the generated images.

Also copy these files from the application folder:

- `week01-requirements-lock.txt`
- `week01-source-install.txt`
- `extra_model_paths.yaml`
- `week01-startup-options.txt`

The shared model library lives outside the application at
`C:/AI/Shared_Models_Week01/models` in the public example, or
`G:/educational_videos/Shared_Models_Week01/models` in the recording. Keep a backup of that
library or retain the original model links and filenames for downloading it
again. Change the base path in the YAML template to your own library location.

If you use ComfyUI's default model folders instead, back up its `models`
folder or keep the download links. Copy `input` if you supplied input media,
and save any custom-node configuration you added. Skip files or folders that
you have not created. The supplied first-image workflow needs no separately
installed custom-node pack.

Generate `week01-startup-options.txt` with
`python main.py --help > week01-startup-options.txt` while the environment is
active. Package and source files under this companion's `references` folder
are the instructor's recorded snapshots. Back up the files generated in your
own installation; do not replace them with those reference copies.

Use the maintenance commands in `Week01_ComfyUI_commands.txt`. This sequence
switches from the recorded detached course snapshot to the tracked master
branch, pulls fast-forward only, refreshes application and Manager requirements,
runs `pip check`, and writes separate after-update package and source records.
Copy both after-update records into the dated backup beside the earlier files.

After updating, restart ComfyUI and open a known workflow. Check its model
selections, run it, and save the result. If the update fails, read the first
relevant error and use the saved source identifier and package list to rebuild
the earlier environment in a separate folder. Restore the workflow and output
folders and point its model mapping at the preserved model library.

When rebuilding, clone into a new folder, select the saved source commit,
create a fresh Python 3.12 virtual environment and install the matching GPU
packages and application requirements. Use your saved package list to select
the previous versions. CUDA-tagged PyTorch wheels need their matching
official package source; a plain `pip freeze` file does not record that source.
Do not overwrite the working backup or assume a copied virtual environment
will work after moving it to another path.

The recorded installation source was
`d43a5fa20c8547ff42d13232f589a06536c42b97`. Maintenance switched to
`19e1058f4c445ef74047e77a23f9ca7684c1e4b6`; the pull reported already up to date,
and the before/after package lists contained the same package versions.
