#!/usr/bin/env python
from random import randint
from random import choice
import prompt


def main_operation():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print_question = question()
    i = 1
    while i <=3:
        random_question = random_question()
        output_question = random_question[0]
        right_answer = random_question[1]
        print(f'Question: {output_question}')
        print('Your answer:', end=' ')
        answer = input()
        if answer != str(right_answer):
            return print('\'' + str(answer) + '\' is wrong answer ;\(. Correct answer was \'' + str(right_answer) + '\'.\nLet\'s try again, ' + name + '!')
        print('Correct!')
        i = i + 1
    return print('Congratulations, ' + name + '!')

if __name__ == '__main__':
    main()
