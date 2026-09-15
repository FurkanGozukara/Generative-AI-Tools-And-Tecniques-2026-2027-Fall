# Recorded environment references

These files come from the lecture's installation and maintenance session. They preserve the recorded package versions and source commits. Keep them as references; create and back up your **own** records inside your ComfyUI folder using the command sheet.

| File | Contents |
|---|---|
| [week01-requirements-lock.txt](week01-requirements-lock.txt) | Installed packages after setup (`pip freeze`) |
| [week01-requirements-after-update.txt](week01-requirements-after-update.txt) | Installed packages after the maintenance exercise |
| [week01-source-install.txt](week01-source-install.txt) | Source commit used for setup |
| [week01-source-after-update.txt](week01-source-after-update.txt) | Source commit after maintenance |
| [week01-startup-options.txt](week01-startup-options.txt) | Saved `python main.py --help` output from the recorded application |

The setup commit is [`d43a5fa20c8547ff42d13232f589a06536c42b97`](https://github.com/Comfy-Org/ComfyUI/commit/d43a5fa20c8547ff42d13232f589a06536c42b97). Maintenance switched to [`19e1058f4c445ef74047e77a23f9ca7684c1e4b6`](https://github.com/Comfy-Org/ComfyUI/commit/19e1058f4c445ef74047e77a23f9ca7684c1e4b6). The before/after package lists contain the same package versions.

Selected recorded packages: `torch==2.14.0+cu130`, `torchvision==0.29.0+cu130`, `torchaudio==2.11.0+cu130`, `comfyui_frontend_package==1.52.7` and `comfyui-manager==4.2.2`. Python 3.12 is the ComfyUI environment used by the lecture.

A `pip freeze` file contains package versions, not wheel hashes, the GPU hardware, index URLs or a complete installer recipe. The CUDA-tagged packages used the official `https://download.pytorch.org/whl/cu130` source. Select the matching source when rebuilding those versions. Package availability and compatibility must be checked before applying the snapshot to another machine.

The public command sheet pins the ComfyUI source but leaves dependency resolution to the package indexes. If you need to reproduce a previous working setup, keep its source commit, Python version, package list, model files and configuration together. Rebuild in a new folder rather than overwriting your backup.

Startup flags can change between versions. For your active installation, generate its own help file with `python main.py --help > week01-startup-options.txt` and use only the options it lists.
