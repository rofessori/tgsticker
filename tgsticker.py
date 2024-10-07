import os
import sys
from PIL import Image

def main():
    # Get the folder to process from command-line argument or use current directory
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = '.'

    # Check if folder exists
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' does not exist.")
        sys.exit(1)

    # Create 'render' folder inside the specified folder
    render_folder = os.path.join(folder, 'render')
    if not os.path.exists(render_folder):
        os.makedirs(render_folder)

    # Process all PNG files in the folder
    for filename in os.listdir(folder):
        if filename.lower().endswith('.png'):
            filepath = os.path.join(folder, filename)
            # Open image
            with Image.open(filepath) as img:
                # Get original dimensions
                width, height = img.size
                
                # Calculate new dimensions to fit within 512x512 while maintaining aspect ratio
                if width > height:
                    new_width = 512
                    new_height = int((height / width) * 512)
                else:
                    new_height = 512
                    new_width = int((width / height) * 512)
                
                # Resize image
                img_resized = img.resize((new_width, new_height), resample=Image.LANCZOS)
                
                # Prepare new filename
                new_filename = '512x-' + filename
                new_filepath = os.path.join(render_folder, new_filename)
                
                # Save resized image
                img_resized.save(new_filepath)
                print(f"Processed {filename} -> {new_filename}")

if __name__ == '__main__':
    main()