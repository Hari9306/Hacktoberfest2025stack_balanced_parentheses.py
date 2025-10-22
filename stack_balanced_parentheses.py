def is_balanced(expr):
    stack = []
    for char in expr:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and char == ']') or \
               (top == '[' and char == '}') or \
               (top == '{' and char == ')'):  # ❌ Wrong match pairs
                return False
    return len(stack) == 0

print(is_balanced("{[()]}"))  # Expected True
