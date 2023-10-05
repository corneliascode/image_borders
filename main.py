# Function that creates the border for every image

# Import the libraries
import cv2
import os
import sys
import ast

INPUT_IMAGES_PATH = 'input_images'
OUTPUT_IMAGES_PATH = 'output_images'



# This function scans the specified folder and collects the names of all files
# found in that folder. It constructs the full path to each file and returns
# a list of these filenames. If the folder contains subdirectories, they are
# not included in the result; only the filenames in the top-level directory
# are considered.


def read_files_names_from_folder(input_folder_path: str) -> list:
    """Retrieve a list of filenames with full paths from a specified foder, folder names are ignored.

    Args:
        input_folder_path (str): The path to the folder from which filenames will be retrieved.

    Returns:
        list of str: A list of filenames, each represented as a full path.
    """
    files_names = []
    names = os.listdir(input_folder_path)
    for name in names:
      name_path = os.path.join(input_folder_path, name)
      is_file = os.path.isfile(name_path)
      if is_file:
          files_names.append(name_path)
    return files_names


# This function filter only the jpgs files and return a list
# of file names with that extension

def filter_jpgs(file_names: str) -> list:
    """ Filter only the jpgs files

    Parameters:
    file_names (str): name of the files

    Returns:
    list: a list of file names that have the '.jpg' extension.
    """
    return [file_name for file_name in file_names if file_name.split('.')[1] == 'jpg']


# This function takes the input_image path and remove everything after the '.' 
# using the split function in order to create the output_image_path
# using 'file_processed.jpg'

def create_output_path_from_input(image_path:str, output_folder_path:str):
    """ Creates the output_image_path where the processed image will be saved

    Args:
        image_path (str): input_images path
        output_folder_path (str): The path to the folder where the image will be saved

    Returns:
        str: the path where the modification will be saved
    """
    _, file = os.path.split(image_path)
    processed_file = '.'.join([file.split('.')[0] + '_processed', file.split('.')[1]])
    output_image_path = os.path.join(output_folder_path, processed_file)
    return output_image_path


# This function adds borders using the dimension_borders result and choose the color of that borders

def process_jpg(image_path:str, output_image_path:str, color:list):
    """Adds image border:
    # If height > width: adds borders in the top & bottom of the image
    # If height < width: adds borders in the left & right of the image

    Args:
        image_path (_type_): path to the unprocessed image
        output_image_path (_type_): the path where image will be saved
        color (list): accept only a list in the format RGB(red/green/blue)
    """
    img = cv2.imread(image_path)
    dimension_borders = int(abs((img.shape[0] - img.shape[1]) / 2))

    top = 0
    bottom = 0
    left = 0
    right = 0

    if img.shape[0] < img.shape[1]:
        top = dimension_borders
        bottom = dimension_borders
    elif img.shape[0] > img.shape[1]:
        left = dimension_borders
        right = dimension_borders

    imgage = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value = color)
    cv2.imwrite(output_image_path, imgage, [cv2.IMWRITE_JPEG_QUALITY, 100])
    return None

# This is the main function: it uses all the small functions above

def process_folder(border_color:list, input_folder_path = INPUT_IMAGES_PATH, output_folder_path = OUTPUT_IMAGES_PATH):
    """Incorporates all the above functions

    Args:
        border_color (list): accept only a list in the format RGB(red/green/blue)
        input_folder_path (_type_, optional): _description_. Defaults to INPUT_IMAGES_PATH.
        output_folder_path (_type_, optional): _description_. Defaults to OUTPUT_IMAGES_PATH.
    """

    files_paths = read_files_names_from_folder(input_folder_path)
    images_paths = filter_jpgs(files_paths)
    for image_path in images_paths:
        output_image_path = create_output_path_from_input(image_path, output_folder_path)
        process_jpg(image_path, output_image_path, border_color)

        
# The color should be passed as an argument using the format '[0,0,0]'

if __name__ == '__main__':
    border_color = ast.literal_eval(sys.argv[1])
    process_folder(border_color)
