import os
from pathlib import Path
import click
from .iso_handler import mount_iso, unmount_iso, get_list_of_iso, extract_and_zip


SOURCE_ISO_LOCATION = '/Users/v.pandey/Documents/DICOMS/test_images/'
MOUNT_FOLDER = os.path.join(str(Path.home()), 'temp_mount')
ZIP_DESTINATION = '/Users/v.pandey/Documents/DICOMS/zipped_dicoms/'


def main():
    """This is the entry point for the application.
    """
    # Get a list of ISOs present in the source folder.
    list_of_iso = get_list_of_iso(SOURCE_ISO_LOCATION)

    # Extract each ISO in Source ISO folder iteratively.
    for iso in list_of_iso:
        try:
            mount_iso(iso, MOUNT_FOLDER)
            extract_and_zip(MOUNT_FOLDER)

        except Exception as e:
            print(e.with_traceback())
            print("Failed!")

        finally:
            unmount_iso(MOUNT_FOLDER)


if __name__ == "__main__":
    main()
