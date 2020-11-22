def zero(f = None): 
	if f is None: 
		return 0 
	else: 
		return f(0) 
def one(f = None): 
	if f is None: 
		return 1 
	else: 
		return f(1) 
def two(f = None): 
	if f is None: 
		return 2 
	else: 
		return f(2) 
def three(f = None): 
	if f is None: 
		return 3 
	else: 
		return f(3) 
def four(f = None): 
	if f is None: 
		return 4 
	else: 
		return f(4) 
def five(f = None): 
	if f is None: 
		return 5 
	else: 
		return f(5) 
def six(f = None): 
	if f is None: 
		return 6 
	else: 
		return f(6) 
def seven(f = None): 
	if f is None: 
		return 7 
	else: 
		return f(7) 
def eight(f = None): 
	if f is None: 
		return 8 
	else: 
		return f(8) 
def nine(f = None): 
	if f is None: 
		return 9 
	else: 
		return f(9) 

def plus(f): 
	return lambda x: x + f
def minus(f): 
	return lambda x: x - f
def times(f): 
	return lambda x: x * f
def divided_by(f): 
	return lambda x: x // f

print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))

print(seven(divided_by(four())))
