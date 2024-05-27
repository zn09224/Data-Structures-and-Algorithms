from Question1 import *

def balanced_braces(s):
    brackets = {")": "(", "}": "{", "]": "["}
    stack = Initialize(len(s))
    for i in s:
        if i in "({[":
            push(stack, i)
        if i in ")}]":
            if is_empty(stack) == True:
                return False
            else:
                b = pop(stack)
                if brackets[i] == b:
                    pass
                else:
                    return False
    return True



if __name__ == "__main__":
    print(balanced_braces("()"))
    # Should print "True"

    print(balanced_braces("())"))
    # Should print "False"

    print(balanced_braces("{()}"))
    # Should print "True"

    print(balanced_braces("{)({"))
    # Should print "False"

    print(balanced_braces("{()}[]()"))
    # Should print "True"

    print(balanced_braces("{[}]"))
    # Should print "False"