class NumberInvalidError(Exception):
    """数字无效错误"""
    def __init__(self, data):
        Exception.__init__(self, data)
        self.data = data

    def __str__(self):
        return "'"+self.data+"' is a invalid number.Please input again."


def read_int_number(prompt):
    """读入大于等于0的整数"""
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                raise NumberInvalidError(str(number))
        except (ValueError, NumberInvalidError) as s:
            print(s)
        else:
            break
    return number


def read_float_number(prompt):
    """读入大于等于0的浮点数"""
    while True:
        try:
            number = float(input(prompt))
            if number < 0:
                raise NumberInvalidError(str(number))
        except (ValueError, NumberInvalidError) as s:
            print(s)
        else:
            break
    return number


def read_choice(choice_range):
    """读入选择序号直至输入正确"""
    read = True
    choice = None
    while read:
        choice = read_int_number("> ")
        if choice in choice_range:
            read = False
        else:
            print("Invalid option, please try again.")
    return choice


if __name__ == "__main__":
    x = read_int_number("Please enter a non negative integer:")
    y = read_float_number("Please enter a non negative floating-point number:")
    print(x)
    print(y)
    print("Please enter an option")
    print("1.OptionA 2.OptionB 3.OptionC")
    z = read_choice([1, 2, 3])
    print(z)
