import os
import shutil

base_path = os.path.dirname(os.path.realpath(__file__))


def update_windows_updater():
    top_path = os.path.dirname(base_path)
    updater_path = os.path.join(base_path, ".ci/update_windows/update.py")
    bat_path = os.path.join(base_path, ".ci/update_windows/update_quasarui.bat")

    dest_updater_path = os.path.join(top_path, "update/update.py")
    dest_bat_path = os.path.join(top_path, "update/update_quasarui.bat")
    dest_bat_deps_path = os.path.join(top_path, "update/update_quasarui_and_python_dependencies.bat")

    try:
        with open(dest_bat_path, 'rb') as f:
            contents = f.read()
    except:
        return

    if not contents.startswith(b"..\\python_embeded\\python.exe .\\update.py"):
        return

    shutil.copy(updater_path, dest_updater_path)
    try:
        with open(dest_bat_deps_path, 'rb') as f:
            contents = f.read()
            contents = contents.replace(b'..\\python_embeded\\python.exe .\\update.py ..\\QuasarUI\\', b'call update_quasarui.bat nopause')
        with open(dest_bat_deps_path, 'wb') as f:
            f.write(contents)
    except:
        pass
    shutil.copy(bat_path, dest_bat_path)
    print("Updated the windows standalone package updater.")
