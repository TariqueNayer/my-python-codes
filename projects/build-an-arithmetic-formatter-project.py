
def arithmetic_arranger(problems, show_answers=False):
    # Check for too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # Now solve
    first = []
    second = []
    dash = []
    anser = []

    for problem in problems:
        fnum = problem.split(' ')[0]
        operator = problem.split(' ')[1]
        snum = problem.split(' ')[2]
        lenth = max(len(fnum),len(snum)) + 2
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        if fnum.isdigit() == False or snum.isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        if len(fnum) > 4 or len(snum) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len(fnum) < len(snum):
            up = (' ' * (lenth - len(fnum))) + fnum
            down = operator + ' ' + snum
        elif len(fnum) > len(snum):
            up = '  '+fnum
            down = operator+(' ' * (lenth - len(snum) - 1)) + snum
        else : 
            up = '  ' + fnum
            down = operator + ' ' + snum
        line = ('-' * lenth)
        if operator == '+':
            solve = str(int(fnum) + int(snum))
            solve = ' ' * (lenth - len(solve)) + solve
        elif operator == '-':
            solve = str(int(fnum) - int(snum))
            solve = ' ' * (lenth - len(solve)) + solve
        
        first.append(up)
        second.append(down)
        anser.append(solve)
        dash.append(line)
    # Now print
    if show_answers == False:
        arranged_str = '    '.join(first) +'\n'+ '    '.join(second) +'\n'+ '    '.join(dash)
    else:
        arranged_str = '    '.join(first) +'\n'+ '    '.join(second) +'\n'+ '    '.join(dash) +'\n'+ '    '.join(anser)
    return arranged_str

# Example usage:
#print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')