import random

def main():
    while True:
        try:
            num = int(input('Level: '))
            if num > 0:
                break
        except ValueError:
            pass
    number = random.randint(1,num)
    guess(number)

def guess(random_guess):
    while True:
        try:
            guess = int(input('Guess: '))
            if guess < 1:
                pass
            else:
                if guess == random_guess:
                    print('Just right!')
                    break
                elif guess > random_guess:
                    print('Too large!')
                else:
                    print('Too small!')
        except ValueError:
            pass



main()
