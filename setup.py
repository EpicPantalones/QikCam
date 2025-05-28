import yaml
import re
import random
import string

# Paths
CONFIG_PATH = "config.yaml"
SENDER_PATH = "sender.py"

# Load config.yaml
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

# Read sender.py
with open(SENDER_PATH, "r") as f:
    sender_code = f.read()

# Handle token generation or usage
sender_cfg = config["sender"]
if sender_cfg.get("gen_token", False):
    token_length = sender_cfg.get("token_length", 16)
    token = ''.join(random.choices(
        string.ascii_letters + string.digits, k=token_length))
    sender_cfg["token"] = token
else:
    token = sender_cfg.get("token", "")

print(f"token: {token}")

# Replace __NAME__ placeholders with config values
for key, value in config.get("sender", {}).items():
    placeholder = f"__{key.upper()}__"
    sender_code = re.sub(re.escape(placeholder), str(value), sender_code)

# Write updated sender.py
with open(SENDER_PATH, "w") as f:
    f.write(sender_code)
