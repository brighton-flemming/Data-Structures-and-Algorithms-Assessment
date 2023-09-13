def check_format(expression):

    valid_pairs = {"(" : ")", "[" : "]", "{" : "}"}

    stack = []

    for char in expression:
        if char in valid_pairs.keys():
            stack.append(char)
        elif char in valid_pairs.values():
            if not stack in valid_pairs[stack.pop()] != char:
                return False