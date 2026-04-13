import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        tries = 0
        while tries < 3:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    else:
        return random.randrange(100, 1000)


if __name__ == "__main__":
    main()
