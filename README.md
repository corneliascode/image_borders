# Borders of images 
##           Tip for Instagram

|Before                     | After                       |
|------------------------- | --------------------------- |
|![](input_images/picture.jpg) | ![](output_images/picture_processed.jpg)|

#### Introduction
- In this project I developed a function that creates border to the pictures (mainly for the Instagram).  
We know th issue of photos being cropped, so this script will resolve this issue.

#### Installation

- The libraries can be installed using the requirement file with the following code:  
```pip install requirements.txt```

#### Usage

- Can be used with any (JPG) photo or photos for which we want to create a border
- The code need to be run from the terminal and we should pass the color argument using the RGB format '[0,0,0]' - for each color you should pass a value from 0 ('no color') to 255 ('full color')

E.g.:  
```python main.py '[0,0,0]'```

#### Function Details

- Before running the function it is important to have in the same directory with the function: **input_images** (a folder which should contain image/s for which we want to create the borders) and __output_images__ (a folder which will contain the processed image/s)

- The function procces all images from the **input_images** folder
- All images should have the extension **'jpg'**. The script will ignore files with other extensions.



#### References 
Image used as the example from here: https://www.flickr.com/photos/respenda/53229010978/ (thank you!)
