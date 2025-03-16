import subprocess
import sys
import os
import shutil

# Function to check and install missing modules
def check_and_install_module(import_name, install_name):
    try:
        # Try to import the module
        __import__(import_name)
    except Exception as e:
        print(f"Module {import_name} not found. Installing {install_name}...")
        # Install the module if not found
        subprocess.check_call([sys.executable, "-m", "pip", "install", install_name])
        # Try importing it again after installation
        __import__(import_name)

# List of required modules: [importname installname]
modules = [
    ['requests', 'requests'],
    # Add other modules as needed: ['import_name', 'install_name']
]

# Install each required module individually
for module in modules:
    check_and_install_module(module[0], module[1])

# Download the new icon and wallpaper
def download_file(url, destination):
    try:
        import requests
        response = requests.get(url)
        with open(destination, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def extract_zip(zip_file_path, extract_to):
    """Extract a ZIP file to a specified directory."""
    try:
        # Create the extraction directory if it doesn't exist
        os.makedirs(extract_to, exist_ok=True)

        # Open the zip file and extract its contents
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted {zip_file_path} to {extract_to}")
    except zipfile.BadZipFile:
        print(f"Error: Bad zip file or extraction failed for {zip_file_path}")
    except Exception as e:
        print(f"Error extracting {zip_file_path}: {str(e)}")


print("Updating Style...")
# Paths for images
icon_url = "https://alexidians.github.io/SDLinux/SDLinux/images/SuperDiamondIcon.png"
wallpaper_url = "https://alexidians.github.io/SDLinux/SDLinux/wallpapers/default.png"

icon_path = "/SDLinux/images/SuperDiamondIcon.png"
wallpaper_path = "/SDLinux/wallpapers/default.png"

# Download the icon and wallpaper to the appropriate directories
download_file(icon_url, icon_path)
download_file(wallpaper_url, wallpaper_path)

# Replace system icons with the new SuperDiamondIcon.png
def replace_system_icons():
    # List of directories where icons are located
    icon_directories = [
        "/usr/share/icons/hicolor/16x16/apps",
        "/usr/share/icons/hicolor/32x32/apps",
        "/usr/share/icons/hicolor/48x48/apps",
        "/usr/share/icons/hicolor/64x64/apps",
        "/usr/share/icons/hicolor/128x128/apps",
        "/usr/share/icons/hicolor/256x256/apps"
    ]

    for directory in icon_directories:
        # Replace the existing icon with the new one
        if os.path.exists(directory):
            for icon in os.listdir(directory):
                icon_path_to_replace = os.path.join(directory, icon)
                if os.path.isfile(icon_path_to_replace):
                    print(f"Replacing icon: {icon_path_to_replace}")
                    shutil.copy(icon_path, icon_path_to_replace)

# Replace the default wallpaper without affecting other wallpapers
def replace_wallpaper():
    wallpaper_directory = "/usr/share/backgrounds"
    
    # Check if the wallpaper directory exists
    if os.path.exists(wallpaper_directory):
        # Replace the default wallpaper if it exists
        default_wallpaper_path = os.path.join(wallpaper_directory, "default.jpg")
        
        # Copy the new wallpaper to the default wallpaper location
        if os.path.exists(default_wallpaper_path):
            print(f"Replacing wallpaper: {default_wallpaper_path}")
            shutil.copy(wallpaper_path, default_wallpaper_path)

# Run functions to replace icons and wallpaper
replace_system_icons()
replace_wallpaper()

installSDAppStore = input("Would you like to install SDAppStore? (Y/N): ")
if installSDAppStore.lower() == "y":
  download_file("https://alexidians.github.io/SD-App-Store/SDAppStore.zip", "/SDLinux/apps_zip/SDAppStore/")
  extract_zip("/SDLinux/apps_zip/SDAppStore/", "/SDLinux/apps/SDAppStore")

print("SDLinux setup complete!")
