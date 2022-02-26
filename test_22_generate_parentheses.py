from code_22_generate_parentheses import Solution

def test_example_1():
    s = Solution()
    n = 3
    output = ["((()))","(()())","(())()","()(())","()()()"]
    assert sorted(s.generateParenthesis(n)) == sorted(output)

def test_example_2():
    s = Solution()
    n = 1
    output = ['()']
    assert s.generateParenthesis(n) == output

def test_example_3():
    s = Solution()
    n = 4
    output = [
        "(((())))","((()()))","((())())","((()))()","(()(()))",
        "(()()())","(()())()","(())(())","(())()()","()((()))",
        "()(()())","()(())()","()()(())","()()()()"
    ]
    assert sorted(s.generateParenthesis(n)) == sorted(output)