import subprocess
import os

def download_files_with_names(url_list, output_names):
    with open(url_list, 'r') as url_file, open(output_names, 'r') as names_file:
        for url, custom_name in zip(url_file, names_file):
            url = url.strip()
            custom_name = custom_name.strip()

            # Full path to the output file
            output_file_path = os.path.join(custom_name)

            # Check if the file already exists
            if os.path.exists(output_file_path):
                print(f"File '{custom_name}' already exists. Skipping.")
                continue
            # Use curl to download the file and save it with the specified name
            subprocess.run(['curl', url, '-o', f"{custom_name}"])

if __name__ == "__main__":
    url_list = "./dl/url"
    output_names = "./dl/patch"
    
    download_files_with_names(url_list, output_names)

