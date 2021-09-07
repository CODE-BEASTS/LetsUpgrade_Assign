#Write a program to find the prime number
#Enter a number to program and get the output "Prime" or "Not Prime"

num = int(input("Enter any number"))

if num>1:
	for i in range(2, num//2) :
		if (num%i) == 0:
			print(num,"is not a prime number")
			break
		else:
			print(num,"is a prime number")
else:
    print(num,"is not a prime number")
		