f = open('input.txt', 'r')
first_line = True
num_test_cases = 0
tcs = []
for line in f:
	if first_line:
		num_test_cases = int(line.strip())
		first_line = False
	else:
		tcs.append(line.strip())

for tc in tcs:
	print(tc)