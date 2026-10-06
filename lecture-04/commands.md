# Update ComfyUI (chapter 2)

Use the Lecture 2 installation and startup route. Stop its running ComfyUI server before restarting after the update. Open Command Prompt in that ComfyUI folder and run each command separately:

```bat
venv\Scripts\activate
```

```bat
git pull --ff-only
```

```bat
python -m pip install -r requirements.txt
```

Restart ComfyUI with the same startup command or shortcut used in Lecture 2, retaining your model-path configuration. Wait for the server to be ready, then refresh its page in the browser. Open the desired workflow from this package. The saved starting workflow still contains the Lecture 3 travel-poster example; chapter 3 begins the image-to-image conversion.
