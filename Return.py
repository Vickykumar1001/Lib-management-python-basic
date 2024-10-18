import List
import date_time
import datetime
import os
def returnf():
	id=int(input("Enter I'd of Issuer: "))
	a="Issue-"+str(id)+".txt"
	try:
		with open(a,"r") as f:
			data=f.read()
			print(data)
	except:
		print("The issuer I'd is incorrect")
		returnf()
	b="Return-"+str(id)+".txt"
	name1=input("Enter the name of issuer: ")
	class1=int(input("Enter the class of issuer: "))
	section1=input("Enter the section of issuer: ")
	with open(a,"r") as file:
		line=file.readlines()
	line1=line[4]
	date=line1[10:20]
	time=line1[33:48]
	date_str1=date+" "+time
	date_obj1=datetime.datetime.strptime(date_str1,'%Y-%m-%d %H:%M:%S.%f')
	d1=date_obj1.date()
	date2=date_time.getDate()
	time2=date_time.getTime()
	date_str2=date2+" "+time2
	date_obj2=datetime.datetime.strptime(date_str2,'%Y-%m-%d %H:%M:%S.%f')
	d2=date_obj2.date()
	d=d2-d1
	day=d.days-14
	fine=0
	ln=0
	count=1
	with open("BOOKLIST.txt","r") as f:
		for i , l in enumerate(f):
			pass
		ln=i+1
	with open(b,"w+") as f:
		f.write("_____________Library Management System______________  \n")
		f.write("                        Returned By: "+ name1+"\n")
		f.write("                        Library ID: "+str(id)+"\n")
		f.write("                        Class: "+str(class1)+section1+"\n")
		f.write("    Date: " + date_time.getDate()+"        Time:"+ date_time.getTime()+"\n")
		f.write("--------------------------------------------------------------\n")
		f.write("S.N. \t\t Bookname \n" )
		f.close()
	for i in range(ln):
		if List.bookname[i] in data:
			with open(b,"a") as f:
				f.write(str(count)+"\t\t"+List.bookname[i]+"\n")
				count+=1
			List.quantity[i]=int(List.quantity[i])+1
	print()
	if(day>=0):
		print("Your return date has passed "+str(day)+" days before!!")
		fine=2*day
		print("\t\t\t Fine: ₹"+ str(fine))
		with open(b,"a")as f:
			f.write("\t\t\t\t\tFine: ₹"+ str(fine)+"\n")
	print("BOOK RETURNED...!!!")
	print()
	os.remove(a)
	

	with open("Booklist.txt","w+") as f:
		for i in range(ln):
			f.write(List.bookname[i]+","+str(List.quantity[i])+"\n")
			
