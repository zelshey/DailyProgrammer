#https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

def yahtzee_upper(_arr):
	d = dict()
	for n in _arr:
		if(not (n in d)): d[n] = 0
		d[n] += 1
	m = 0
	for k in d:
		m = max(m, d[k]*k)
	return m
	
print(yahtzee_upper([2, 3, 5, 5, 6]))
print(yahtzee_upper([1, 1, 1, 1, 3]))
print(yahtzee_upper([1, 1, 1, 3, 3]))
print(yahtzee_upper([1, 2, 3, 4, 5]))
print(yahtzee_upper([6, 6, 6, 6, 6]))

print(yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
    1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
    30864, 4868, 30864]))