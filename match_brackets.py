bropen = ["[","{","("]
brclose = ["]","}",")"]

def is_bracket(item):
    return item in bropen or item in brclose

def check(expressionstr: str) -> bool:
    pending = []
    for character in expressionstr:
        if is_bracket(character):
            if character in bropen:
                pending.append(character)
            else:
                if len(pending) > 0:
                    if character == (brclose[bropen.index(pending[-1])]):
                        pending.pop()
                else:
                    return False
    else:  # nobreak
        return len(pending) == 0

if __name__ == "__main__":
    #false
    stringtomatch = "()}{()"
    print(f"Result is: {check(stringtomatch)}")

    #false
    stringtomatch1 = "{[help]{(me)]}"
    print(f"Result is: {check(stringtomatch1)}")

    #false
    stringtomatch2= "{[help[{(me)}}"
    print(f"Result is: {check(stringtomatch2)}")

    #true
    stringtomatch3 = "{[help]{(me)}}"
    print(f"Result is: {check(stringtomatch3)}")

    #false
    stringtomatch4 = "({m})}"
    print(f"Result is: {check(stringtomatch4)}")
