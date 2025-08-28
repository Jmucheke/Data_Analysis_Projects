# Importing necessary libraries
import os, shutil

# Defining the path to the directory to be sorted
path = r"C:\Users\HP\Downloads/"

# Listing all files in the specified directory
file_name = os.listdir(path)

# Defining folder names for categorization
folders = ['images', 'documents', 'archives', 'datasets', 'code', 'others']

# update path to create a folder where the rest of the folders will be created
update_path = r"C:\Users\HP\Downloads/sortingfolder"
if not os.path.exists(update_path):
    os.mkdir(update_path)
    

for loop in range(len(folders)):
    folder_path = os.path.join(update_path, folders[loop])
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        
        
# Function to move files to respective folders
def move_files(file_name):
    for file in file_name:
        full_path = os.path.join(path, file)
        
        if not os.path.isfile(full_path):
            continue
        name, ext = os.path.splitext(file)

        ext = ext.lower()
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            shutil.move(full_path, os.path.join(update_path, 'images', file))
        elif ext in ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx']:
            shutil.move(full_path, os.path.join(update_path, 'documents', file))
        elif ext in ['.zip', '.rar', '.tar', '.gz']:
            shutil.move(full_path, os.path.join(update_path, 'archives', file))
        elif ext in ['.csv', '.json', '.xml', '.xlsx']:
            shutil.move(full_path, os.path.join(update_path, 'datasets', file))
        elif ext in ['.py', '.java', '.cpp', '.js', '.jsx', '.html', '.css']:
            shutil.move(full_path, os.path.join(update_path, 'code', file))
        else:
            shutil.move(full_path, os.path.join(update_path, 'others', file))
            
            
# call the function
move_files(file_name)