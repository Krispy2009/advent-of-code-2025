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
    
with open("input.txt", "r") as file:
    lines = file.readlines()
    matrix = []
    for line in lines:
        matrix.append([x for x in line.strip().split(" ") if x != ""])

    for i in range(len(matrix[0])):
        collected_equation = []
        for j in matrix:
            collected_equation.append(j[i])
        answers.append(solve_equation(collected_equation))

    print(sum(answers))