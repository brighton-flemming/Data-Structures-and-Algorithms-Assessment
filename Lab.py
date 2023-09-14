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

def remove_duplicates(sequence):

    spotted = set()
    result = []

    for item in sequence:
        if item not in spotted:
            spotted.add(item)
            result.append(item)

    return result


input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]                                       

















































