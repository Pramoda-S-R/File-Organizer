# Folder Organizer

This Python script automatically organizes your folder by sorting files into categorized subfolders based on their file types.

## Categories
Files are sorted into the following categories:
- Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`
- Documents: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
- Videos: `.mp4`, `.mov`, `.avi`, `.mkv`
- Music: `.mp3`, `.wav`, `.aac`, `.flac`
- Archives: `.zip`, `.rar`, `.7z`, `.gz`, `.tar`
- Executables: `.exe`, `.msi`
- Others: Files that don't match any of the above categories

## Usage
1. Ensure Python is installed on your system.
2. Modify `path` in the script to point to your folder.
3. Run the script: `python file_organizer.py`

The script will create subfolders in your folder for each category and move the files into their respective folders.

## Note
Always back up your files before running the script to prevent any unintended file movement or loss.
