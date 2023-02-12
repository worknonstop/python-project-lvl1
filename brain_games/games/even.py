import random

from logic import hello_name, prompt, user_name, welcome


def is_even():
    welcome()
    name = user_name()
    hello_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wrong_no = "'no' is wrong answer ;/(. Correct answer was 'yes'"
    wrong_yes = "'yes' is wrong answer ;/(. Correct answer was 'no'"

    i = 0
    while i < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("")
        no_answer = user_answer == "no"
        yes_answer = user_answer == "yes"
        even_number = number % 2 == 0
        uneven_number = number % 2 != 0
        print(f"Answer: {user_answer}")

        if even_number and no_answer:
            print(wrong_no)
            print(f"Let's try again, {name}")
            break
        elif uneven_number and yes_answer:
            print(wrong_yes)
            print(f"Let's try again, {name}")
            break
        elif (even_number and yes_answer) or (uneven_number and no_answer):
            print("Correct!")
            i += 1
        else:
            print(f"Let's try again, {name}")
            break

        if i == 3:
            print(f"Congratulations, {name}!")
        else:
            print(f"Let's try again, {name}")
