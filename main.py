import os
import shutil

directory = "Example"

try:
    os.mkdir(directory)
    print(f"'{directory}' directory created.")
except FileExistsError:
    print(f"A directory named '{directory}' already exists. Please enter a different name.")


subdirectory = os.path.join(directory, "Subdirect")

try:
    os.makedirs(subdirectory)
    print(f"'{subdirectory}' directory created inside '{directory}' directory.")
except FileExistsError:
    print(f"A subdirectory named '{subdirectory}' already exists inside '{directory}' directory.")


image = 'Lion.jpg'
image_path = os.path.join(os.getcwd(), image)

if os.path.exists(image_path):
    shutil.move(image_path, os.path.join(subdirectory, image))
else:
    print(f"Error! File not found: {image_path}")


text_path = os.path.join(subdirectory, 'text.txt')
with open(text_path, 'w', encoding='utf-8') as file:
    file.write("Success is the sum of small efforts repeated day in and day out.")

print(f"'text.txt' file added to '{subdirectory}' directory.")

for filename in os.listdir(subdirectory):
    if filename.endswith('.txt'):
        source_path = os.path.join(subdirectory, filename)
        destination_path = os.path.join(directory, filename)
        

        with open(source_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
        
        with open(destination_path, 'w', encoding='utf-8') as destination_file:
            destination_file.write(content)
        
        os.remove(source_path)
        
        print(f"'{filename}' file moved from '{subdirectory}' directory to '{directory}' directory.")