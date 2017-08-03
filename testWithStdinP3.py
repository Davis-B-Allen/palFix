#code

import random
import string
tc10000 = ""
for i in range(10000):
	tc10000 += random.choice(string.ascii_lowercase)
#print(tc10000)

tc1 = "abaaa"
tc2 = "geek"
tc3 = "test"


def add_substring_to_count_dict(count_dict, substring):
	if substring not in count_dict:
		count_dict[substring] = 1
	else:
		count_dict[substring] = count_dict[substring] + 1

def is_pal(substring):
	str = substring
	str_len = len(substring)
	for i in range(len(substring)//2):
		if not (str[0] == str[-1]):
			return False
		str = str[1:str_len-1]
		str_len = len(str)
	return True

# returns the number of unique continuous palindromic substrings
def num_uniq_cont_pal(some_string):
	count_dict = dict()
	ss_length = len(some_string)
	# print(ss_length)
	# iterate over substring lengths
	for substring_length in range(1,ss_length+1):
		# print(substring_length)
		# iterate through string
		for i in range(ss_length):

			# choose substring if within bounds
			if (i + substring_length) > ss_length:
				break
			substring = some_string[i:i+substring_length]
			# print(substring)
			# check if palindrome
			if is_pal(substring):
				# print(substring)
				add_substring_to_count_dict(count_dict, substring)
	for key in list(count_dict.keys()):
		pass
		# print(key + ": " + str(count_dict[key]))
	return len(list(count_dict.keys()))


x = 0
# x = num_uniq_cont_pal(tc10000)
# print("Number of uniq palindromic substrings in ''" + tc10000 + "'' is: " + str(x))
# print(is_pal("aab"))

first_line = True
num_test_cases = int(input())
tcs = []
for i in range(num_test_cases):
	line = input()
	tcs.append(line)

#print("****")
#print("****")

for tc in tcs:
	print((str(num_uniq_cont_pal(tc))))