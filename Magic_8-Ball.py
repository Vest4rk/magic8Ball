import random
from time import sleep

def main():
    name = input('Who is there?: ')
    print('Hello, {name}\n'.format(name = name))
    while True:
        x = input('Do you want to ask a question? (Y / N): ')
        print('\n')
        if x == 'Y':
            question = input('What is your question?: ')
            answer = random_answer()
            if len(name) > 0:
                print('\n{name} asks: {question}'.format(name=name, question=question))
                sleep(1)
            else:
                print('Question: {question}'.format(name=name, question=question))
                sleep(1)

            print('Magic 8-Ball\'s answer: {answer}\n'.format(answer=answer))
            sleep(2)
            input('Press enter to continue. \n')

        elif x == 'y':
            question = input('What is your question?: ')
            answer = random_answer()
            if len(name) > 0:
                print('\n{name} asks: {question}'.format(name=name, question=question))
                sleep(1)
            else:
                print('Question: {question}'.format(name=name, question=question))
                sleep(1)

            print('Magic 8-Ball\'s answer: {answer}\n'.format(answer=answer))
            sleep(2)
            input('Press enter to continue. \n')

        else:
            print('Thank you for coming. Good luck...')
            break

def random_answer ():
    random_number = random.randint(1, 9)

    answers = ['Yes - definitely.', 'It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.',
              'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.',
              'Very doubtful.']

    answer_rand = answers[(random_number - 1)]

    return answer_rand

main()