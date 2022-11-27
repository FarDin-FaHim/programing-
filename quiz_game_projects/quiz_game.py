print("-----------Welcome to my quiz game!------------")

answer = input(" Do you want to play game ? ")
if answer.lower() != "yes":
    quit()
else:
    print("Ok! Let's play")
    score = 0
#----------------------Question_#1----------------------------------------------------
    answer = input(" What is full name of AMD ?")
    if answer.lower() == "advanced micro devices":
        print("Correct")
        score += 1
    else:
        print("****Incorrect****")
#----------------------Question_#2----------------------------------------------------
    answer = input("""From what location are the 1st computer instructions available on boot up?
        A. 	ROM BIOS
        B. 	CPU
        C. 	boot.ini
        D. 	CONFIG.SYS
        E. 	None of the above 
          >>> """)
    if answer.lower() == "c":
        print("Correct")
        score += 1
    else:
        print("****Incorrect****")
#----------------------Question_#3----------------------------------------------------
    answer = input(""" Ram stands for ?
        A: Random Access Memory
        B: Read Access Memory
        C: Read Arithmetic Memory
        D: Random Artithemtic Memory
        >>>  """)
    if answer.lower() == "a":
        print("Correct")
        score += 1
    else:
        print("****Incorrect****")
#----------------------Question_#4----------------------------------------------------
    answer = input(""" The Central Processin Unit(CPU) consists of ?
        A: main store
        B: Control Unit
        C: Arithmetic and Logic Unit
        D: All of above
        >>>  """)
    if answer.lower() == "B":
        print("Correct")
        score += 1
    else:
        print("****Incorrect****")
#----------------------Question_#5----------------------------------------------------
    answer = input(""" The main computer that stores the files that can 
    be sent to computers that are networked together is ?
    (A) Clip art
    (B) Mother board
    (C) Peripheral
    (D) File server
    >>>  """)
    if answer.lower() == "B":
        print("Correct")
        score += 1
    else:
        print("****Incorrect****")
#----------------------Question_#6----------------------------------------------------
    answer = input(""" Google (www.google.com) is a:
    (A) Search Engine
    (B) Number in Math
    (C) Directory of images
    (D) Chat service on the web
     >>>  """)
    if answer.lower() == " A ":
        print("Correct")
        score += 1
    else:
        print("****Incorrect****")

print("you got  "+str(score) +" questions correct !")
print("you got  " + str((score/6)*100) + " %." )
#test
print("-----------Good Bay!------------")
