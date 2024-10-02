import os
import shutil
import zipfile
from datetime import datetime

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'db.sqlite3')  # Path to the database file
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')  # Directory to store backups

# Ensure the backup directory exists
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

# Create a timestamp for the backup file
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file = os.path.join(BACKUP_DIR, f'backup_{timestamp}.zip')

# Function to backup the SQLite database and other important files
def backup_data():
    try:
        # Create a zip file to store the backup
        with zipfile.ZipFile(backup_file, 'w') as backup_zip:
            # Add the SQLite database to the backup zip
            if os.path.exists(DB_FILE):
                backup_zip.write(DB_FILE, os.path.basename(DB_FILE))
                print(f'Added {DB_FILE} to backup.')
            else:
                print('No database file found.')

            media_folder = os.path.join(BASE_DIR, 'media')
            if os.path.exists(media_folder):
                for foldername, subfolders, filenames in os.walk(media_folder):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        backup_zip.write(file_path, os.path.relpath(file_path, BASE_DIR))
                print(f'Added media files to backup.')

        print(f'Backup successful: {backup_file}')
    except Exception as e:
        print(f'Error during backup: {e}')

if __name__ == '__main__':
    backup_data()
