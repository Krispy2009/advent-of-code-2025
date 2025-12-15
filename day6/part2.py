answers = []

def solve_equation(equation):

    nums, operand = equation[:-1], equation[-1]
    nums = [int(num) for num in nums]
    if operand == "+":
        return sum(nums)
    elif operand == "*":
        ans = 1
        for i in range(len(nums)):
            ans *= nums[i]
        return ans

def check_for_empty(matrix, num_rows, col):
    return all(matrix[row][col] == ' ' for row in range(num_rows))
            

def make_cephalopod_numbers(matrix):    
    equations = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    operator_row = num_rows - 1
    
    col = num_cols - 1
    while col >= 0:
        if check_for_empty(matrix, num_rows, col):
            col -= 1
            continue
        
        problem_cols = []
        while col >= 0:
            if check_for_empty(matrix, num_rows, col):
                break
            
            problem_cols.append(col)
            col -= 1
        
        problem_cols.reverse()        
        operator_col = None
        operator = None
        for c in problem_cols:
            char = matrix[operator_row][c]
            if char in ['+', '*']:
                operator_col = c
                operator = char
                break
        
        if operator_col is None:
            continue
        
        numbers = []
        for c in reversed(problem_cols):
            digits = []
            for row in range(operator_row):
                char = matrix[row][c]
                if char != ' ':
                    digits.append(char)
            
            if digits:
                number = int(''.join(digits))
                numbers.append(number)
        
        equation = numbers + [operator]
        equations.append(equation)
    
    return equations




with open("input.txt", "r") as file:
    lines = file.readlines()
    matrix = []
    for line in lines:
        matrix.append([x for x in line.strip("\n")])
    print(matrix)

    equations = make_cephalopod_numbers(matrix)
    print(equations)
    for equation in equations:
        answers.append(solve_equation(equation))
    


    print(sum(answers))