# Lecture 8 command reference

Use **Windows Command Prompt**. The paths in [Lecture08_commands.txt](Lecture08_commands.txt) are the recorded installation paths; substitute your own ComfyUI and extracted companion folders. Activate that installation's `venv\Scripts\activate` before the Python examples. Keep the API scripts together and run them from the companion's `api` folder.

## API inspection, submission and queue

The complete commands are in [api/README.md](api/README.md). Inspect the export first, then use `--dry-run`; a live submission needs the matching server and models. The lecture's main server is `http://127.0.0.1:8189`; its separate test installation uses port `8190`.

## Live schemas and SDK versions

Open `http://127.0.0.1:8189/object_info` in the browser to inspect the schemas of the nodes your server actually has. In the activated environment:

```cmd
pip index versions comfy-sdk
```

This lists available SDK versions; the supplied standard-library clients do not require the SDK. The lecture observed version `0.5.0` at its recording date.

## Inspect a node pack

From the actual pack folder, such as `ComfyUI\custom_nodes\comfyui-impact-pack`:

```cmd
findstr /s /n /i "subprocess download_url eval( exec(" *.py
findstr /s /n /i "environ token requests." *.py
```

Read the surrounding code to understand each match. These string searches point to behavior worth inspecting; they do not prove that a pack is safe or unsafe. For the model hash example, from `ComfyUI\models\sams`:

```cmd
certutil -hashfile sam_vit_b_01ec64.pth SHA256
```

## Record an environment

From your ComfyUI root with its environment active:

```cmd
git rev-parse HEAD > Lecture08_core_commit.txt
python -m pip freeze > Lecture08_requirements_lock.txt
set COMFYUI_PATH=%CD%
cm-cli save-snapshot --output L08_snapshot.json
cm-cli restore-snapshot --help
```

The final command displays restore options; it does not apply a restore. The Manager CLI must be installed and available in your environment. The [recorded files](environment/README.md) are compatibility references. A dependency list describes installed packages; it does not include model weights or guarantee an identical environment on another computer.

## Isolate a problem

The lecture uses a separate ComfyUI checkout and virtual environment. Place [run_isolated_no_custom_nodes.bat](launchers/run_isolated_no_custom_nodes.bat) or [run_isolated_one_pack.bat](launchers/run_isolated_one_pack.bat) in that separate installation's root. They expect `main.py` and `venv\Scripts\python.exe` there and start port `8190`.

The first launcher disables all custom nodes. The second allows `comfyui-inpaint-cropandstitch` while the other custom nodes stay disabled. Prepare that pack in the test copy before using it. Submit the same supplied API graph to `http://127.0.0.1:8190` to compare the isolated core route, then inspect startup and job errors before adding another variable. The launchers do not create the installation or copy its models.
