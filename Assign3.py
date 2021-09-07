def fun1(a,b=0, *args,**kwargs):
	print(a,b)
	print(args)
	print(kwargs)
fun1(20,30)
fun1(40)
fun1(1,2,3,4)
fun1(2, x=4, y=5)