from Question1 import *

def Infix_to_Postfix(expression):
    prec = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = Initialize(len(expression))
    letters = expression.split()
    output = []
    for i in letters:
        if i == "(":
            push(stack, i)
        elif i == ")":
            while True:
                b = pop(stack)
                if b == "(":
                    break
                else:
                    output.append(b)
        elif i in "+-*/":
            if top(stack) in "+-*/":
                if prec[top(stack)] >= prec[i]:
                    l = pop(stack)
                    output.append(l)
            push(stack, i)
        else:
            output.append(i)
    while is_empty(stack) == False:
        m = pop(stack)
        output.append(m)
    return ' '.join(output)




if __name__ == "__main__":
    print(Infix_to_Postfix("( A + B ) * ( C + D )"))
    # Should print "A B + C D + *"

    print(Infix_to_Postfix("A * B + C * D"))
    # Should print "A B * C D * +"

    print(Infix_to_Postfix("A * B + C"))
    # Should print "A B * C +"

    print(Infix_to_Postfix("A * ( B + C )"))
    # Should print "A B C + *"

    print(Infix_to_Postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    # Should print "A B + C * D E - F G + * -"
