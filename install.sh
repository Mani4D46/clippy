#!/bin/bash

chmod +x clippy
echo "Made executable"
sudo cp clippy /usr/local/bin/clippy
echo "Added clippy to /usr/local/bin"
alias clippy='python3 /usr/local/bin/clippy'

# Determine the user's shell (extracting just the shell name)
SHELL_NAME=$(basename "$SHELL")

# The alias you want to add
ALIAS="alias clippy='python3 /usr/local/bin/clippy'"

# Function to add alias to the appropriate shell config file
add_alias() {
    if [ -f "$1" ]; then
        # Check if the alias is already in the config file
        if ! grep -q "$ALIAS" "$1"; then
            echo "$ALIAS" >> "$1"
            echo "Alias added to $1"
        else
            echo "Alias already present in $1"
        fi
    else
        echo "$1 not found. Skipping."
    fi
}

# Check for bash or zsh and call add_alias
if [ "$SHELL_NAME" == "bash" ]; then
    add_alias "$HOME/.bashrc"
elif [ "$SHELL_NAME" == "zsh" ]; then
    add_alias "$HOME/.zshrc"
else
    echo "Unsupported shell: $SHELL_NAME"
    exit 1
fi

exit
