import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        # Check if source exists
        if not os.path.isdir(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' not found.")
        
        # Check if destination exists
        if not os.path.isdir(dest_dir):
            raise FileNotFoundError(f"Destination directory '{dest_dir}' not found.")

        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)

            if os.path.isfile(source_file):
                dest_file = os.path.join(dest_dir, filename)

                # Check for duplicate and rename with timestamp
                if os.path.exists(dest_file):
                    base, ext = os.path.splitext(filename)
                    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                    new_filename = f"{base}_{timestamp}{ext}"
                    dest_file = os.path.join(dest_dir, new_filename)

                shutil.copy2(source_file, dest_file)
                print(f"Copied: {filename} -> {dest_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]
    backup_files(source, destination)