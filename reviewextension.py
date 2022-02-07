data = []
count = 0
with open('reviews.txt', 'r') as f: 
	for line in f: 
		data.append(line)
		count += 1
		if count % 50000 == 0: 
			print(len(data)) #calculate the total length of the data 
print(data[0]) #test of printing first review



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

but = [d for d in data if 'but' in d]
print('There are roughly', len(but), 'reviews that has concerns or issues in their trade, however, this data is not precise.')

#word count model
wc = {} #word count
for d in data: 
 	words = d.split()
 	for word in words:
 		if word in wc:
 			wc[word] +=1
 		else:
 			wc[word] = 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))
while True:
	word = input('Insert the word you want to search: ')
	if word == 'q':
		break
	if word in wc:
		print('The word', word, 'appeared', wc[word], 'times')
	else:
		print('This word is not found in the reviews')
print('Thank you for searching!')