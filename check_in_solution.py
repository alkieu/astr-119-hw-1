#include the Numpy library 
import numpy as np


#define main() function
def main():

	i = 0		#declare integer i
	x = 119.0	#declare float x
	
	for i in range(120):	#loop i from 0 to 119, inclusive
		if((i%2)==0):		#if i is even
			x += 3.				#add 3 to x
		else:				#if i is odd
			x -=5.				#subtract 5 from x
			
	s = "%3.2e" % x			#make a string containing x with 
							#sci notation with 2 decimal places
							
	print(s)				#print s to the screen
	
	
#now the rest of the program continues 

if __name__ == "__main__":	#if main() function exists, run it
	main()