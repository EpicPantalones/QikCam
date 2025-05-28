import os
import time
import socket

DEST_IP = '__IP_ADDR__'
DEST_PORT = __PORT__
INTERVAL = __INT__
CAM_ID = '__CAM_ID__'
TOKEN = '__TOKEN__'
IMAGE_PATH = '/home/__CAM_ID__/QikCam/image.jpg'

CAPTURE_CMD = f"libcamera-still -n --immediate -e jpg --width __WIDTH__ --height __HEIGHT__ -o {IMAGE_PATH}"


def send_image(path):
    with socket.socket() as s:
        s.connect((DEST_IP, DEST_PORT))
        header = f"{CAM_ID},{TOKEN}\n"
        s.sendall(header.encode())
        with open(path, 'rb') as f:
            s.sendfile(f)


while True:
    os.system(CAPTURE_CMD)
    send_image(IMAGE_PATH)
    time.sleep(INTERVAL)
