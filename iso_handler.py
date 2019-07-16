import os
import platform
import shutil
import pydicom
import datetime


def get_list_of_iso(mount_path):
    """Returns a list of iso files at the mount location passed as parameter

    Parameters:
        mount_path (str): The folder where ISOs are mounted

    Returns:
        list: A list of absolute pathnames of ISOs at the mount_path
    """
    list_of_iso = []
    for file in os.listdir(mount_path):
        if file.endswith(".iso"):
            list_of_iso.append(os.path.join(mount_path, file))
    return list_of_iso


def mount_iso(iso_path, mount_path):
    """Mounts the ISO at the path provided

    Parameters:
        iso_path (str): The absolute path pf folder where ISOs are stored
        mount_path (str): The absolute path pf folder where we want to mount the ISOs

    Returns:
        None
    """
    os.system(f"mkdir {mount_path}")
    if platform.system() == 'Darwin':
        os.system(f"hdiutil mount -mountpoint {mount_path} {iso_path}")
    elif platform.system() == 'Linux':
        os.system(f"sudo mount -o loop {iso_path} {mount_path}")


def extract_and_zip(mount_path):
    """Extracts the contents of passed ISO and zips it up

    Parameters:
        mount_path (str): The folder where ISOs are mounted

    Returns:
        None
    """
    dicom_folder_path, dicom_img = get_dicom(mount_path)
    zip_filename = determine_filename(dicom_folder_path, dicom_img)
    shutil.make_archive(zip_filename, 'zip', dicom_folder_path)
    print("Zipped Successfully!")


def determine_filename(dicom_folder_path, dicom_img):
    """Returns the formatted filename used to save the zip with.

    Parameters:
        mount_path (str): The folder where ISOs are mounted

    Returns:
        str: An absolute path for the zipped ISO
    """
    img_path = os.path.join(dicom_folder_path, dicom_img)
    img = pydicom.read_file(img_path)
    formatted_study_date = datetime.datetime.strptime(img.StudyDate, '%Y%m%d').strftime('%m_%d_%Y')
    patient_name = img.PatientName
    filename = str(patient_name) + '_' + formatted_study_date
    ZIP_DESTINATION = '/Users/v.pandey/Documents/DICOMS/zipped_dicoms/'
    return ZIP_DESTINATION + filename


def get_dicom(mount_path):
    """Recursively traverse the ISO file structure till we reach the folder having the DICOM images.

    Parameters:
        mount_path (str): The absolute path of the mounted ISO

    Returns:
        curr_dir: The directory inside the ISO that has all the DICOM images.
        files_list[0]: A sample image path to read patient's data from

    """
    for curr_dir, child_dirs, files_list in os.walk(mount_path):
        if len(child_dirs) == 0:
            return curr_dir, files_list[0]


def unmount_iso(mount_path):
    """Unmounts the ISO passed as the parameter.

    Parameters:
        mount_path (str): The absolute path of the mounted ISO

    Returns:
        None
    """
    if platform.system() == 'Darwin':
        os.system(f"hdiutil unmount {mount_path}")
    elif platform.system() == 'Linux':
        os.system(f"sudo unmount {mount_path}")
    os.system(f"rmdir {mount_path}")
