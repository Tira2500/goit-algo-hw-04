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
    try:
        extension = file_path.suffix.lstrip(".").lower()
        if not extension:
            extension = "no_extension"

        target_dir = destination / extension
        target_dir.mkdir(parents=True, exist_ok=True)

        shutil.copy2(file_path, target_dir / file_path.name)
        print(f"  [OK] {file_path.name} -> {extension}/")

    except PermissionError:
        print(f"  [ERR] Немає доступу до файлу: {file_path.name}")
    except FileExistsError:
        print(f"  [SKIP] Файл вже існує: {file_path.name}")
    except Exception as e:
        print(f"  [ERR] Помилка копіювання {file_path.name}: {e}")


def read_directory(source, destination):
    """Рекурсивно читає директорію та копіює файли."""
    try:
        for item in source.iterdir():
            if item.is_dir():
                print(f"  [DIR] {item.name}")
                read_directory(item, destination)
            elif item.is_file():
                copy_file(item, destination)

    except PermissionError:
        print(f"  [ERR] Немає доступу до директорії: {source}")
    except Exception as e:
        print(f"  [ERR] Помилка читання директорії {source}: {e}")


def main():
    args = parse_arguments()
    source = Path(args.source)
    destination = Path(args.destination)

    print("=" * 50)
    print("  СОРТУВАННЯ ФАЙЛІВ ЗА РОЗШИРЕННЯМ")
    print("=" * 50)
    print(f"  Джерело     : {source}")
    print(f"  Призначення : {destination}")
    print("=" * 50)

    # Перевірка вихідної директорії
    if not source.exists():
        print(f"[ERR] Директорія не існує: {source}")
        return
    if not source.is_dir():
        print(f"[ERR] Це не директорія: {source}")
        return

    # Створення директорії призначення
    try:
        destination.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print(f"[ERR] Немає прав для створення: {destination}")
        return
    except Exception as e:
        print(f"[ERR] Помилка створення директорії: {e}")
        return

    # Рекурсивне копіювання
    print("\n  Копіювання файлів:")
    read_directory(source, destination)

    # Підсумок
    print("\n" + "=" * 50)
    subdirs = [d.name for d in destination.iterdir() if d.is_dir()]
    print(f"  Створено піддиректорій : {len(subdirs)}")
    print(f"  Типи файлів: {', '.join(sorted(subdirs))}")
    print("  [DONE] Готово!")
    print("=" * 50)


if __name__ == "__main__":
    main()