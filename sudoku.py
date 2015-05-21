import os
from random import randint
def print_sudoku(list,flag):
	print "\n\n"
	for i in range(0,4):
		print "\t\t",
		print "-"*17
		print "\t\t",
		for j in range(0,4):
			if flag[i][j]:
				print "| %d" % list[i][j],
			else:
				print "|  ",
		print "|"
	print "\t\t",
	print "-"*17

os.system('clear')

def randomise(arr):
	r = randint(0,3)
	c = randint(0,3)
	temp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for i in range(0,4):
		for j in range(0,4):
			temp[r%4][j] = arr[i][j]
		r +=1
	for j in range(0,4):
		for i in range(0,4):
			temp[i][c%4] = arr[i][j]
		c +=1
	return temp
			
def start_game():
	list = [[2,3,4,1],[1,4,2,3],[3,2,1,4],[4,1,3,2]]
	flag = [[1,0,1,0],[0,0,1,0],[1,0,0,1],[0,1,0,1]]
	list = randomise(list)
	flag = randomise(flag)
	
	os.system('clear')
	print "\n\n\t\t     SUDOKU"
	print_sudoku(list,flag)
	check = 7
	while(check != 16):
		a = int(raw_input("\n\nEnter the number to be inserted { a : 1<=a<=4 } : "))
		while(not a in range(1,5)):
			print "Invalid Input"
			a = int(raw_input("Enter the number to be inserted { a : 1<=a<=4 } : "))
		b,c = (raw_input("Enter co-ordinates { x,y : 1<=x,y<=4 } : ")).split()
		b = int(b)-1
		c = int(c)-1
		while(not b in range(0,4) or not c in range(0,4)):
			print "Invalid co-ordinates"
			b,c = (raw_input("Enter co-ordinates {x,y : 1<=x<=4} : ")).split()
			b = int(b)-1
			c = int(c)-1
		if flag[b][c]==0:
			if a == list[b][c]:
				print "Correct"
				check += 1
				flag[b][c] = 1
			else:
				print "Incorrect. Try Again"
		else:
			print "Number already exists in that place"
		
		raw_input("Press any key to continue : ")
		
		os.system('clear')
		print "\t\t SUDOKU"
		print_sudoku(list,flag)
	
	print "Congrats you have completed the game!"
			
		
print "\n\n\t\t     SUDOKU\n"
raw_input("Press any key to continue : ")
c = 'y'
while c == 'y' or c == 'Y':
	start_game()
	print "Do you want to play again ? (y)"
	c = raw_input()

print "Thank you for playing. Bye!"
os.system('clear')
exit(0)	