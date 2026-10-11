# answer 1:
def infix_to_postfix(expression):
    stack = []
    postfix = []

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    for ch in expression:
        if ch.isalnum():
            postfix.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[ch] or
                   (precedence[stack[-1]] == precedence[ch]
                    and ch != '^'))):
                postfix.append(stack.pop())

            stack.append(ch)

    while stack:
        postfix.append(stack.pop())

    return ' '.join(postfix)


expression = input("Enter infix expression: ")
result = infix_to_postfix(expression)

print("Postfix expression:", result)

#Answer 2:

def evaluate_postfix(expression):
    stack = []

    for ch in expression.split():
        if ch.isdigit():
            stack.append(int(ch))

        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a // b)

    return stack.pop()


expression = input("Enter postfix expression: ")

result = evaluate_postfix(expression)

print("Final Result:", result)
