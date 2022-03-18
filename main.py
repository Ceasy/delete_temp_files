from __future__ import print_function
import ctypes, sys

import os
import os.path
import sys
import shutil
import getpass


from pathlib import Path


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# def change_permissions_recursive(path, mode):
#     for root, dirs, files in os.walk(path, topdown=False):
#         for dir in [os.path.join(root, d) for d in dirs]:
#             os.chmod(dir, mode)
#     for file in [os.path.join(root, f) for f in files]:
#         os.chmod(file, mode)
#
#
# change_permissions_recursive('c:/Users/1/AppData/Roaming/Microsoft/Excel', 0o777)

def path_user(main_path):
    for filename in os.listdir(main_path):
        file_path = os.path.join(main_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete file %s. Reason: %s" % (file_path, e))


def search_path(users):
    for user in users:
        check_folder = os.path.exists(rf'C:/Users/{user}/AppData/Roaming/Microsoft/Excel')
        if user == '1':
            if check_folder:
                folder = rf'C:/Users/{user}/AppData/Roaming/Microsoft/Excel'
                path_user(folder)
            else:
                print('no found...')
        else:
            if check_folder:
                folder = rf'C:/Users/{user}/AppData/Roaming/Microsoft/Excel'
                print(f'user = {user}')
                path_user(folder)


def main():
    user_name = getpass.getuser()

    users = [
        x.name for x in Path(r'C:\Users').glob('*') if x.name not in [
            'Default', 'Default User', 'Public', 'All Users', 'DTore', 'print', 'Все пользователи'
        ] and x.is_dir()
    ]

    search_path(users)

    # if is_admin():
    #     # Добавьте код для запуска здесь
    #     search_path(users)
    # else:
    #     if sys.version_info[0] == 3:
    #         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    #     else:  # in python2.x
    #         ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
