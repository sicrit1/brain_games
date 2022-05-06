#!/usr/bin/env python


from random import randint
from random import choice
import prompt


def progression(a, d, k):
    i = 0
    prog = [a]
    for i in range(k):
        Q = a + d
        prog = prog + [Q]
        a = Q
    return prog


def random_arg():
    a = randint(1, 100)
    d = randint(1, 10)
    k = randint(5, 10)
    return (a, d, k)


def question():
    return print('What number is missing in the progression?')


def random_question():
    (a, d, k) = random_arg()
    prog = progression(a, d, k)
    n = randint(0, k - 1)
    s = prog[n]
    prog[n] = ".."
    return (" ".join(map(str, prog)), s)


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
