# python program to read the specific file
while True :
    print('\nenter "exit" to close the application')
    fname = input('\nenter the file name :')
    if fname == 'exit' :
        exit()
    else :
        try :
            with open(fname,'r',newline ="") as fo :
                for line in fo :
                    print(line, end = "")
        except :
            print('sorry the file {} is not existed in the folder')
            print('please enter the correct file name to read the contents')
input()
