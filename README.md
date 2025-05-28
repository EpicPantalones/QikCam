# QikCam

instantaneous socket-based PiCam.

## Usage

Flash Rasbperry Pi Z2W with Rasbian OS Lite (64 bit).

Attach camera module.

Upon log in, run:

```sh
curl <put link here>
chmod +x ./isntall.sh
./install.sh
```

You can now run the camera by running

```sh
python3 camera/sender.py
```
