# QikCam

instantaneous socket-based PiCam.

## Usage

Flash Rasbperry Pi Z2W with Rasbian OS Lite (64 bit).

Attach camera module.

Upon log in, run:

```sh
curl -O https://raw.githubusercontent.com/EpicPantalones/QikCam/refs/heads/main/install.sh
chmod +x ./isntall.sh
./install.sh
```

Once those steps finish, the resulting GitHub repo will have a `config.yaml`. Edit the settings to your setup, then run

```sh
python3 setup.py
```

You can now run the camera by running

```sh
python3 camera/sender.py
```
