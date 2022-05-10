#!/usr/bin/env python
from random import randint
import prompt


def random_number():
    x = randint(1, 100)
    y = randint(1, 100)
    return (x, y)


def gcd(x, y):
    if x > y:
        i = y
        while i > 0:
            if x % i == 0 and y % i == 0:
                return i
            i = i - 1
    else:
        i = x
        while i > 0:
            if x % i == 0 and y % i == 0:
                return i
            i = i - 1


def question():
    return print('Find the greatest common divisir of given numbers.')


def greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def main_operation():
    name = greeting()
    question()
    i = 1
    while i <= 3:
        (x, y) = random_number()
        right_answer = gcd(x, y)
        print(f'Question: {x} {y}')
        print('Your answer:', end=' ')
        answer = input()
        if answer != str(right_answer):
            return print(f"""\"{str(answer)}\" is wrong answer ;(. \
Correct answer was \"{str(right_answer)}\"
Let\'s try again, {name}!""")
        print('Correct!')
        i = i + 1
    return print('Congratulations, ' + name + '!')


def main():
    main_operation()


if __name__ == '__main__':
    main()
