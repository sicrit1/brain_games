#!/usr/bin/env python


from random import randint
import prompt


def question():
    return print('Answer \"yes\" if given number is prime. Otherwise answer \"no\"')


def random_question():
    n = randint(1, 100)
    i = n - 1
    while i > 1:
        if n % i == 0:
            return (n, 'no')
        i = i - 1
    return (n, 'yes')


def main_operation():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print_question = question()
    i = 1
    while i <=3:
        (x, y) = random_question()
        output_question = x
        right_answer = y
        print(f'Question: {output_question}')
        print('Your answer:', end=' ')
        answer = input()
        if answer != str(right_answer):
            return print('\'' + str(answer) + '\' is wrong answer ;\(. Correct answer was \'' + str(right_answer) + '\'.\nLet\'s try again, ' + name + '!')
            print('Correct!')
        i = i + 1
    return print('Congratulations, ' + name + '!')


def main():
    main_operation()


if __name__ == '__main__':
    main()
