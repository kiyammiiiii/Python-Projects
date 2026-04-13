def camel_to_snake(camel):
    snake = ""
    for char in camel:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

def main():
    camel_case = input("camelCase: ")
    print("snake_case:", camel_to_snake(camel_case))

main()
