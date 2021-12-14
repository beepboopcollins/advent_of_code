with open("input.txt") as file:
    puzzle_input = file.readlines()

signals = []
outputs = []

for line in puzzle_input:
    line = line.replace('\n','')
    split_line = line.split(' | ')
    signals.append(split_line[0].split(' '))
    outputs.append(split_line[1].split(' '))

output_dict = {1: 0, 4: 0, 7: 0, 8: 0}

unpacked_outputs = []
for output in outputs:
    unpacked_outputs.extend(output)

for output in unpacked_outputs:
    segs_used = len(output)
    match segs_used:
        case 2:
            output_dict[1] += 1
        case 3:
            output_dict[7] += 1
        case 4:
            output_dict[4] += 1
        case 7:
            output_dict[8] += 1

total = sum(output_dict.values())

print(f"answer part one is {total}")
converted_outputs = []
for signal,output in zip(signals,outputs):
    digit_map = {}
    digit_map[1] = [x for x in signal if len(x) == 2][0]
    digit_map[7] = [x for x in signal if len(x) == 3][0]
    digit_map[4] = [x for x in signal if len(x) == 4][0]
    two_or_3_or_5 = [x for x in signal if len(x) == 5]
    zero_or_6_or_9 = [x for x in signal if len(x) == 6]
    digit_map[8] = [x for x in signal if len(x) == 7][0]
    a = digit_map[7]
    for char in digit_map[1]:
        a = a.replace(char, '')
    for char in digit_map[1]:
        for num in zero_or_6_or_9:
            if char not in num:
                c = char
                f = digit_map[1].replace(char, '')
                digit_map[6] = num
    zero_or_6_or_9.remove(digit_map[6])
    zero_or_9 = zero_or_6_or_9
    b_or_d = digit_map[4].replace(f, '').replace(c, '')
    for char in b_or_d:
        for num in zero_or_9:
            if char not in num:
                digit_map[0] = num
    zero_or_9.remove(digit_map[0])
    digit_map[9] = zero_or_9[0]

    for digit in two_or_3_or_5:
        if c not in digit:
            digit_map[5] = digit
    two_or_3_or_5.remove(digit_map[5])
    two_or_3 = two_or_3_or_5

    for digit in two_or_3:
        if f not in digit:
            digit_map[2] = digit
    two_or_3.remove(digit_map[2])
    digit_map[3] = two_or_3[0]

    output_map = {''.join(sorted(v)): k for k, v in digit_map.items()}
    converted_output = []
    for digit in output:
        converted_output.append(output_map[''.join(sorted(digit))])
    converted_output = [str(n) for n in converted_output]
    converted_outputs.append(int(''.join(converted_output)))

print(f"the answer to part two is {sum(converted_outputs)}")


