# Windows setup guide

Lecture 1 companion, published September 16, 2026. This guide follows the manual source-installation route used in the lecture. The optional automatic installer is a different route; do not run both into the same folder.

## 1. Prepare a workspace

Create a short, writable folder such as `C:\AI` on a drive with enough free space. Use separate folders for the downloaded companion, Python exercises, ComfyUI and shared models. In File Explorer, show file-name extensions so that a YAML or JSON file does not accidentally become a `.txt` file.

To open the terminal used by the command sheets, navigate to the required folder in Explorer, type `cmd` in its address bar and press Enter. Run the application and package commands without administrator elevation. Windows installers may request elevation when installing system components.

## 2. Install Python and Git

- Download the 64-bit Windows installer from the [Python 3.12.10 release page](https://www.python.org/downloads/release/python-31210/). This is the course baseline. Include the Python launcher and the installer's PATH option. Reopen Command Prompt after installation.
- For the two-environment exercise, also install a Python 3.11 interpreter from [Python's Windows release list](https://www.python.org/downloads/windows/). That exercise needs 3.11 and 3.12; ComfyUI in this lecture uses 3.12.
- Download Git from [Git for Windows](https://git-scm.com/download/win). Select the installer option that makes Git available from the command line, then reopen Command Prompt.

Run the Python and Git checks in [Week01_System_Checks.txt](Week01_System_Checks.txt). The `py -0p` list shows which interpreters the launcher can find. Use `py -3.12` when a task specifically needs Python 3.12.

Create an empty folder for the [environment exercise](Environment-commands.txt). Its NumPy pins deliberately differ between environments. They are not the package requirements for ComfyUI.

## 3. Install the C++ toolchain

Follow [Visual_Studio_Cpp_Checklist.md](Visual_Studio_Cpp_Checklist.md): **Visual Studio Community 2022**, only **Desktop development with C++**, and the listed optional components. Do not select all workloads. Follow the [official Microsoft installation guide](https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-170) and use Microsoft's [older downloads page](https://visualstudio.microsoft.com/vs/older-downloads/) when locating the 2022 release.

After installation, open **x64 Native Tools Command Prompt for VS 2022** from Start and follow the [C++ example guide](examples/README.md). That terminal sets up the compiler, headers and libraries together. Adding only `cl.exe` to an ordinary terminal's PATH is not a replacement for this environment.

## 4. Prepare the NVIDIA stack

Choose your GPU and Windows version on the [official NVIDIA driver page](https://www.nvidia.com/Download/index.aspx). Complete the installation, restart if requested and run `nvidia-smi` in a fresh terminal.

There are three version labels to understand:

| Where you see the version | What it describes |
|---|---|
| `nvidia-smi` | The driver and the CUDA capability advertised by that driver |
| `nvcc --version` | The CUDA Toolkit compiler selected through PATH |
| `torch.version.cuda` | The CUDA build used by the installed PyTorch package |

They do not need to display the same number. Choose a compatible driver and the PyTorch build required by the application. Install a standalone CUDA Toolkit when the course exercise or a native extension needs its compiler. The lecture demonstrates CUDA 12.9.1 and 13.1.1; use the [CUDA Toolkit archive](https://developer.nvidia.com/cuda-toolkit-archive) and the matching version's installation guide. Keep side-by-side toolkit paths distinct, and use `where nvcc` to see which executable your terminal selects.

The ComfyUI command sheet uses the official `cu130` package source. A standalone cuDNN installation or TensorRT ZIP is not an extra step required by that first-image command sheet. Those packages are covered for applications that explicitly need them; follow [Package_downloads.md](Package_downloads.md) and the application's compatibility requirements before adding them.

## 5. Install supporting tools when needed

- **FFmpeg:** follow [Package_downloads.md](Package_downloads.md), extract the complete ZIP, and use [Week01_FFmpeg_commands.txt](Week01_FFmpeg_commands.txt) to add the actual `bin` folder to PATH and run the short media exercise.
- **Node.js:** use the official Windows installer for the application's required version. The lecture's checks use 22.20.0; its release link is in the package guide. Run `node --version` and `npm --version` in a new terminal.
- **cuDNN and TensorRT:** use the release-specific Windows package and its documentation. Do not copy arbitrary DLL versions into unrelated application folders.

For a PATH edit, search Windows for **Edit environment variables for your account**, select `Path`, choose **Edit**, then add a separate entry for the actual executable folder. Keep the existing entries. Open a new terminal afterward; an already-open terminal retains its previous environment.

## 6. Understand Windows memory and path settings

Keep enough free disk space for model downloads, caches and outputs. A Windows page file helps with system-memory pressure; it does not add GPU VRAM. To inspect it, open **View advanced system settings → Advanced → Performance / Settings → Advanced → Virtual memory / Change**. Start with Windows-managed paging and free disk space rather than copying an arbitrary fixed size from another computer. See [Microsoft's page-file introduction](https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/introduction-to-the-page-file).

For path-length errors, first move the installation to a short folder such as `C:\AI`. Windows long-path support also requires application support; follow [Microsoft's long-path documentation](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation) if you need to change that setting. Do not disable system security protections to fix a package or path error.

## 7. Install ComfyUI and generate the image

Follow [Week01_ComfyUI_commands.txt](Week01_ComfyUI_commands.txt) from your installation parent folder. It selects the recorded source snapshot, creates its own virtual environment, installs the NVIDIA packages and starts the server on port 8189.

Then follow [Week01_Model_Downloads.md](Week01_Model_Downloads.md) and load the supplied workflow. Leave the terminal open while ComfyUI runs. Stop it with Ctrl+C before changing startup options or performing maintenance.

After a successful generation, save the original PNG and the matching workflow JSON. The [PNG recovery guide](PNG_Workflow_Recovery.md) explains how to preserve the seed actually submitted to the sampler. Complete the [backup guide](Week01_Backup_and_Recovery.md) before trying an update.
