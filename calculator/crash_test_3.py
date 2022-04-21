"""
Operator's precedence:
() - brace, brackets
** - exponentiating
+x, -x, ~x - унарный плюс, минус и битовое отрицание
*, /, //, % - multiplication, division, взятие остатка
+, -, - addition, difference
"""




operators = ["(",")","*","/","*","+","-"]
numbers = []
position = []

def brackets(a):
    num_in_brackets = []
    pos_in_brackets = []
    pos_of_brackets = []
    n = 0
    for i in a:
        if i in ["(",")"]:
            pos_of_brackets.append(n)
        n = n + 1
    print(pos_of_brackets)
    return (num_in_brackets,pos_in_brackets)
def addition(a):
    c = a + b
    return c

def difference(a):
    c = a - b
    return c

def division(a):
    if b != 0:
        c = a/b
        return c
    else :
        print("Can't divide by zero")

def multiplication(a):
    c = a*b
    return c

def how_many_signs():
    a = input()
    n = 0
    left_brackets, right_brackets = [],[]
    multiplication,division = [],[]
    addition,difference = [],[]
    for i in a:
        if i in operators:
            if i == "(":
                left_brackets.append(n)
            if i == ")":
                right_brackets.append(n)
            if i == "+":
                addition.append(n)
            if i == "-":
                difference.append(n)
            if i == "/":
                division.append(n)
            if i == "*":
                multiplication.append(n)
        position.append(n)
        n = n + 1
    pos_of_signs = {
        "left_brackets - '(' ": left_brackets,
        "right_brackets - ')' ": right_brackets,
        "multiplication - '*' ": multiplication,
        "division - '/' ": division,
        "addition - '+' ": addition,
        "difference - '-' ": difference
    }
    #print(f' "(" - {left_brackets}\n ")" - {right_brackets}\n "*" - {multiplication}\n "/" - {division}\n "+" - {addition}\n "-" - {difference}')
    #print(pos_of_signs, "\n", which_pos_has_number(a), "\n", which_pos_has_signs(a),"\n", numbers)
    print(brackets(a))
    return (a, pos_of_signs, which_pos_has_number(a))

def which_pos_has_number(a):
    pos_of_num = []
    n = 0
    for i in a:
        if i.isdigit() == True:
            pos_of_num.append(n)
            num = int(i)
            numbers.append(num)
        n = n+1
    return pos_of_num

def which_pos_has_signs(a):
    pos_of_signs = []
    n = 0
    for i in a:
        if i in operators:
            pos_of_signs.append(n)
        n = n + 1
    return pos_of_signs

def main():
    how_many_signs()


if __name__ == "__main__":
    brackets(input())