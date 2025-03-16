#!/bin/bash

echo "SDLinux Installer - Setting up your system..."

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root (use sudo)."
    exit 1
fi

# Ask for confirmation to install SDLinux
read -p "Are you sure you want to install SDLinux? (y/n): " confirm_install

if [[ "$confirm_install" != "y" && "$confirm_install" != "Y" ]]; then
    echo "Installation canceled."
    exit 0
fi

# Wait 3 seconds before the next step
sleep 3

# Ask if the user wants to update the package list
read -p "Do you want to update the package list? (y/n): " update_choice

if [[ "$update_choice" == "y" || "$update_choice" == "Y" ]]; then
    echo "Updating package lists..."
    sleep 3
    apt update -y
else
    echo "Skipping package list update."
    sleep 3
fi

# Check if Python is installed
if command -v python3 &> /dev/null; then
    echo "Python is already installed."
    # Ask if the user wants to reinstall Python
    read -p "Do you want to reinstall Python? (y/n): " reinstall_python
    if [[ "$reinstall_python" == "y" || "$reinstall_python" == "Y" ]]; then
        echo "Reinstalling Python..."
        sleep 3
        apt install --reinstall -y python3 python3-pip
    else
        echo "Skipping Python installation."
    fi
else
    echo "Installing Python..."
    sleep 3
    apt install -y python3 python3-pip
fi

# Create the SDLinux directory if it doesn't exist
mkdir -p /SDLinux

# Download the setup script into the SDLinux directory
echo "Downloading the SDLinux setup script..."
sleep 3
wget -O /SDLinux/setup/setup.py "https://alexidians.github.io/SDLinux/SDLinux/setup/setup.py"

# Wait before running the setup script
echo "Running the SDLinux setup script..."
sleep 3
cd /SDLinux
python3 /SDLinux/setup/setup.py

echo "SDLinux setup complete!"
