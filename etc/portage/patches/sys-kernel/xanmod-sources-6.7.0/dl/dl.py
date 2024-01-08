import subprocess
import os

def download_files_with_names(url_list, output_names, log_file):
    # Check if the number of lines in both files match
    with open(url_list, 'r') as url_file, open(output_names, 'r') as names_file, open(log_file, 'a') as log:
        urls = url_file.readlines()
        names = names_file.readlines()

        if len(urls) != len(names):
            log.write("Error: The number of URLs and custom names don't match.\n")
            return

        for url, custom_name in zip(urls, names):
            url = url.strip()
            custom_name = custom_name.strip()

            # Ignore lines starting with #
            if url.startswith('#') or custom_name.startswith('#'):
                continue

            # Full path to the output file
            output_file_path = os.path.join("./", custom_name)

            # Check if the file already exists
            if os.path.exists(output_file_path):
                log.write(f"File '{custom_name}' already exists. Skipping.\n")
                continue

            # Use curl to download the file and save it with the specified name
            subprocess.run(['curl', url, '-s', '-o', output_file_path])

            # Write download information to the log file
            log.write(f"Downloaded '{custom_name}' from '{url}'\n")

if __name__ == "__main__":
    url_list = "./dl/url"
    output_names = "./dl/patch"
    log_file = "./dl/download_log.txt"

    download_files_with_names(url_list, output_names, log_file)

