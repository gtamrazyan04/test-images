import os

def rename_images_in_subfolders(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        if foldername == root_folder:
            continue  # skip the root folder itself

        image_count = 1
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            new_name = f"{os.path.basename(foldername)}_{image_count}.png"
            new_path = os.path.join(foldername, new_name)

            # Avoid overwriting by checking if new_path exists
            if not os.path.exists(new_path):
                os.rename(file_path, new_path)
                image_count += 1
            else:
                print(f"Skipped {file_path} — {new_path} already exists.")

# Replace this with your actual path
folder_path = "/Users/gt/Documents/ETH/6.Semester/capturecore/images"
rename_images_in_subfolders(folder_path)
