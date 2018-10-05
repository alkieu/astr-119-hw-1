import numpy as np
import sys

#define function that returns a value
def expo(x):
	return np.exp(x)	#return np e^x function
	
#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#cal the expo function
		
#define main() function
def main():
	n = 10	#provide default function for n
	
	#check of there is a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])	#if an argument was provided, use it for n
		
	show_expo(n)	#call show_expo function
	
	
#run the main() function
if __name__ == "__main__":
	main()