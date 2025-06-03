# 🖼️ CrowPanel ESP32 2.9” PNG to txt.bin Converter

## 📦 Requirements
Ensure Python 3 is installed and the following packages are available:
```
brew install python
brew install pillow numpy
```
✅ If you've installed Pillow and NumPy via brew or pip, you're good to go.

### Works best with [CrowPanel ESP32 2.9" nametag firmware](https://github.com/MariusQuabeck/CrowPanel-ESP32-2.9-inch-nametag-firmware/tree/main)

## 📁 Files
binner.py – The converter script.

Your_image.png – A black and white 296 × 128 px PNG (the script will convert automatically).

Output: txt.bin – Ready-to-upload binary file.
### Make sure to flip it horizontally for it to be displayed correctly, step will be included in the script at some point

## 🚀 Usage
1. Place your image in the same folder as the script
Your image should be 296x128 pixels or it will be scaled and centered automatically.
FLIP IT HORIZONTALLY for now, will be included in the script later

2. Run the script
```
python3 binner.py my_nametag.png
```
The script will output ```txt.bin``` in the current directory.

3. Upload to your CrowPanel
Connect to the CrowPanel’s ESP32_Config Wi-Fi network.

Open a browser and go to http://192.168.4.1/

Upload txt.bin via the form.

The screen should update automatically.

## 🔧 How it Works
Resizes your PNG proportionally to fit 296x128

Converts it to 1-bit black/white

Centers it on a white canvas

Converts to vertical bit-packed column-major format (8 pixels per byte)

Bits are reversed per byte to fix orientation quirks

Saves as a raw .bin file suitable for display

## 🧼 Tips
White areas in the image become background.

Make sure your image is legible in black/white for best results.

Use high contrast text and avoid gradients.
