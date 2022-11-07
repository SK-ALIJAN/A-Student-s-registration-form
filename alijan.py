id=input("where are you from!")
if(id=="kolkata"):
    print("please say us your age")
    age=input()
    if(age=="18" or age>"18" or age=="atharo"):
        print("okey you are eligible for this show")
        print("please say your ticket standard")
        ticket_standard=int(input())
        if(ticket_standard>=500):
            print('''thank you and go to your shit there up-stair''')
        else:
            print("go down-stair please you have reserve for down grade shit")
    else:
        print('''soory you are uneligibile for under the 18 age''')           
else:
    print("sorry it is for only kolkata resident") 

student=input()
if(student.isalpha()):
    print("what is your qualifiction!")
    qualification=input()
    if(qualification=="hs" or qualification=="b.tech" or qualification=="bca"):
        print("are you apply for it anywhere?")
        ask=input()
        if(ask=="no" or ask=="naa"):
            print("okey give me your user_id and password")
            ask2=list(input().split(" "))
            if(ask2[0]=="masai"  and ask2[1]=="masai"):
                print("thank you!")
            else:
                print("""wrong! please reset it and come agian""")  
        else:
            print("okey okey :) ")  
    else:
        print("sorry at lease 12 pass") 
else:
    print("wrong input!")                       




