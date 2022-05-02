#!/usr/bin/env python
from random import randint
from random import choice
import prompt


def summ():
    a = randint(1, 100)
    b = randint(1, 100)
    return ((a + b), str(a) + ' + ' + str(b))


def sub():
    c = randint(1, 100)
    d = randint(1, 100)
    return ((c - d), str(c) + ' - ' + str(d))


def div():
    e = randint(1, 100)
    f = randint(1, 100)
    return ((e * f), str(e) + ' * ' + str(f))


def random_operation():
    x = summ()
    y = sub()
    z = div()
    list = [x, y, z]
    return choice(list)


def question():
    return print('What is the result of the expression?')


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
        random_question = random_operation()
        output_question = random_question[1]
        right_answer = random_question[0]
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
