import os
import datetime

def collector(path, res_path):
    res_path = os.path.normpath(res_path)
    path = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_time = os.path.getmtime(file_path)
            datetime_file = datetime.datetime.fromtimestamp(file_time)
            file_date = datetime_file.strftime("%d.%m.%Y")
            target_dir = os.path.join(res_path, file_date)
            if not os.path.isdir(target_dir):
                os.makedirs(target_dir)  # Створюємо каталог, якщо його не існує
            try:
                os.replace(file_path, os.path.join(target_dir, file))
            except Exception as e:
                print(f"Помилка при переміщенні файлу {file}: {e}")

path = "D:/Web"
res_path = "D:/agent_data"
collector(path, res_path)
