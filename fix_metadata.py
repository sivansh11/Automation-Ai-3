with open("dataset/movies_metadata.csv") as file:
    lines = []
    for line in file.readlines():
        lines.append(line)

lines_to_back_spaces = []

for i, line in enumerate(lines):
    if "True" in line[:5] or "False" in line[:5]:
        pass
    else:
        lines_to_back_spaces.append(i)


lines_to_back_spaces.pop(0)
print(lines_to_back_spaces)



for line_to_back_space in reversed(lines_to_back_spaces):
    line = lines[line_to_back_space]
    lines[line_to_back_space - 1] = lines[line_to_back_space - 1][:-1]
    lines[line_to_back_space - 1] += line


pops = 0
for line_to_back_space in lines_to_back_spaces:
    lines.pop(line_to_back_space - pops)
    pops += 1

with open("dataset/movies_metadata_processed.csv", 'w') as file:
    file.write("".join(lines))