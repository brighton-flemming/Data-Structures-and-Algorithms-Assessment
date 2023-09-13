def check_format(expression):

    valid_pairs = {"(" : ")", "[" : "]", "{" : "}"}

    stack = []

    for char in expression:
        if char in valid_pairs.keys():
            stack.append(char)
        elif char in valid_pairs.values():
            if not stack or valid_pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

expression1 = "([]{})"
expression2 = "([)]"
print(check_format(expression1))  
print(check_format(expression2))  
