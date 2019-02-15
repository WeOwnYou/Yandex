def inside_check(test_expression):
    temp_expression = []
    for symbol_index in range(len(test_expression)):
        if test_expression[symbol_index] in inside_symbols:
            # try-catch
            for transposition in inside_symbols[test_expression[symbol_index]]:
                if(transposition == "/" and (test_expression[symbol_index-1]=='=' or symbol_index-1==0)):
                    continue
                temp_expression = test_expression[0: symbol_index] + transposition + test_expression[
                                                                                     symbol_index + 1:]
                if (expression_check(temp_expression)):
                    return temp_expression
                # print(temp_expression)

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
                            # print(temp_expression_2, "!")
                            if (expression_check(temp_expression_2)):
                                return temp_expression_2
    return 0


def expression_check(res_expression):  # приоритет, минус перед числом, 11ая степень
    expression_text1, expression_text2 = res_expression.split('=')
    expression1 = expression_builder(expression_text1)
    expression2 = expression_builder(expression_text2)
    # print(expression2, sep = "\n")
    # print(expression1, expression2)
    # print(count_value(expression1))
    if(count_value(expression1) == count_value(expression2)):
        return True
    else:
        return False

def count_value(expression):
    i = 0
    # print(len(expression), "!")
    while(len(expression)!=1):#мутно с индексом и
        # print("?")
        try:
            expression[i]
        except IndexError:
            i-=2
            continue
        # print(i)
        if(expression[i] == '*'):
            temp = expression[i-1] * expression[i+1]
            expression.insert(i,temp)
            expression.pop(i-1)
            expression.pop(i+1)
            expression.pop(i)
            i-=1
        elif (expression[i] == '/'):
            temp = (int)(expression[i - 1] / expression[i + 1])
            expression.insert(i, temp)
            expression.pop(i - 1)
            expression.pop(i + 1)
            expression.pop(i)
            i -= 1
        elif('*' not in expression and '/' not in expression):
            if (expression[i] == '+'):
                temp = expression[i-1] + expression[i+1]
                expression.insert(i, temp)
                expression.pop(i - 1)
                expression.pop(i + 1)
                expression.pop(i)
                i -= 1
            elif(expression[i] == '-'):
                temp = expression[i - 1] - expression[i + 1]
                expression.insert(i, temp)
                expression.pop(i - 1)
                expression.pop(i + 1)
                expression.pop(i)
                i -= 1
        # print(expression, "!")
        # print(expression, "!")
        i+=1
    return expression[0]

def expression_builder(res_expression):
    i = 0
    expression = []
    first_ind = -1
    while (True and len(res_expression)!=1):
        # print(i, len(res_expression))
        if i == 0:
            first_ind = i
        elif res_expression[i] in signs:
            expression.append(int(res_expression[first_ind:i]))
            expression.append(res_expression[i])
            first_ind = i+1
        i += 1
        if(i == len(res_expression)-1 ):
            # print(i, expression)
            expression.append(int(res_expression[first_ind:i+1]))
            return expression
    return [int(res_expression)]



# idef add_remove_check():
#     pass


add_match = {"0": ["8"], "1": ["7"], "3": ["9"], "5": ["6", "9"], "6": ["8"], "9": ["8"], "-": ["+"],
             "/": ["*"]}  # нет возможности для 2, 4, 7, 8, +, *
inside_symbols = {"0": ["9"], "2": ["3"], "3": ["5"], "4": ["11"], "5": ["3"], "6": ["9", "0"], "9": ["0", "6"],
                  "11": ["4"], "-": ["/"],
                  "/": ["-"]}
remove_match = {"6": ["5"], "7": ["1"], "8": ["0"], "9": ["5"], "+": ["-"], "*": ["/"], "-":[""]}  # нет 1,2,3,4,5(-)

signs = "+-*/="

# expression = input()
is_match_taken = False
is_match_placed = False
# print(expression_check("-1*2+3=-1+3*2*3"))
# expression = "-3+10=1"
for i in range(15):
    expression = input()
    a = inside_check(expression)
    if (a == 0):
        a = outside_check(expression)
    print(a)
