# Filename: update_home.py
# Author: Kenny Yu
# Description: Moving files from imgur folder into the static folder

# Import os module
import os

# Import shutil module
import shutil

# Function Name: moving_images
# Description: Moves images from imgur folder into static folder 
def moving_images(): 
	source = '/Users/kenny/Desktop/PicHub/imgur/*'
	dest_one = '/Users/kenny/Desktop/PicHub/frontend/static/h_images/fulls'
	dest_two = '/Users/kenny/Desktop/PicHub/frontend/static/h_images/thumbs'

	shutil.move(source, dest_one)

if __name__ == '__main__':
	moving_images()
