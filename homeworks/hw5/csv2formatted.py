import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as fin, open(output_file, "w") as fout:
    for line in fin:
        numbers = [float(x) for x in line.split(",")]
        formatted_numbers = ["{:>12.3f}".format(x) for x in numbers]
        fout.write("".join(formatted_numbers) + "\n")