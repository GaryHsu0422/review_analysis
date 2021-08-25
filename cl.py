data = []
count = 0
with open('reviews.txt', 'r') as f: 
	for line in f: 
		data.append(line)
		count += 1
		if count % 50000 == 0: 
			print(len(data))
sum_len = 0
for d in data: 
	sum_len = sum＿len + len(d)
	if sum_len % 500000 == 0: 
		print(sum_len)
avg = sum_len / len(data)
print('The average word length of a review is', avg, 'words')

new = []
for o in data:
	if len(o) < 100:
		new.append(o)
print('There are', len(new), 'amount of reviews that the word length is not over 100')

good = [d for d in data if 'good' in d]
print('There are roughly', len(good), 'reviews that are satisfied with their trade, however, this data is not precise.')

but = []
for a in data: 
	if 'but' in d:
		but.append(d)
print('There are roughly', len(but), 'reviews that has concerns or issues in their trade, however, this data is not precise.')