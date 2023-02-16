from brain_games import logic


def is_even():
    logic.welcome()
    name = logic.user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        number = logic.random_number()
        answer = logic.check_number(number)
        print(f"Question: {number}")
        print("Your answer: ", end="")
        user_answer = logic.user_answer()

        if answer == user_answer:
            print("Correct!")
            i += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;/(. "
                + f"Correct answer was '{answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f"Congratulations, {name}!")
