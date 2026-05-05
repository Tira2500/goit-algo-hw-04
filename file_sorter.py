import argparse
import shutil
from pathlib import Path


def parse_arguments():
    """Парсинг аргументів командного рядка."""
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання та сортування файлів за розширенням"
    )
    parser.add_argument(
        "source",
        type=str,
        help="Шлях до вихідної директорії"
    )
    parser.add_argument(
        "destination",
        type=str,
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення (за замовчуванням: dist)"
    )
    return parser.parse_args()


def copy_file(file_path, destination):
    """Копіює файл до піддиректорії за його розширенням."""
    extension = file_path.suffix.lstrip(".").lower()
    if not extension:
        extension = "no_extension"

    target_dir = destination / extension
    target_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(file_path, target_dir / file_path.name)
    print(f"  [OK] {file_path.name} -> {extension}/")


def read_directory(source, destination):
    """Рекурсивно читає директорію та копіює файли."""
    try:
        for item in source.iterdir():
            if item.is_dir():
                print(f"  [DIR]  {item.name}")
                read_directory(item, destination)
            elif item.is_file():
                copy_file(item, destination)
    except PermissionError:
        print(f"  [ERR] Помилка доступу: {source}")
    except Exception as e:
        print(f"  [ERR] Помилка: {e}")


def main():
    args = parse_arguments()
    source = Path(args.source)
    destination = Path(args.destination)

    print(f"Джерело     : {source}")
    print(f"Призначення : {destination}")

    if not source.exists() or not source.is_dir():
        print(f"[ERR] Директорія не існує: {source}")
        return

    destination.mkdir(parents=True, exist_ok=True)

    print("\nКопіювання файлів:")
    read_directory(source, destination)
    print("\n[DONE] Готово!")


if __name__ == "__main__":
    main()