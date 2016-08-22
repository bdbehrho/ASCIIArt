# ASCIIArt
A python program to convert jpgs to text representations

## Overview
This program takes a jpg file, breaks the pixels into groups based on the char height and width variables, and then maps them to a character
of similar darkness. It then prints the characters to standard output. The result is a block of text that should look like the original image.
To use this program, change the path in the Image.open call to the image you would like to convert. Next you will want to adjust the char_height
and char_width variables (which are in units of pixels) to control how many characters are in the output. Now you can run the program. You will likely
want to redirect the output to a file so that it can be viewed more easily. 

Here is a link to an example output from my progam: [lena.txt](lena.txt)
