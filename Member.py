import List
def memberf():
	#PASSWORD is 123456
	Password=123456
	count=0
	while(True):
		print('_______Welcome to Member Management Module_______')
		print('-------------------------------------------------')
		if count ==0:
			password1=int(input("Enter Password : "))
			print()
			if password1==Password:
			 count=1
			else:
				print("WRONG PASSWORD!!")
				break
		print('Enter 1 to See Member list ')
		print('Enter 2 to Add Member ')
		print('Enter 3 to Remove  Member ')
		print('Enter 4 to go to main menu')
		try:
				a=int(input("Select a choice from 1-4:   "))
				print()
				if(a==1):
				 print("Lib_ID,Name,Class, Section")
				 with open("STUDENTS.txt","r") as f:
				  lines=f.read()
				 print(lines)
				 print ()
				elif(a==2):
					a=input("Enter Library ID :")
					b=input("Enter Name :")
					c=input("Enter Class :")
					d=input("Enter Section :")
					new_student=a+','+b+','+c+','+d
					file1 = open("STUDENTS.txt","a")
					file1.write(new_student+"\n")
					file1.close()
					print()
					print("MEMBER ADDED...!!!")
					print()
					List.listf()
				elif(a==3):
					List.listf()
					id=int(input("Please enter Student's Library ID: "))
					print()
					for i in range(0,len(List.name)):
						if(id==int(List.libId[i])):
							remove=str(List.libId[i]+","+str(List.name[i])+","+str(List.classs[i])+","+str(List.section[i]))
							with open("STUDENTS.txt", "r") as f:
								lines = f.readlines()
							with open("STUDENTS.txt", "w") as f:
								for line in lines:
									if (line.strip("\n") != remove):
										f.write(line)
					List.listf()
					print("REMOVED.....!!!")
					print()
				elif(a==4):
					break
				else:
					print("Please enter a valid choice from 1-4 ")
		except ValueError:
				print("Please input as suggested.")
				    	