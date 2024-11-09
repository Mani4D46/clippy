#!/bin/bash

python3 -m pip install -r requirements.txt
chmod +x clippy
sudo cp clippy /usr/local/bin/clippy
alias clippy='python3 /usr/local/bin/clippy'
