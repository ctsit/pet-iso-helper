import os
import platform
import shutil
import pydicom
import datetime

def get_list_of_iso(mount_path):
    list_of_iso = []
    for file in os.listdir(mount_path):
        if file.endswith(".iso"):
            list_of_iso.append(os.path.join(mount_path, file))
    return list_of_iso


def mount_iso(iso_path, mount_path):
    os.system(f"mkdir {mount_path}")
    if platform.system() == 'Darwin':
        os.system(f"hdiutil mount -mountpoint {mount_path} {iso_path}")
    elif platform.system() == 'Linux':
        os.system(f"sudo mount -o loop {iso_path} {mount_path}")


def extract_and_zip(mount_path):
    dicom_folder_path, dicom_img = get_dicom(mount_path)
    zip_filename = determine_filename(dicom_folder_path, dicom_img)
    shutil.make_archive(zip_filename, 'zip', dicom_folder_path)
    print("Zipped Succesfully!")


def determine_filename(dicom_folder_path, dicom_img):
    img_path = os.path.join(dicom_folder_path, dicom_img)
    img = pydicom.read_file(img_path)
    formatted_study_date = datetime.datetime.strptime(img.StudyDate,'%Y%m%d').strftime('%m_%d_%Y')
    patient_name = img.PatientName
    filename = str(patient_name) + '_' + formatted_study_date
    ZIP_DESTINATION = '/Users/v.pandey/Documents/DICOMS/zipped_dicoms/'
    return ZIP_DESTINATION + filename


def get_dicom(mount_path):
    for curr_dir, child_dirs, files_list in os.walk(mount_path):
        if len(child_dirs) == 0:                
            return curr_dir, files_list[0]


def unmount_iso(mount_path):
    if platform.system() == 'Darwin':
        os.system(f"hdiutil unmount {mount_path}")
    elif platform.system() == 'Linux':
        os.system(f"sudo unmount {mount_path}")
    os.system(f"rmdir {mount_path}")

