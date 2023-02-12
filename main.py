# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1

    return "Success"


def main():
    input_type = input()
    if input_type == 'I':
        text = input()
    elif input_type == 'F':
        file_name = input()
        with open(file_name, 'r') as file:
            text = file.read()
    mismatch = find_mismatch(text)
    if isinstance(mismatch, int):
        print(mismatch)
    else:
        print("Success")


if __name__ == "__main__":
    main()
