import turtle
import argparse


def parse_arguments():
    """Парсинг аргументів командного рядка."""
    parser = argparse.ArgumentParser(
        description="Сніжинка Коха — фрактал з рекурсією"
    )
    parser.add_argument(
        "level",
        type=int,
        help="Рівень рекурсії (наприклад: 0, 1, 2, 3, 4)"
    )
    parser.add_argument(
        "--size",
        type=int,
        default=300,
        help="Розмір сніжинки (за замовчуванням: 300)"
    )
    return parser.parse_args()


def koch_curve(t, level, size):
    """Рекурсивно малює криву Коха."""
    if level == 0:
        t.forward(size)
        return

    size /= 3
    koch_curve(t, level - 1, size)
    t.left(60)
    koch_curve(t, level - 1, size)
    t.right(120)
    koch_curve(t, level - 1, size)
    t.left(60)
    koch_curve(t, level - 1, size)


def draw_snowflake(level, size):
    """Малює сніжинку Коха — три криві Коха."""
    screen = turtle.Screen()
    screen.title(f"Сніжинка Коха — рівень {level}")
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan")
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, level, size)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


def main():
    args = parse_arguments()

    if args.level < 0:
        print("[ERR] Рівень рекурсії не може бути від'ємним!")
        return
    if args.level > 6:
        print("[WARN] Рівень > 6 може займати багато часу для малювання.")

    print(f"Малюємо сніжинку Коха рівня {args.level}...")
    draw_snowflake(args.level, args.size)


if __name__ == "__main__":
    main()
