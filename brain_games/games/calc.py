def calc_game():
    random_list = ["+", "*", "-"]
    random_operator = random.choice(random_list)
    if random_operator == "+":
        operation = addition()
    elif random_operator == "*":
        operation = multiplication()
    else:
        operation = subtraction()
    return operation
