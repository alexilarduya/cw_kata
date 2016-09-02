#https://www.codewars.com/kata/valid-braces

def validBraces(string):

	d = { '(': ')', '[' : ']', '{' : '}'}

	if len(string)%2 == 1:
		return False

	l = []

	for char in string:
		try:
			l.append( d[char] )
		except KeyError:
			if len(l) > 0 and l[-1] == char:
				del(l[-1])
			else:
				return False

	if len(l) == len(string):
		return False

	return True




