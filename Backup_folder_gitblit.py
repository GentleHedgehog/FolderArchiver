#! python3
# it copies a folder to a backup folder and zips it

import shutil
import os
import zipfile
import errno, stat


def create_zip_from_folder(folder_path):
    print('begin to create the zip ({})'.format(folder_path))
    folder = os.path.basename(folder_path)
    zip_file_name = folder + '.zip'
    print('creating {}...'.format(zip_file_name))
    backup_zip = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)

    for folder_name, subfolders, file_names in os.walk(folder_path):
        print('adding files in {}..'.format(folder_name))
        for file_name in file_names:
            backup_zip.write(os.path.join(folder_name, file_name))

    backup_zip.close()
    print('creating the zip has done')


def deleter_for_file_with_access_error(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)


def delete_folder_if_exist(path_to_folder):
    if os.path.isdir(path_to_folder):
        print('dir "{0}" already exists, deleting..'.format(path_to_folder))
        shutil.rmtree(path_to_folder, onerror=deleter_for_file_with_access_error)


def create_temp_folder_stuff(path_to_folder):
    temp_nested_dir_name = 'temp_dir_nested'

    os.mkdir(path_to_folder)
    os.chdir(path_to_folder)
    file_1_level = open("file_1_level.txt", 'w')
    file_1_level.write('1 level')
    file_1_level.close()

    os.mkdir(temp_nested_dir_name)
    os.chdir(temp_nested_dir_name)
    file_2_level = open("file_2_level.txt", 'w')
    file_2_level.write('2 level')
    file_2_level.close()

    os.chdir('..')
    os.chdir('..')


if __name__ == '__main__':

    folder_name_origin = 'gitblit-1.6.2'
    folder_name_for_backup = 'gitblit-1.6.2_backup'
    folder_for_copy_zip_file = 'D:\\Archive_of_work'

    folder_path_origin = os.path.join(os.getcwd(), folder_name_origin)
    backup_folder_path = os.path.join(os.getcwd(), folder_name_for_backup)
    print("hello")
    print('we are in {0}'.format(os.getcwd()))
    print('we will work with  {0}'.format(folder_path_origin))

    print('deleting old backup folder...')
    delete_folder_if_exist(backup_folder_path)
    print('done')

    print('copying origin folder to backup folder...')
    shutil.copytree(folder_path_origin, backup_folder_path)
    print('done')

    # create_zip_from_folder(backup_folder_path)
    print('creating zip file...')
    archive_name = os.path.basename(backup_folder_path)
    shutil.make_archive(archive_name, 'zip', backup_folder_path)
    print('done')

    print('copying zip file to storage...')
    archive_src = os.path.join(os.getcwd(), archive_name + '.zip')
    shutil.copy(archive_src, folder_for_copy_zip_file)
    print('done')

    print('try to delete backup folder..')
    delete_folder_if_exist(backup_folder_path)
    print('done!')
    print('try to delete backup zip file..')
    try :
        os.remove(archive_src)
    except OSError:
        print('Exception: zip file "{}" is directory!: '.format(archive_src))
    else:
        print('done!')