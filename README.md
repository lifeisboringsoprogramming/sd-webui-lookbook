<img src="images/webui.png" />

# Stable Diffusion Image 2 Video lookbook extension
A custom extension for [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) that create a video lookbook in different size from images with background music.

# Overview
* This project allows users to create a video lookbook from a set of images.
* With background music of their choice. 
* The output video can be saved to a specified folder. 
* Users can also specify the duration of each image clip.
* As well as the zoom effect factor for each image clip.
* Run as stable Diffusion extension inside the Stable Diffusion WebUI.
* Run as standalone application

# Tutorial
There is a video to show how to use the extension

[![How I Made 900 YouTube AI Lookbook Videos in 1 DAY for a Faceless YouTube Channel](https://img.youtube.com/vi/Ko-076NUCE8/sddefault.jpg)](https://www.youtube.com/watch?v=Ko-076NUCE8)

# Stable Diffusion extension
This project can be run as a stable Diffusion extension inside the Stable Diffusion WebUI.

## Installation for stable Diffusion extension
* Copy and paste `https://github.com/lifeisboringsoprogramming/sd-webui-img2lookbook.git` to URL for extension's git repository
* Press Install button
* Apply and restart UI when finished installing

<img src="images/webui-install.png" />

# Standalone application
This project can be run as a standalone application.

## Installation for standalone application
* `git clone https://github.com/lifeisboringsoprogramming/sd-webui-img2lookbook.git`
* `cd sd-webui-img2lookbook`
* `pip install -r requirements.txt`
* `python app.py`

<img src="images/gradio.png" />

# Bonus features
There are bonus features for Patreon supporters.
The bonus features include:
 * randomize images
 * make one video per seed from the source folder
 * match the duration of the images by the length of the music
 * background music fade out
 * background color selection
 * watermark overlay

<img src="images/bonus.png" />

☕️ Get the Patreon bonus features here 🍻
https://bit.ly/432RDIk


# Note
* The script will randomly choose an audio file found in the background music directory as the background music for the video.
* The output video format is mp4, and the output video size is determined by the size of the input images.
