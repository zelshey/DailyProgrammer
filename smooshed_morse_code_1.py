#https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

code_str = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'
code_split = code_str.split(' ')

def getMorseCode(_ltr):
	return code_split[ord(_ltr.lower())-97]

def smorse(_str):
	ret = ''
	for i in _str:
		ret += getMorseCode(i)
	return ret
	
print(smorse('sos'))
print(smorse('daily'))
print(smorse('programmer'))
print(smorse('bits'))
print(smorse('three'))
