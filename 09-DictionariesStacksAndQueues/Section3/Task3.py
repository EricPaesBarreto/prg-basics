import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

brackets_dict = {
    ")":"(",
    "]":"[",
    "}":"{"
}

def brackets_ok(expression):
    brackets = queue.LifoQueue()
    for char in expression:
        match char:
            case "(" | "[" | "{":
                brackets.put(char)
            case ")" | "]" | "}":
                if brackets.empty():
                    return False
                else:
                    if brackets.get() != brackets_dict[char]:
                        return False
    if not brackets.empty(): return False
    return True

def test_expressions(expressions):
    test_results = ""
    for expression in expressions:
        test_results += expression
        test_result = brackets_ok(expression)
        test_results += f"   :   Passed: {test_result}\n"
    return test_results

if __name__ == "__main__":
    expressions = [expression1, expression2, expression3]
    print(test_expressions(expressions))