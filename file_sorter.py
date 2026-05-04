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


def main():
    args = parse_arguments()
    source = Path(args.source)
    destination = Path(args.destination)

    print(f"Джерело     : {source}")
    print(f"Призначення : {destination}")


if __name__ == "__main__":
    main()
