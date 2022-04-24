#!/usr/bin/env python
from random import randint
import prompt


def question():
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    print('Your answer:',end=' ')
    answer = input()
    return (random_number % 2 == 0 and answer == 'yes') or (random_number % 2 != 0 and answer == 'no')


def is_even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    argument = question()
    i = 1
    while i < 3 and argument == True:
        print('Correct!')
        i = i + 1
        question()
    return print('Congratulations, ' + name + '!')


def main():
    is_even()


if __name__ == '__main__':
    main()

