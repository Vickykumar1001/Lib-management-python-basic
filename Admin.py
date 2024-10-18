import List
def adminf():
	
	#PASSWORD is 123456
	Password=123456
	count=0
	while(True):
				  print('_______Welcome to Admin Module_______')
				  print('----------------------------------------------')
				  #SECURITY
				  if count ==0:
				  	password1=int(input("Enter Password : "))
				  	print()
				  	if password1==Password:
				  		count=1
				  	else:
				  		print("WRONG PASSWORD!!")
				  		break
				  	
				  print('Enter 1 to See Booklist ')
				  print('Enter 2 to Add Books ')
				  print('Enter 3 to Remove Books ')
				  print('Enter 4 to go to main menu')
				  try:
				  	a=int(input("Select a choice from 1-4:   "))
				  	print()
				  	if(a==1):
				  		print("BOOK NAMES,QUANTITY")
				  		with open("BOOKLIST.txt","r") as f:
				  			lines=f.read()
				  			print(lines)
				  			print ()
				  	elif(a==2):
				  		q=0
				  		print("Enter 1 to Add New Book")
				  		print("Enter 2 to Increase Quantity of Book")
				  		print()
				  		List.listf()
				  		c=int(input())
				  		if(c==1):
				  			new_book= input("Enter the Name of Book followed by comma and Quantity:")
				  			file1 = open("BOOKLIST.txt","a")
				  			file1.write(new_book+"\n")
				  			file1.close()
				  			print()
				  			print("BOOK ADDED...!!!")
				  			print()
				  			List.listf()
				  		elif(c==2):
				  			print("Please select a option below:")
				  			for i in range(len(List.bookname)):
				  				print("Enter", i+1, "to increase quantity of ", List.bookname[i])
				  			a=int(input())-1
				  			q=int(input("Enter quantity: "))
				  			print()
				  			print("BOOK ADDED....!!!")
				  			print()
				  			List.quantity[a]=int(List.quantity[a])+q
				  			with open("Booklist.txt","r") as f:
				  				for i, l in enumerate(f):
				  					pass
				  				ln=i+1
				  			with open("Booklist.txt","w+") as f:
				  				for i in range(ln):
				  					f.write(List.bookname[i]+","+str(List.quantity[i])+"\n")
				  		else:
				  			print("WRONG OPTION...!!! TRY AGAIN...!!")
				  			print()
				  	elif(a==3):
				  		List.listf()
				  		remove=""
				  		print("Please select a option below:")
				  		for i in range(len(List.bookname)):
				  			print("Enter", i+1, "to remove book", List.bookname[i])
				  		a=int(input())-1
				  		q=int(input("Enter quantity: "))
				  		print()
				  		print("BOOK REMOVED....!!!")
				  		print()
				  		List.quantity[a]=int(List.quantity[a])-q
				  		with open("Booklist.txt","r") as f:
				  			for i, l in enumerate(f):
				  				pass
				  			ln=i+1
				  		with open("Booklist.txt","w+") as f:
				  			for i in range(ln):
				  				f.write(List.bookname[i]+","+str(List.quantity[i])+"\n")
				  		if (int(List.quantity[a])==0):
				  			remove=(List.bookname[a]+","+str(List.quantity[a]))
				  			with open("BOOKLIST.txt", "r") as f:
				  				lines = f.readlines()
				  			with open("BOOKLIST.txt", "w") as f:
				  				for line in lines:
				  					if (line.strip("\n") != remove):
				  						f.write(line)
				  			List.listf()
				  	elif(a==4):
				  		break
				  	else:
				  		print("Please enter a valid choice from 1-4")
				  except ValueError:
				  	print("Please input as suggested.")
				  