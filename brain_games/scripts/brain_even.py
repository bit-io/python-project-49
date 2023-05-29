import random


def main():
    print(start_game())
    name = input('May I have your name? ')
    print(f"Hello, {name}")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    count = []
    while True:
        answer, number = question()
        if answer == 'yes' and number %2 == 0:
            print('Correct!')
            count.append(answer)
        elif answer == 'no' and number %2 != 0:
            print('Correct!')
            count.append(answer)
        else:
            print(f"""'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!""")  
            break
        
        if len(count) > 3:
            print(f"Congratulations, {name}")
            break


def is_even(num):
    if num % 2 == 0:
        return True


def generate_number():
    return random.randint(0, 100)

def start_game():
    return """Welcome to the Brain Games!"""


def question():
    number = generate_number()
    print(f'Question: {number} ')
    answer = input(f'Your answer: ')
    return answer, number


if __name__ == '__main__':
    main()