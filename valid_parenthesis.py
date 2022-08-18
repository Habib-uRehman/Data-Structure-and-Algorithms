
def is_valid(s):
    while True:
        if '()' in s:
            s = s.replace('()', '')
        elif '{}' in s:
            s = s.replace('{}', '')
        elif '[]' in s:
            s = s.replace('[]', '')
        else:
            return not s


s = '[({)(())}]'


# print(is_valid(s))

def valid_paran(s):
    stack = []
    # Define opening brackets
    opening = set('([{')
    # Define closing brackets
    closing = set(')]}')
    # Create pairs. that ( must be paired with ) brace. i,e '(' : ')'
    pair = {')': '(', ']': '[', '}': '{'}
    # Loop through string
    for i in s:
        # If string is opening. push to stack
        if i in opening:
            stack.append(i)
        # If string is closing
        if i in closing:
            # first check whether stack is empty. i,e stack = [], and st is }, return false
            if len(stack) == 0:
                return False
            # else. check if popped st is paired. i,e { is } or not.
            elif stack.pop() != pair[i]:
                return False
            # If yes check for rest brackets
            else:
                continue
    # if all are paired and there are no elements left in stack return True.
    if len(stack) == 0:
        return True
    # return False if there were elements
    else:
        return False


print(valid_paran(s))
