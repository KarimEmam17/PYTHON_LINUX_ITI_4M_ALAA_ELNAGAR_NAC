		
import os 
 
while (True):
    print("1) List Directories/Files")
    print("2) Create a File")
    print("3) Create a Directory/Folder")
    print("4) Ping a Server")
    print("5) Search For a File")
    print("6) Check Python Version")
    print("7) Show Path of Current Working Directory")
    print("8) Read a File Contents") 
    print("9) Write/Append To a File")
    print("10) Exit")
 
    ch = int(input("Enter Your Choice : "))
 
    if ch == 1:
        os.system('ls')
    elif ch == 2:
        f_name = input("Enter file name : ")
        e_name = input("Enter file extension : ")
 
        os.system('touch ' + f_name + '.' + e_name)
    elif ch == 3:
        name = input("Enter folder name : ")
        os.system('mkdir ' + name)
    elif ch == 4:
        s = input("Enter address(Press enter for default - google.com) : ")
        p = input("Enter number of packer(press enter for default - 10 : )")
        o = input("Do you want the output in a txt file -- y | n -- :")
 
        # p = int(p)
 
        if (s == ''):
            s = 'google.com'
        if (p == ''):
            p = '10'
 
        if (o == 'y'):
            os.system('ping ' + s + ' -c ' + p + ' > ping-output.txt')
        else:
            os.system('ping ' + s + ' -c ' + p)
    elif ch == 5:
        f_name = input("Enter file name : ")
        d_name = input("Enter Directory Path : ")
        os.system('find' + d_name + '-name' + f_name) 
 
    elif ch == 6:
        os.system('python --version')
 
    elif ch == 7:
        os.system('pwd')
		
    elif ch == 8:
        f_name = input("Enter file name : ")
        d_name = input("Enter Directory Path : ")
        os.system('cat' + d_name + '/' + f_name)
		
    elif ch == 9:
        op = input("Enter Operation (W/A):")
        if op == 'W':
            f_name = input("Enter file name : ")
            d_name = input("Enter Directory Path : ")
            text = input("Enter Text : ")
            os.system('echo' + text + '>' + d_name + '/' + f_name)
        elif op == 'A':
            f_name = input("Enter file name : ")
            d_name = input("Enter Directory Path : ")
            text = input("Enter Text : ")
            os.system('echo' + text + '>>' + d_name + '/' + f_name)
        else:
            print("Wrong Choice!")
    elif ch == 10:
        break
    else:
        print("Invalid Choice")