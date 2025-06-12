import os
import shutil

target_folder = input("Please enter the directory: ")


mapping = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'videos': ['.mp4', '.mov', '.avi'],
    'audio': ['.mp3', '.wav'],
    'archives': ['.zip', '.rar', '.tar', '.gz']
}

def get_category(extension):
    for category, extensions in mapping.items():
        if extension.lower() in extensions:
            return category
    return 'others'

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        if not ext:
            continue

        category = get_category(ext)
        category_folder = os.path.join(folder_path, category)

        os.makedirs(category_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(category_folder, filename))
        print(f"Moved {filename} to {category_folder}/")

    if __name__ == '__main__':
        organize_files(target_folder)
        print("All done! ")