def slot(coke_price):
    total = 0

    while total < coke_price:
        coin = int(input("Insert Coin: "))

        if coin in [5, 10, 25]:
            total += coin
            if total < coke_price:
                print(f"Amount Due: {coke_price - total}")
        else:
            print("Invalid coin.")

    if total > coke_price:
        print(f"Change Owed: {total - coke_price}")
    else:
        print(f"Amount Due: {coke_price - total}")

def main():
    coke_price = 50
    print(f"Amount Due: {coke_price}")
    slot(coke_price)

main()
