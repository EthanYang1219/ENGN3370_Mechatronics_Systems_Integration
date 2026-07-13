# ENGN3370 Mechatronic System Integration

Coursework repository for **ENGN3370 (Mechatronic System Integration)**. It contains two
independent tracks of work built on a Raspberry Pi:

- **`robot_control/`** — GPIO/I2C code for driving a 4-motor robot chassis through a PCA9685
  PWM/motor driver HAT, plus IR obstacle-avoidance and a buzzer demo.
- **`computer_vision/`** — standalone OpenCV experiments (colour space conversions, an
  interactive BGR/RGB colour picker, an install smoke test). This track does not import
  anything from `robot_control/` and has no dependency on the robot hardware.

The two folders can be read and run independently of each other.

## Repository structure

```
.
├── robot_control/
│   ├── robot_control.py       # PCA9685 driver class + FSDEROBOT movement library (shared)
│   ├── Yang_robotcontrol.py   # Demo: drives a preset forward/strafe/back/strafe pattern
│   ├── infrared_control.py    # Demo: IR obstacle avoidance + button + status LEDs
│   └── buzzer_music.py        # Standalone gpiozero TonalBuzzer demo
├── computer_vision/
│   ├── colour_space.py            # Loads assets/profile.png, converts to RGB/RGBA/gray/HSV/HSV_FULL/YUV, displays one via matplotlib
│   ├── bgr_color_picker.py        # OpenCV trackbar GUI to interactively preview a BGR/RGB colour
│   ├── test_opencv.py             # Smoke test: prints cv2 version, writes assets/test.jpg, displays assets/profile.png
│   └── README_OpenCV_Workflow.md  # Full SSH/X11-forwarding workflow for running these scripts headless on a Pi
├── assets/                    # Images used/produced by the computer_vision scripts
│   ├── profile.png
│   ├── profile_rgb.png
│   ├── colour_space.png
│   ├── altered.png
│   └── test.jpg
└── .gitignore
```

All scripts use paths like `"assets/profile.png"` that are **relative to the current working
directory**, not to the script's own location — always run commands from the repository root
as shown below.

## `robot_control/`

Targets a Raspberry Pi with a PCA9685-based motor driver HAT wired to four DC motors (motor D
is additionally driven through two direct Raspberry Pi GPIO pins for direction).

- **`robot_control.py`** — Not run directly. Defines:
  - `PCA9685`: a low-level I2C driver (via `smbus`) for setting the PWM frequency and duty
    cycle/level on the PCA9685's 16 channels.
  - `FSDEROBOT`: the shared robot library built on top of `PCA9685`. Wires up four motors
    (A–D) and exposes movement methods — `t_up`/`t_down` (forward/backward),
    `moveLeft`/`moveRight` (strafe), `turnLeft`/`turnRight` (spin in place),
    `forward_Left`/`forward_Right`/`backward_Left`/`backward_Right` (diagonals), `t_stop`,
    plus the low-level `MotorRun`/`MotorStop`. Both demo scripts below import `FSDEROBOT`
    from this file.
- **`Yang_robotcontrol.py`** — Demo script. Instantiates `FSDEROBOT` and loops through a
  preset pattern (forward → stop → strafe right → stop → backward → stop → strafe left →
  stop). Installs `SIGINT`/`SIGTERM` handlers so the robot stops cleanly on Ctrl+C or
  termination.
- **`infrared_control.py`** — Demo script. Instantiates `FSDEROBOT` and reads two IR
  obstacle-avoidance sensors (`Button` on GPIO 16 and GPIO 12) and a physical button
  (GPIO 19) via `gpiozero`, driving red/green status LEDs (GPIO 6 / GPIO 5) and steering the
  robot based on which sensor(s) detect an obstacle. Only runs its sensing loop while the
  button is pressed.
- **`buzzer_music.py`** — Standalone demo, no dependency on `robot_control.py`. Drives a
  `gpiozero.TonalBuzzer` on GPIO 17 and plays a short sequence of notes/tones (`"A4"`,
  `"C#5"`, a raw 500 Hz value, and a `Tone(440)` object).

### Requirements

- A Raspberry Pi with the I2C bus enabled and a PCA9685 motor driver HAT wired per the pin
  assignments in `robot_control.py` (I2C address `0x40`).
- Python packages: `gpiozero`, `smbus`.
- These scripts **will not run on a regular laptop** — they require the actual GPIO/I2C
  hardware present on a Raspberry Pi.

### Running

From the repository root, on the Pi:

```bash
python3 robot_control/Yang_robotcontrol.py
python3 robot_control/infrared_control.py
python3 robot_control/buzzer_music.py
```

Press Ctrl+C to stop; the movement scripts catch the interrupt and stop the motors before
exiting.

## `computer_vision/`

OpenCV/NumPy/matplotlib experiments, unrelated to the robot code above.

- **`colour_space.py`** — Loads `assets/profile.png` with `cv2.imread` (BGR), converts it to
  RGB, RGBA, grayscale, HSV, HSV_FULL, and YUV, then displays one of the converted images
  (`image_show`, set to the HSV version by default) with matplotlib.
- **`bgr_color_picker.py`** — Opens an OpenCV window with R/G/B trackbars (0–255) and
  continuously fills a blank 640x480 image with the selected colour for live preview. Press
  `q` in the window to quit.
- **`test_opencv.py`** — Install/setup smoke test: prints the installed `cv2.__version__`,
  writes a plain white 100x100 square to `assets/test.jpg`, then loads `assets/profile.png`
  (auto-scaled down to fit within 800 px on the longest side if needed) and displays it,
  waiting for a keypress before closing.

### Requirements

- Python packages: `opencv-python` (`cv2`), `numpy`, `matplotlib`.
- These scripts open GUI windows (`cv2.imshow` / matplotlib), so they need somewhere to draw
  a window. On a headless Raspberry Pi accessed over SSH, see
  **[`computer_vision/README_OpenCV_Workflow.md`](computer_vision/README_OpenCV_Workflow.md)**
  for the full PuTTY + X11 forwarding + VcXsrv setup, connection details, and
  troubleshooting notes (missing `$DISPLAY`, `ModuleNotFoundError: cv2`, font warnings,
  etc.). That file is the source of truth for the headless run workflow and isn't repeated
  in full here.

### Running

From the repository root:

```bash
python3 computer_vision/test_opencv.py
python3 computer_vision/colour_space.py
python3 computer_vision/bgr_color_picker.py
```

## Notes

- `.gitignore` excludes `.venv/`, `__pycache__/`, and `*.pyc`.
- This is a personal coursework repository for a university unit, not a published package —
  there is no CI, release process, or contribution process attached to it.
# ENGN3370_Mechatronics_Systems_Integration
