def main():
        try:
            equation = input("Fraction: ")
            x, y = equation.split("/")
            try:
                x = int(x)
                y = int(y)
                if y == 0 or x < 0 or y < 0 or x > y:
                    raise ZeroDivisionError
                compute = (x / y) * 100
                if compute >= 99:
                     print("F")
                elif compute <= 1:
                    print("E")
                else:
                    print(f"{compute:.0f}%")
            except ValueError:
                    main()
            except ZeroDivisionError:
                    main()
        except ValueError:
            main()


if __name__ == "__main__":    main()
