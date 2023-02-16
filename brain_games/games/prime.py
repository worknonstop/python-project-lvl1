import random

from brain_games import logic


def is_prime_game():
    logic.welcome()
    name = logic.user_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0
    while i < 3:
        question = random.randint(1, 20)
        print(f"Question: {question}")
        print("Your answer: ", end="")
        user_answer = logic.user_answer()
        answer = logic.is_prime(question)

        if user_answer == answer:
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
