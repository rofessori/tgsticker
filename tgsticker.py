import os
import sys
from PIL import Image

def main():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = '.'

    if not os.path.isdir(folder):
        print(f"Folder '{folder}' does not exist.")
        sys.exit(1)

    # processed images will be added to a new new directory "render"
    render_folder = os.path.join(folder, 'render')
    if not os.path.exists(render_folder):
        os.makedirs(render_folder)

    # !! This will process ALL the images in the folder where the script is being executed from
    for filename in os.listdir(folder):
        if filename.lower().endswith('.png'):
            filepath = os.path.join(folder, filename)
            # ge timg
            with Image.open(filepath) as img:
                # og dimensions
                width, height = img.size
                
                if width > height:
                    new_width = 512
                    new_height = int((height / width) * 512)
                else:
                    new_height = 512
                    new_width = int((width / height) * 512)
                
                #resize and name
                img_resized = img.resize((new_width, new_height), resample=Image.LANCZOS)
                new_filename = '512x-' + filename
                new_filepath = os.path.join(render_folder, new_filename)
                #save
                img_resized.save(new_filepath)
                print(f"Processed {filename} -> {new_filename}")

if __name__ == '__main__':
    main()
