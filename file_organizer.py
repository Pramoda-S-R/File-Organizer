import os
import shutil

path = os.path.expanduser('folder_path_here')

file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.gz', '.tar'],
    'Executables': ['.exe', '.msi'],
    'Others': []
}

if 'Others' not in file_categories:
    file_categories['Others'] = []

def file_category(filename):
    extension = os.path.splitext(filename)[1].lower()
    for category, extensions in file_categories.items():
        if extension in extensions:
            return category
    return 'Others'

def organize_downloads():
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            category = file_category(item)
            category_path = os.path.join(path, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            shutil.move(item_path, category_path)
            print(f'Moved {item} to {category}/')

if __name__ == '__main__':
    organize_downloads()
    print('Folder organized.')
