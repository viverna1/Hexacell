import os
import zipfile
import shutil
import subprocess

def archive_and_move(target_folder):
    # Получаем текущую рабочую папку
    current_dir = os.getcwd()
    folder_name = os.path.basename(current_dir)

    # Создаем имя архива с временной меткой
    archive_name = f"{folder_name}.zip"

    # Полный путь к архиву (временно сохраняем в текущей папке)
    temp_archive_path = os.path.join(current_dir, archive_name)

    # Создаем ZIP-архив, включая саму папку как корневую
    with zipfile.ZipFile(temp_archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(current_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Не архивируем сам создаваемый архив (чтобы избежать рекурсии)
                if file_path != temp_archive_path:
                    # arcname теперь включает имя папки
                    arcname = os.path.join(folder_name, os.path.relpath(file_path, current_dir))
                    zipf.write(file_path, arcname)

    # Проверяем, существует ли целевая папка, и создаем при необходимости
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Перемещаем архив в целевую папку, предварительно удаляя старый архив если он есть
    final_archive_path = os.path.join(target_folder, archive_name)
    if os.path.exists(final_archive_path):
        os.remove(final_archive_path)
    shutil.move(temp_archive_path, final_archive_path)

    print(f"Архив создан и перемещен в: {final_archive_path}")


# Укажите путь к целевой папке (можно абсолютный или относительный)
# target_folder = os.path.dirname(os.path.abspath(__file__))
target_folder = r"D:\Steam\steamapps\common\Mindustry\saves\mods"
archive_and_move(target_folder)

# Запуск игры
game_path = r"D:\Steam\steamapps\common\Mindustry\Mindustry.exe"
subprocess.Popen(game_path)  # Запускает игру