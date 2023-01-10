import re
# import sympy


with open('../data/day21.txt') as f:
    lines = f.read().strip().split('\n')

# dict to hold monkeys that do operations
ops = {}
# dict to hold monkeys that do numbers
nums = {}

for line in lines:
    k, line = line.split(': ')
    # if it contains a number
    if re.search(r'\d', line):
        nums[k] = eval(line)
    # otherwise its an op
    else:
        left, op, right = line.split(' ')
        ops[k] = {
            'left': left,
            'op': op,
            'right': right.replace('\n', ''),
        }

def monkey_math(m):
    """Find the result of the equation

    Parameters:
    - m: the monkey to start at. Call this initially with "root", will then call recursively

    Returns:
    - an int representing the result of the equation
    """
    # base case - monkey has a number
    if m in nums:
        return nums[m]
    # recursive case - monkey has an operation
    return int(eval(f'({monkey_math(ops[m]["left"])} {ops[m]["op"]} {monkey_math(ops[m]["right"])})'))

print('Part 1:', monkey_math('root'))

def monkey_math_str(m):
    """Return a simplified string of the monkey equation

    Parameters:
    - m: the monkey to start at. Call this initially with "root", will then call recursively

    Returns:
    - a string representing the simplified equation
    """
    # base case - monkey has a number or is the human
    if m == 'humn':
        return 'x'
    elif m in nums:
        return str(nums[m])
    # recursive case - monkey has an operation
    eqxn = f"({monkey_math_str(ops[m]['left'])} {('=' if m == 'root' else ops[m]['op'])} {monkey_math_str(ops[m]['right'])})"
    if 'x' in eqxn or '=' in eqxn:
        return eqxn
    else:
        return int(eval(eqxn))

def solve_for_x(eqxn):
    """Take an equation and solve it for x.
    
    Parameters:
    - eqxn: a string representing an equation of the form (left expression) = (right expression) where x is on one side

    Returns:
    - The value of x if it exists, or a message if infitine or no solutions
    """
    s2 = eqxn.replace('=', '-(')
    s = s2+')'
    # substitute x for the imaginary number j
    s = s.replace('x', 'j')
    z = eval(s, {'j': 1j})
    real, imag = z.real, -z.imag
    if imag:
            return int(real/imag)
    else:
        if real:
            print("No solution")
        else:
            print("Infinite solutions")
    return None

pt2 = monkey_math_str('root')
print('Part 2:', solve_for_x(pt2))

# couldnt get sympy to work for solving but here is the code to do it
# # parse the equation string
# equation = sympy.parse_expr(equation_string)

# # solve the equation
# solution_set = sympy.solveset(equation)

# print the solution
# print(solution_set)