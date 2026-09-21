# Download the course companion files

## Lecture 1

**[Download Lecture_01_Companion_Files.zip](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/raw/refs/heads/main/downloads/Lecture_01_Companion_Files.zip)**

Extract the ZIP, then open `lecture-01/README.md`. Keep the extracted companion separate from your ComfyUI installation. It contains the guides, command sheets, chapter list, C++ source, recorded environment references, model-path configuration, workflow JSON, original PNG, video title and emoji-formatted video description.

▶️ [Watch Lecture 1](https://youtu.be/KgUhPAOjagI) · 📺 [Full course playlist](https://www.youtube.com/playlist?list=PLUMEJUep1hiI)

The model weights, third-party installers and video are not inside the ZIP. Their publisher download links are in the guides.

## Lecture 2

**[Download Lecture_02_Companion_Files.zip](https://github.com/FurkanGozukara/Generative-AI-Tools-And-Tecniques-2026-2027-Fall/raw/refs/heads/main/downloads/Lecture_02_Companion_Files.zip)**

Extract the ZIP, then open `lecture-02/README.md`. It contains the reference workflow JSON, the original generated PNG with its recoverable metadata, the starting graph from Lecture 1, the update commands, the model-folder guide, the baseline prompt and settings, the measured generation cost, the chapter guide, the video title and the emoji-formatted video description.

▶️ [Watch Lecture 2](https://youtu.be/T2_z7ZaffyI) · 📺 [Full course playlist](https://www.youtube.com/playlist?list=PLUMEJUep1hiI)

The model weights are separate downloads; their publisher links are in the Lecture 1 model guide.

## Check a download

The [SHA256SUMS.txt](SHA256SUMS.txt) file gives the ZIP's SHA-256 hash. In **PowerShell**, run this command from the folder containing your download:

```powershell
Get-FileHash -LiteralPath '.\Lecture_01_Companion_Files.zip' -Algorithm SHA256
```

Compare the returned hash with the published checksum; pass the Lecture 2 filename to the same command for that download. Each extracted folder's `SHA256SUMS.txt` also lists the individual companion-file hashes. Hashes are case-insensitive. To check a particular extracted file, pass its path to the same command.

For the immutable source of a particular revision, open the repository's commit history and browse the desired commit. The `main` download link points to the current companion revision.
