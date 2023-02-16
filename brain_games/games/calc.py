from brain_games import logic


def calc_game():
    logic.welcome()
    name = logic.user_name()
    print("What is the result of the experssion?")

    i = 0
    while i < 3:
        question = eval(logic.random_question_calc())
        print(f"Question: {question}")
        user_answer = logic.user_answer()
        print(f"Answer: {user_answer}")
        if user_answer == str(question):
            print("Correct!")
            i += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;/(."
                + f"Correct answer was '{question}'"
            )
            print(f"Let's try again, {name}")
            break

    if i == 3:
        print(f"Congratulations, {name}")
