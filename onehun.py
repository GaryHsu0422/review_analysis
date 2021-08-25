data = []
count = 0
with open('reviews.txt', 'r') as f: 
	for line in f: 
		data.append(line)
		count += 1
		if count % 1000 == 0: 
			print(len(data))
sum_len = 0
for d in data: 
	sum_len = sum＿len + len(d)
	if sum_len % 100000 == 0: 
		print(sum_len)
avg = sum_len / len(data)
print('The average word length of a review is', avg, 'words')

new = []
for o in data:
	if len(o) < 100:
		new.append(o)
print('There are', len(new), 'amount of reviews that the word length is not over 100')
