import Admin
import Member
import List
import Issue
import Return
def start():
    while(True):
        print("_______Welcome to the Library Management System_______")
        print("-------------------------------------------------------")
        print("Enter 1. for Admin module ")
        print("Enter 2. for Member management module ")
        print("Enter 3. to Issue or Return book ")
        print("Enter 4. to exit ")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
            	List.listf()
            	Admin.adminf()
            	print ()
   
            elif(a==2):
                List.listf()
                Member.memberf()
            elif(a==3):
            	   while(True):
            	   	print("Enter 1 to See Booklist")
            	   	print("Enter 2 to Issue Book")
            	   	print("Enter 3 to Return Book")
            	   	print("Enter 4 to return to main menu")
            	   	c=int(input("Enter your Choice: "))
            	   	print()
            	   	if(c==1):
            	   		print("BOOK NAMES,QUANTITY")
            	   		with open("BOOKLIST.txt","r") as f:
            	   			lines=f.read()
            	   			print(lines)
            	   			print ()
            	   	elif(c==2):
            	   		List.listf()
            	   		Issue.issuef()
            	   		print()
            	   	elif(c==3):
            	   		List.listf()
            	   		Return.returnf()
            	   		print()
            	   	elif(c==4):
            	   		break
            	   	else:
            	   		print("Wrong Option...!! ")
            	   		print("TRY AGAIN...!!")
            	   		print()
            elif(a==4):
                print("Thank you for using Library Management System")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
start()