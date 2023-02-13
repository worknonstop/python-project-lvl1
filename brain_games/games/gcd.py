from brain_games import logic


def gcd_game():
    logic.welcome()
    name = logic.user_name()
    print("Find greatest common divisor of given numbers.")

    i = 0
    while i < 3:
        num1 = logic.random_number()
        num2 = logic.random_number()
        result = logic.gcd(num1, num2)
        user_answer = logic.user_answer()
        print(f"Question: {num1} {num2}")
        print(f"Answer: {user_answer}")

        if int(user_answer) == result:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;/(."
                + f" Correct answer was '{result}'"
            )
            print(f"Let's try again, {name}")
            break

    if i == 3:
        print(f"Congratulations, {name}")
