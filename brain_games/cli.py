import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    answer = f"Hello, {name}"
    return answer

