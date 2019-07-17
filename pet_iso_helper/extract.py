import os
from pathlib import Path
import click
from subprocess import CalledProcessError
from .iso_handler import mount_iso, unmount_iso, get_list_of_iso, extract_and_zip


SOURCE_ISO_LOCATION = '/Users/v.pandey/Documents/DICOMS/test_images/'
MOUNT_FOLDER = os.path.join(str(Path.home()), 'temp_mount')
ZIP_DESTINATION = '/Users/v.pandey/Documents/DICOMS/zipped_dicoms/'


# Using click to get command line arguments
@click.command()
@click.argument('iso_source', required=True)
@click.argument('zip_destination', default=os.path.join(str(Path.home()), 'zipped_dicoms'))
def main(iso_source, zip_destination):
    """This program pulls the DICOM images from ISOs and creates a ZIP archive.
    """
    SOURCE_ISO_LOCATION = iso_source
    ZIP_DESTINATION = zip_destination + '/'

    # Get a list of ISOs present in the source folder.
    try:
        list_of_iso = get_list_of_iso(SOURCE_ISO_LOCATION)
    except Exception as e:
        click.echo(e.with_traceback())
        click.secho("Source Directory does not exist!", fg='red', bold=True, err=True)
        return

    # Extract each ISO in Source ISO folder iteratively.
    for iso in list_of_iso:
        try:
            mount_iso(iso, MOUNT_FOLDER)
            extract_and_zip(MOUNT_FOLDER, ZIP_DESTINATION)

        except CalledProcessError as e:
            click.echo(e.with_traceback(), err=True)
            click.secho(f"Could not mount ISO {iso}", fg='red', bold=True)
        except Exception as e:
            click.echo(e.with_traceback(), err=True)
            click.secho(f"Couldn't convert the ISO file at {iso} to ZIP!", fg='red', bold=True)

        finally:
            unmount_iso(MOUNT_FOLDER)

    click.secho(f"Zipped DICOM images are available at {ZIP_DESTINATION}", fg='yellow', bold=True)


if __name__ == "__main__":
    main()
