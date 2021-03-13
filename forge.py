# 1. create a new function object
# 2. prepend itself to enclosing class's __init__
# 3. self._func = new func object <method> with reinitialised params

def forge(func):
	tmp_obj = func.__new__(func.__class__, func.__code__, func.__globals__)
	tmp_obj.__defaults__ = tuple([type(i)() for i in func.__defaults__])
	return tmp_obj

def run_test():
	print(f":. creating function with default arg accumulator")
	def foo(acc=[]):
		acc.append('a')
		#print(acc, end="")
		return acc
	
	print(f":. first function ~> {foo}")
	print(f":. forging a new copy of foo... ")

	_tmp_obj = forge(foo)

	print(f":. forged object ~> {_tmp_obj}")
	print(f":. calling obj1 {foo} thrice and obj2 {foo} once")
	print(f":. obj1 <{foo}> ~> {foo()}{foo()}{foo()}")
	print(f":. obj2 <{_tmp_obj}> ~> {_tmp_obj()}")


if __name__ == "__main__":
	run_test()
