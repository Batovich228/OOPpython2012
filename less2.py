import os
import datetime

def collector(path, res_path):
    res_path = os.path.normpath(res_path)
    path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_time = os.path.getmtime(os.path.join(dirpath, file))
            datetime_file = datetime.datetime.fromtimestamp(file_time)
            file_date = datetime_file.strftime("%d.%m.%Y")
            destination_folder = os.path.join(res_path, file_date)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            os.replace(os.path.join(dirpath, file), os.path.join(destination_folder, file))
