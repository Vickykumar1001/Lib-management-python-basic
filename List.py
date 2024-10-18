def listf():
    global bookname
    global quantity
    global libId
    global name
    global classs
    global section 
    bookname=[]
    quantity=[]
    libId=[]
    name=[]
    classs=[]
    section=[]
    with open("Booklist.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookname.append(a)
                elif(ind==1):
                    quantity.append(a)
                ind+=1
    with open("STUDENTS.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    libId.append(a)
                elif(ind==1):
                    name.append(a)
                elif(ind==2):
                	classs.append(a)
                elif(ind==3):
                	section.append(a)
                ind+=1