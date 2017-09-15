# Counts the number of occurrances of each letter in a string.

message = 'It was bright cold day in April,and the clocks were striking thirteen.'

count = {}
for character in message:
	count.setdefault(character,0)
	count[character] = count[character] + 1
print(count)
