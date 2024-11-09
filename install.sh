#!/bin/bash

chmod +x clippy
echo "Made executable"
sudo cp clippy /usr/local/bin/clippy
echo "Added clippy to /usr/local/bin"
alias clippy='python3 /usr/local/bin/clippy'
echo "Added alias clippy"
exit
