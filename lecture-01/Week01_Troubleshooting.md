# Lecture 1 troubleshooting

Start with the first relevant error in the Command Prompt. Run one change at a time, then repeat the failed step. Do not continue through the remaining install commands after an earlier command has failed.

## A command is not found, or the wrong Python runs

Open a new **Command Prompt** after an installation or PATH edit. Run `where python`, `where git` or the matching command from [Week01_System_Checks.txt](Week01_System_Checks.txt). In PowerShell, use `where.exe`; plain `where` is a different command there.

For the course interpreter, run `py -3.12 --version`. If it is missing from `py -0p`, install Python 3.12 with the launcher. In the ComfyUI folder, run `venv\Scripts\activate.bat`, then `python -c "import sys; print(sys.executable)"`. The path should be inside that installation's `venv`.

Use `python -m pip` so that package installation follows the Python executable you just selected. Do not mix the environment exercise's NumPy pins into the ComfyUI environment.

## A package install fails or pip reports conflicts

Read the package name and first error, not just the final summary. Check the active Python version, available disk space and the package's supported Python/GPU versions. Run `python -m pip check` after a completed install.

The course source commit is fixed, but the ordinary install commands resolve packages from the indexes at the time you run them. The [recorded snapshots](references/README.md) show what was installed during the lecture; they are not a universal cross-platform lockfile. For a damaged environment, build a fresh environment in a separate installation folder instead of repeatedly changing unrelated global packages.

## cl is missing, or C++ headers/libraries cannot be found

Use **x64 Native Tools Command Prompt for VS 2022**, not an ordinary Command Prompt with only `cl.exe` added to PATH. Follow the [component checklist](Visual_Studio_Cpp_Checklist.md) and [example instructions](examples/README.md). The expected program output ends with `sum=42`.

## CUDA is unavailable in PyTorch

Run the PyTorch check in [Week01_System_Checks.txt](Week01_System_Checks.txt) from the activated ComfyUI environment. If `nvidia-smi` also fails, check the NVIDIA driver installation first. If `nvidia-smi` works but PyTorch reports no CUDA device, check that the installed PyTorch build, driver and GPU are compatible and that you installed into this environment.

The `CUDA Version` heading in `nvidia-smi` is not the version of a separately installed Toolkit. Use `nvcc --version` for the selected Toolkit compiler and `torch.version.cuda` for the PyTorch CUDA build. Installing every CUDA Toolkit version does not fix a mismatched Python environment or GPU package.

## ComfyUI will not open in the browser

Keep its terminal open and wait for the local address. Open the **port printed by that running server**, not a bookmarked default port. This course launches on `http://127.0.0.1:8189`.

If the port is already in use, stop your earlier ComfyUI server with Ctrl+C, or launch this one with another unused port and use that new address. Do not terminate an unrelated process just to free the port. If the server exited, fix the terminal error before refreshing the browser. Local-only use does not need a public tunnel or `--listen 0.0.0.0`.

## The workflow reports a missing model

Use [Week01_Model_Downloads.md](Week01_Model_Downloads.md) to check all three filenames and categories. A browser download may still be incomplete, or an error page may have been saved instead of the model. Compare its file size with the recorded reference, and inspect the publisher's current file page if it changed.

For shared models, put `extra_model_paths.yaml` beside `main.py`, make `base_path` point to the parent of `models`, preserve spaces rather than tabs, and show file-name extensions to catch `.yaml.txt`. Restart the server, reload the workflow and choose the intended file in each selector.

## Nodes are missing when opening the workflow

Load the supplied JSON in the recorded course installation. The first-image graph uses built-in ComfyUI nodes, so do not install an arbitrary custom-node pack just because a grouped node looks unfamiliar. Check startup import errors and your ComfyUI/frontend versions. Use the [official workflow guide](https://docs.comfy.org/tutorials/image/z-image/z-image-turbo) if you intentionally choose a newer template, and back up before updating.

## Out of memory or a very slow first generation

Use batch size 1 and close other GPU-heavy applications. Wait for model loading to finish before deciding that the process is stuck. Check both GPU memory and Windows system memory; page-file space is not GPU VRAM.

Start with the basic launch command. If memory pressure continues, inspect `python main.py --help` for the modes supported by your installed version and try the optional memory-mode example in the command sheet. Different offloading settings trade speed for memory use. If you lower the resolution or change model precision, you are changing the example configuration; save that as a separate workflow.

## The seed changes or the saved result differs

Some template controls randomize the seed for the next run. Restore the submitted seed **before** saving the JSON, or load the original PNG to recover its embedded settings. Follow [PNG_Workflow_Recovery.md](PNG_Workflow_Recovery.md).

A re-encoded image, screenshot or social-media copy may have no embedded workflow. Download this repository's original PNG, or use the accompanying JSON. Check the actual connected values on the grouped workflow, plus the prompt, models, resolution and software versions.

## FFmpeg runs, but a Python audio/video package still fails

`ffmpeg -version` checks the executable available to Command Prompt. A Python library may require a particular shared-library build and compatible Python/PyTorch versions. Follow that library's instructions, such as [TorchCodec's compatibility guide](https://github.com/meta-pytorch/torchcodec), instead of assuming any FFmpeg ZIP is interchangeable.

## A ComfyUI update fails

Stop at the error and keep your backup. The course starts from a detached commit; the maintenance sheet switches to `master` before pulling. If Git reports local changes, review them without discarding them. Follow [Week01_Backup_and_Recovery.md](Week01_Backup_and_Recovery.md) to rebuild the earlier setup in a separate folder if needed.

When asking for help, share the command, the first relevant error and the versions, with passwords, tokens and account details removed.
