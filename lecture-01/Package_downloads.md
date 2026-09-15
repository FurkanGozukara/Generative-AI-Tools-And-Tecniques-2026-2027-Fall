# Download packages that match the installation route

## FFmpeg

Open https://ffmpeg.org/download.html and choose Windows executable files.
Follow the Gyan build-provider link, scroll to release builds, and download
the essentials ZIP. The recording uses 9.0.1 essentials. Wait until the
download completes, open the ZIP in Explorer, and extract the complete
versioned folder. Follow `Week01_FFmpeg_commands.txt` to add its `bin` folder
to Path and check both ffmpeg and ffprobe in a fresh Command Prompt.

Build provider: https://www.gyan.dev/ffmpeg/builds/

## cuDNN

Open https://developer.nvidia.com/cudnn-archive and choose the release your
application supports. The course installation uses cuDNN 9.19. Follow the
Windows installation instructions for that release and select the graphical
Windows executable to follow the installation shown in the lecture.

A separate ZIP contains libraries and has a different setup route. Follow
the instructions supplied for the package you choose. Check the supported
CUDA version before downloading.

Windows guide: https://docs.nvidia.com/deeplearning/cudnn/installation/latest/windows.html

## TensorRT

Open https://developer.nvidia.com/tensorrt-getting-started and select
Download Now. Sign in to NVIDIA if requested. Select the Windows ZIP for
the TensorRT release and CUDA version supported by your application.
Download it, then extract the complete folder. Keep its libraries, headers,
tools and Python wheels together, and follow that release's Windows ZIP
installation guide. Use your extracted package's actual folder structure
when adding library directories or selecting a Python wheel.

Windows ZIP guide: https://docs.nvidia.com/deeplearning/tensorrt/latest/installing-tensorrt/install-zip.html

## Node.js

Start at https://nodejs.org/en/download and select the Windows installer
for your system and the Node.js release required by your application.
The course version checks use 22.20.0. Use the
official previous-release archive when reproducing that exact version.

Recorded release: https://nodejs.org/en/blog/release/v22.20.0
