"""Technical assessment
"""

def print_output_row(j, step):
    row = "" # Initialize an empty string
    for i in range(1,4):
        out = f'{i+step} X {j} = {(i+step)*j}'
        row += out + "        "
    print(row)

def print_line_by_line(step):
    for j in range(1,10):
        print_output_row(j, step)

for step in range(3):
    print_line_by_line(step*3)
    print('//////////////////////////')