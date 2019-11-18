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
	
	counter = 1:
	
	path = '/Users/kenny/Desktop/PicHub/imgur/'
	dest_one = '/Users/kenny/Desktop/PicHub/frontend/static/h_images/fulls'
	dest_two = '/Users/kenny/Desktop/PicHub/frontend/static/h_images/thumbs'


	# Go through all 12 images 
	while counter != 13:
		
		source = ""

		# If counter is below 9
		if counter != 10: 
			source = path + "0" + str(counter) + ".jpg"
		else
			source = path + str(counter) + ".jpg"
		
		shutil.move(source, dest_one)
		
		counter++;


if __name__ == '__main__':
	moving_images()
