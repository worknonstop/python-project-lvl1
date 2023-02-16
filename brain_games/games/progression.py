from brain_games import logic


def progression_game():
    logic.welcome()
    name = logic.user_name()
    print("What number is missing in the progression?")

    steps = [2, 4, 10]

    i = 0
    iter = 0
    while i < 3:
        step = steps[iter]
        new_list = logic.lst_progression(step)
        question_number = logic.mod_list(new_list)
        lst = str(question_number[0])
        question = logic.list_to_string(lst)
        answer = str(question_number[1])

        print("Question:", question)
        print("Your answer: ", end="")
        user_answer = logic.user_answer()

        if user_answer == answer:
            print("Correct!")
            i += 1
            iter += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;/(. "
                + f"Correct answer was '{answer}'."
            )
            print(f"Let's try again, {name}!")
            break

    if i == 3:
        print(f"Congratulations, {name}!")
