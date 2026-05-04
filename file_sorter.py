import argparse
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


def read_directory(source, destination):
    """Рекурсивно читає директорію та виводить всі файли."""
    try:
        for item in source.iterdir():
            if item.is_dir():
                print(f"  📁 Директорія: {item.name}")
                read_directory(item, destination)  # рекурсивний виклик
            elif item.is_file():
                print(f"  📄 Файл: {item.name}")
    except PermissionError:
        print(f"  ❌ Помилка доступу: {source}")
    except Exception as e:
        print(f"  ❌ Помилка: {e}")


def main():
    args = parse_arguments()
    source = Path(args.source)
    destination = Path(args.destination)

    print(f"Джерело     : {source}")
    print(f"Призначення : {destination}")

    if not source.exists() or not source.is_dir():
        print(f"❌ Директорія не існує: {source}")
        return

    print("\nСканування файлів:")
    read_directory(source, destination)


if __name__ == "__main__":
    main()