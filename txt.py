import os

def save_dart_files_to_txt(lib_folder):
    """
    Traverses through all subfolders inside the lib folder, reads .dart files,
    and stores their contents into:
      1. A folder-specific .txt file (one for each subfolder).
      2. A single consolidated .txt file containing all .dart files.

    Args:
        lib_folder (str): Path to the lib folder.
    """
    # Check if the lib folder exists
    if not os.path.exists(lib_folder):
        print(f"The folder '{lib_folder}' does not exist.")
        return

    # Consolidated text file for all dart files
    consolidated_file_path = os.path.join(lib_folder, "all_dart_files.txt")
    with open(consolidated_file_path, 'w', encoding='utf-8') as consolidated_file:
        print("Creating consolidated file for all .dart files...")

        # Iterate through all subdirectories in the lib folder
        for root, dirs, files in os.walk(lib_folder):
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                folder_txt_file_path = os.path.join(lib_folder, f"{folder}.txt")
                
                print(f"Processing folder: {folder}")
                
                # Collect all .dart files in the folder
                dart_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.dart')]
                if not dart_files:
                    print(f"No .dart files found in '{folder_path}'. Skipping...")
                    continue

                # Write contents to the folder-specific .txt file
                with open(folder_txt_file_path, 'w', encoding='utf-8') as folder_txt_file:
                    for dart_file in dart_files:
                        with open(dart_file, 'r', encoding='utf-8') as file:
                            content = file.read()
                            # Write to folder-specific text file
                            folder_txt_file.write(f"--- Content of {os.path.basename(dart_file)} ---\n")
                            folder_txt_file.write(content)
                            folder_txt_file.write("\n\n")

                            # Write to the consolidated file
                            consolidated_file.write(f"--- Content of {os.path.basename(dart_file)} in folder {folder} ---\n")
                            consolidated_file.write(content)
                            consolidated_file.write("\n\n")

                print(f"Contents of .dart files in '{folder}' saved to '{folder_txt_file_path}'.")

    print(f"All .dart files combined and saved to '{consolidated_file_path}'.")

if __name__ == "__main__":
    # Path to the lib folder
    lib_folder = "/Users/rupinajay/Developer/ReLeaf/releaf_final/releaf/lib"  # Update this path if necessary
    save_dart_files_to_txt(lib_folder)
