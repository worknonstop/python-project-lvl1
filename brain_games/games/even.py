from brain_games import logic


def is_even():
    logic.welcome()
    name = logic.user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        number = logic.random_number()
        print(f"Question: {number}")
        user_answer = logic.user_answer()

        if logic.check_number(number) == user_answer:
            print("Correct!")
            i += 1
        else:
            print(
                f"{user_answer} is wrong answer ;/(."
                + f"Correct answer was {logic.check_number()}"
            )
            print(f"Let's try again, {name}")
            break
    if i == 3:
        print(f"Congratulations, {name}")
