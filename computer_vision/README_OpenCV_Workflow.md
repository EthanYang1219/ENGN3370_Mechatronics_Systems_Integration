# OpenCV on Raspberry Pi via PuTTY + VcXsrv

How to run OpenCV scripts (that open windows with `cv2.imshow`) on the Raspberry Pi
and see the windows on your **Windows laptop** — no external monitor needed.

**The idea:** the Pi runs the code; the window is "forwarded" over SSH to an X server
(VcXsrv) running on your laptop.

- **VS Code** = where you *edit* the code
- **PuTTY**  = where you *run* the code (it's the only place `$DISPLAY` is set)
- **VcXsrv** = the program on Windows that actually draws the windows

---

## Connection details

| Thing | Value |
|-------|-------|
| Pi IP address | `192.168.137.133` (on the laptop hotspot — may change if Pi reconnects) |
| SSH user | `yang` |
| Project folder | `~/Desktop/ENGN3370_Mechatronic-System-Integration` |
| Python venv | see "Two virtual environments" below |

> If the IP changed, run `hostname -I` on the Pi (e.g. via the VS Code terminal) to find the new one.

---

## ⚠️ Two virtual environments (important)

This project has **two** separate Python virtual environments. You must `source` the
right one, or you'll hit `ModuleNotFoundError: No module named 'cv2'`.

| venv | Path | Typically used for |
|------|------|--------------------|
| `cv-venv` | `~/cv-venv` | the older top-level smoke test |
| `.venv`   | `~/Desktop/ENGN3370_Mechatronic-System-Integration/.venv` | the `computer_vision/` scripts |

Activate whichever you need (from the project root):
```bash
source ~/cv-venv/bin/activate     # activates cv-venv
# ...or...
source .venv/bin/activate         # activates the in-project .venv
```

The `(cv-venv)` or `(.venv)` prefix in your prompt tells you which is active.
Run `deactivate` before switching to the other.

> Each venv has its **own** copy of OpenCV, so the QFontDatabase font fix (see Troubleshooting)
> has to be applied to **both** — which it already has been. Consolidating to a single venv
> later would remove this footgun.

---

## Start-up (once, each time you sit down)

1. **Windows:** start **VcXsrv** via XLaunch
   - Multiple windows → Display number `0` → **Start no client** → ✅ **Disable access control** → Finish
   - Leave the black **"X" icon** running in the system tray.
2. **Windows:** open **PuTTY**
   - Host `192.168.137.133`, Port `22`, type SSH
   - `Connection → SSH → X11` → ✅ **Enable X11 forwarding**, X display location `localhost:0`
   - **Open**, log in as `yang`.
3. **In PuTTY**, prepare the session:
   ```bash
   cd ~/Desktop/ENGN3370_Mechatronic-System-Integration
   source ~/cv-venv/bin/activate
   echo $DISPLAY        # should print: localhost:10.0
   ```
   Your prompt now starts with `(cv-venv)` = venv is active.

---

## The edit–run loop

```
edit in VS Code → Ctrl+S → PuTTY: ↑ then Enter → window appears → press a key to close → repeat
```

To run the script:
```bash
python3 computer_vision/test_opencv.py
```
- Press **↑ (up arrow)** + **Enter** in PuTTY to repeat the last command.
- **Save in VS Code (Ctrl+S) first** — Python runs the saved file, not what's on screen.
- **Press any key** while the image window is focused to close it and return to the terminal.

You only repeat the start-up steps if you **close PuTTY** or **close VcXsrv**.

---

## Troubleshooting

### `python3: can't open file '/home/yang/computer_vision/test_opencv.py'`
You're in the wrong folder. Run:
```bash
cd ~/Desktop/ENGN3370_Mechatronic-System-Integration
```
Check where you are anytime with `pwd`.

### It ran before but now "can't run" after I closed the window
Closing PuTTY resets the session. After reopening, redo:
```bash
cd ~/Desktop/ENGN3370_Mechatronic-System-Integration
source ~/cv-venv/bin/activate
```

### `xclock: Can't open display` OR `$DISPLAY` is empty
X11 forwarding isn't active. In order:
1. Is **VcXsrv running** on Windows? (black "X" in tray). If not, launch XLaunch.
2. Reconnect with PuTTY, making sure **Enable X11 forwarding** is ticked *before* you click Open.
3. After login, `echo $DISPLAY` must show `localhost:10.0`. If blank, the PuTTY checkbox
   didn't save — re-tick it, Session → Default Settings → Save, then reconnect.

### `qt.qpa.xcb: could not connect to display`
Same root cause as above — no display. You're either running outside PuTTY (e.g. the
VS Code terminal, which has no `$DISPLAY`) or VcXsrv isn't running. Run the script **in PuTTY**.

### The program says "Aborted" right after showing a window
Usually a bug in the script, not the connection. Common ones:
- `cv2.waitkey(0)` → must be **`cv2.waitKey(0)`** (capital K). Without it, the window
  can't render and OpenCV aborts.
- Loading an image that doesn't exist: `cv2.imread("x.png")` returns `None`, and passing
  `None` to `cv2.imshow` crashes. Guard it:
  ```python
  img = cv2.imread("assets/profile.png")
  if img is None:
      print("Could not load image — check the filename/path")
  else:
      cv2.imshow("image", img)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
  ```
- Relative paths like `"assets/profile.png"` only work if you `cd` into the project folder first.

### `ModuleNotFoundError: No module named 'cv2'`
The venv isn't active, **or the wrong one is active** (see "Two virtual environments" above).
Activate the one that has OpenCV for the script you're running — e.g. `source .venv/bin/activate`
for the `computer_vision/` scripts — and confirm the `(...)` prefix shows in your prompt.

### Window is bigger than my screen
The image is high-resolution. Shrink it before showing:
```python
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)   # 30% size
```

### `QFontDatabase: Cannot find font directory .../cv2/qt/fonts`
Harmless **warning** — the image still shows. OpenCV's bundled Qt can't find fonts for
window decorations. To silence it, link the system DejaVu fonts into the folder Qt expects.
**Do this for each venv** (see "Two virtual environments") — redo it if you ever recreate a venv:
```bash
# cv-venv
FONTDIR="$HOME/cv-venv/lib/python3.13/site-packages/cv2/qt/fonts"
mkdir -p "$FONTDIR" && ln -sf /usr/share/fonts/truetype/dejavu/*.ttf "$FONTDIR/"

# in-project .venv
FONTDIR="$HOME/Desktop/ENGN3370_Mechatronic-System-Integration/.venv/lib/python3.13/site-packages/cv2/qt/fonts"
mkdir -p "$FONTDIR" && ln -sf /usr/share/fonts/truetype/dejavu/*.ttf "$FONTDIR/"
```
If DejaVu isn't installed: `sudo apt install fonts-dejavu`.

### Windows appear but live camera video is very laggy
Normal for X11 forwarding over Wi-Fi — fine for testing, not smooth real-time. For real-time
work you'd use a physical monitor or a streaming approach instead.

---

## General debugging tips
- Read the **last line** of the error first — it usually names the problem.
- Reproduce with the smallest code possible (e.g. just load + show one image).
- Check the obvious: right folder (`pwd`), venv active (`(cv-venv)` in prompt),
  display set (`echo $DISPLAY`), file saved in VS Code.
- Print things: `print(img.shape)` after `imread` confirms the image actually loaded.
