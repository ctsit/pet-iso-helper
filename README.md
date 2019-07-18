# pet-iso-helper

This is a command line utility to extract DICOM images from an ISO and create a zip archive of those images.

This program has only one required input - the SOURCE folder where the ISO's are located. The optional argument specifies the DESTINATION folder where user wants the ZIP archives to be stored. If destination is not provided, the ZIPs would be stored in the user's home directory in a folder by the name 'zipped_dicoms'.

## Installation

For installation, it is recommended that you create a virtual environment. Follow steps 1 through 5 to install.

If you do not wish to use a virtual environment, skip steps 3 and 4.

```sh
git clone <repo_url>  # Step 1: Clone the repository

cd /path/to/local/repo/     # Step 2: cd into the cloned repository

python3 -m venv .env    # Step 3: Create a virtual environment for project's dependencies

source .env/bin/activate    # Step 4: Activate the virtual environment.

pip install --editable .    # Step 5: Install the dependencies
```

## Usage

This package installs itself as a command-line utility. So, we don't need to invoke it with python. You simply use the following command:

```sh
pet-iso-helper <SOURCE_ISO_FOLDER> <ZIP_DESTINATION>
```

The script will automatically create a ZIP_DESTINATION folder if it doesn't already exist, and store the zipped dicoms in thats folder.

Or if you want to use just one argument:

```sh
pet-iso-helper <SOURCE_ISO_FOLDER>
```

This will store the zipped files at ~/zipped_dicoms/

## License

Apache 2: <http://www.apache.org/licenses/LICENSE-2.0>
