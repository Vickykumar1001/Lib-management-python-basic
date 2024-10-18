import date_time
import List

def issuef():
	t=" "
	f=0
	success=False
	id=int(input("Enter the Library I'd: "))
	while(True):
		name1=input("Enter the name of the Student: ")
		if name1.isalpha():
			break
		print("please input alphabet from A-Z")
	class1=int(input("Enter Class in digit: "))
	section1=input("Enter Section: ").upper()
	for i in range (len(List.libId)):
		if(id==int(List.libId[i])):
			f=1
			if(class1==int(List.classs[i])):
				if(section1==List.section[i]):
					t="Issue-"+str(id)+".txt"
					with open(t,"w+") as f:
						f.write("_____________Library Management System______________  \n")
						f.write("                        Issueed By: "+ name1+"\n")
						f.write("                        Library ID: "+str(id)+"\n")
						f.write("                        Class: "+str(class1)+section1+"\n")
						f.write("    Date: " + date_time.getDate()+"        Time:"+ date_time.getTime()+"\n")
						f.write("------------------------------------------------------\n")
						f.write("S.N. \t\t Bookname \n" )
						f.close()
					while success==False:
							print("Please select a option below:")
							for i in range(len(List.bookname)):
								print("Enter", i+1, "to Issue Book", List.bookname[i])
							try:
								a=int(input())-1
								try:
									if(int(List.quantity[a])>0):
										print("BOOK ISSUED....!!!")
										with open(t,"a") as f1:
											f1.write("1. \t\t"+ List.bookname[a]+"\n")
											f1.close()
										List.quantity[a]=int(List.quantity[a])-1
										ln=0
										with open("BOOKLIST.txt","r") as f:
											for i , l in enumerate(f):
												pass
											ln=i+1
										with open("BOOKLIST.txt","w+") as f:
											for i in range(ln):
												f.write(List.bookname[i]+","+str(List.quantity[i])+"\n")
										loop=True
										count=1
										List.listf()
										while loop==True:
											choice=str(input("Do you want to issue more books? Press Y for yes and N for no.You can not issue same book again..!:"))
											if(choice.upper()=="Y"):
												count=count+1
												print("Please select an option below:")
												for i in range(len(List.bookname)):
													print("Enter", i+1, "to Issue Book", List.bookname[i])
												a=int(input())-1
												if(int(List.quantity[a])>0):
													print("BOOK ISSUED...!!!")
													with open(t,"a") as f:
														f.write(str(count) +". \t\t"+ List.bookname[a]+"\n")
														f.close()
													List.quantity[a]=int(List.quantity[a])-1
													with open("BOOKLIST.txt","w+") as f:
														for i in range(ln):
															f.write(List.bookname[i]+","+str(List.quantity[i])+"\n")
												else:
													print("Book is out of Stock...!!!")
													loop=False
											elif (choice.upper()=="N"):
												with open (t,"r") as f:
													l=f.read()
													print(l)
												print ("Thank you for issuing books from us. ")
												print("")
												loop=False
												success=True
											else:
												print("Please choose as instructed")
									else:
										print("Book is out of Stock...!!!")
										success=False
										break
								except IndexError:
									print("")
									print("Please choose book acording to their number.")
							except ValueError:
								print("")
								print("Please choose as suggested.")
				else:
					print("Section mismatch...!!")
			else:
				print("Class mismatch...!!")
	if(f==0):
		print("I'D not found in member list...!!")