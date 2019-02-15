def inside_check(test_expression):
    temp_expression = []
    for symbol_index in range(len(test_expression)):
        if test_expression[symbol_index] in inside_symbols:
            # try-catch
            for transposition in inside_symbols[test_expression[symbol_index]]:
                temp_expression = test_expression[0: symbol_index] + transposition + test_expression[
                                                                                     symbol_index + 1:]
                if (expression_check(temp_expression)):
                    return temp_expression

    return 0


def outside_check(test_expression):
    temp_expression_1 = []
    temp_expression_2 = []
    for symbol_index_1 in range(len(test_expression)):
        if test_expression[symbol_index_1] in remove_match:
            for transposition_1 in remove_match[test_expression[symbol_index_1]]:
                temp_expression_1 = test_expression[0:symbol_index_1] + transposition_1 + test_expression[
                                                                                          symbol_index_1 + 1:]
                for symbol_index_2 in range(len(test_expression)):
                    if temp_expression_1[symbol_index_2] in add_match:
                        for transposition_2 in add_match[temp_expression_1[symbol_index_2]]:
                            temp_expression_2 = temp_expression_1[
                                                0:symbol_index_2] + transposition_2 + temp_expression_1[
                                                                                      symbol_index_2 + 1:]
                            if (temp_expression_2 == test_expression):
                                continue
                            print(temp_expression_2, "!")
                            if (expression_check(temp_expression_2)):
                                return temp_expression_2
    return 0


def expression_check(res_expression):  # приоритет, минус перед числом, 11ая степень
    first_ind = -1
    expression1 = 0
    expression2 = 0
    signs_t = []
    numbers = []
    n = len(res_expression)
    for i in range(n):
        if first_ind == -1:
            first_ind = i
        if res_expression[i] in signs:
            if (i == 0 or i == res_expression.find('=') + 1):
                continue
            numbers.append(int(res_expression[first_ind:i]))
            signs_t.append(res_expression[i])
            first_ind = i + 1
            
    numbers.append(int(res_expression[first_ind:]))
    i = 0
    expression1 = numbers[i]
    while signs_t[i] != '=':
        if (signs_t[i] == '+'):
            expression1 += numbers[i + 1]
        elif (signs_t[i] == '*'):
            expression1 *= numbers[i + 1]
        elif (signs_t[i] == '-'):
            expression1 -= numbers[i + 1]
        elif (signs_t[i] == '/'):
            expression1 = (int)(expression1 / numbers[i + 1])
        i += 1
    i += 1
    expression2 = numbers[i]
    for sign in signs_t[i:]:
        if (sign == '+'):
            expression2 += numbers[i + 1]
        elif (sign == '-'):
            expression2 -= numbers[i + 1]
        elif (sign == '*'):
            expression2 *= numbers[i + 1]
        elif (sign == '/'):
            expression2 = (int)(expression2 / numbers[i + 1])
        i += 1
    if (expression1 == expression2):
        return True
    else:
        return False


# idef add_remove_check():
#     pass


add_match = {"0": ["8"], "1": ["7"], "3": ["9"], "5": ["6", "9"], "6": ["8"], "9": ["8"], "-": ["+"],
             "/": ["*"]}  # нет возможности для 2, 4, 7, 8, +, *
inside_symbols = {"0": ["9"], "2": ["3"], "3": ["5"], "4": ["11"], "5": ["3"], "6": ["9", "0"], "9": ["0", "6"],
                  "11": ["4"], "-": ["/"],
                  "/": ["-"]}
remove_match = {"6": ["5"], "7": ["1"], "8": ["0"], "9": ["5"], "+": ["-"], "*": ["/"], "-":[""]}  # нет 1,2,3,4,5

signs = "+-*/="

# expression = input()
is_match_taken = False
is_match_placed = False
# print(expression_check("-1=-1"))
expression = "3+10=-1"
# for i in range(15):
#     expression = input()
a = inside_check(expression)
if (a == 0):
    a = outside_check(expression)
#     print(a)
