# -*- coding: utf-8 -*-
from time import*
from random import*
from os import*
from msvcrt import*



disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|                          Develope by                           |\n|                          willieku123                           |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n------------------------------------------------------------------"
print(disp)
sleep(2)


system('cls')
disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|                          Powered by                            |\n|                          Python 2.7                            |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n------------------------------------------------------------------"
print(disp)
sleep(2)








while True:
    switch = "up"
    wait_for_s = False
    mode = "choosing"
    while True:


        
        if switch == "up":
            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|                    Steams (Tabletop game)                      |\n|                                                                |\n|                        >>  start  <<                           |\n|                       tuteral & rules                          |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                  ( W/S to switch, SPACE to OK )|\n------------------------------------------------------------------"
            print(disp)
        



        for i in range(10):
            if switch == "down" or wait_for_s == True:
                break
            sleep(0.03)
            if kbhit():
                keyboard = ord(getch())
                if keyboard == 115: #s
                    switch = "down"
                    break
                elif keyboard == 32: #space
                    wait_for_s = True
                    break
        

        if switch == "up":
            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|                    Steams (Tabletop game)                      |\n|                                                                |\n|                            start                               |\n|                       tuteral & rules                          |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                  ( W/S to switch, SPACE to OK )|\n------------------------------------------------------------------"
            print(disp)
        



        for i in range(10):
            if switch == "down" or wait_for_s == True:
                break
            sleep(0.03)
            if kbhit():
                keyboard = ord(getch())
                if keyboard == 115:
                    switch = "down"
                    break
                elif keyboard == 32: #space
                    wait_for_s = True
                    break
       











        if switch == "down":

            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|                    Steams (Tabletop game)                      |\n|                                                                |\n|                            start                               |\n|                    >> tuteral & rules <<                       |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                  ( W/S to switch, SPACE to OK )|\n------------------------------------------------------------------"
            print(disp)
        



        for i in range(10):
            if switch == "up" or wait_for_s == True:
                break
            sleep(0.03)
            if kbhit():
                keyboard = ord(getch())
                if keyboard == 119: #w
                    switch = "up"
                    break
                elif keyboard == 32: #space
                    wait_for_s = True
                    mode = "tutor"
                    break
        

        if switch == "down":
            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|                    Steams (Tabletop game)                      |\n|                                                                |\n|                            start                               |\n|                       tuteral & rules                          |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                  ( W/S to switch, SPACE to OK )|\n------------------------------------------------------------------"
            print(disp)
        



        for i in range(10):
            if switch == "up" or wait_for_s == True:
                break
            sleep(0.03)
            if kbhit():
                keyboard = ord(getch())
                if keyboard == 119:
                    switch = "up"
                    break
                elif keyboard == 32: #space
                    wait_for_s = True
                    mode = "tutor"
                    break






        if mode == "tutor":
            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|         Hello challenger:                                      |\n| \"Steams\" is a tabletop game,and we rebuild it into a program.  |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                       ( SPACE )|\n------------------------------------------------------------------"
            print(disp)
            if ord(getch()) == 32:
                    sleep(0)


            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|         Hello challenger:                                      |\n| your job is to make a \"number train\" from small to big.        |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                       ( SPACE )|\n------------------------------------------------------------------"
            print(disp)
            if ord(getch()) == 32:
                    sleep(0)

            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|         Hello challenger:                                      |\n| number you get will be  given from 1-30(11-19 *2),and a \"star\".|\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                       ( SPACE )|\n------------------------------------------------------------------"
            print(disp)
            if ord(getch()) == 32:
                    sleep(0)

            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|         Hello challenger:                                      |\n| after fill in 20 numbers,you may choose a number as the \"star\".|\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                       ( SPACE )|\n------------------------------------------------------------------"
            print(disp)
            if ord(getch()) == 32:
                    sleep(0)

            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|         Hello challenger:                                      |\n| of course,20 numbers U get will be ramdomly given from 41cards.|\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                       ( SPACE )|\n------------------------------------------------------------------"
            print(disp)
            if ord(getch()) == 32:
                    sleep(0)

            system('cls')
            disp ="------------------------------------------------------------------\n|                                                                |\n|                                                                |\n|                                                                |\n|         Hello challenger:                                      |\n| is the tutoral clear? if so,try once now!!(if not, R.I.P.)     |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                                |\n|                                                       ( SPACE )|\n------------------------------------------------------------------"
            print(disp)
            if ord(getch()) == 32:
                    sleep(0)

            
                    
            










                
        if wait_for_s == True :
            break





    alls = []
    alls.append("star(&)")
    for i in range(30):
        alls.append(i+1)
        if i+1 <=19 and i+1 >= 11:
            alls.append(i+1)
            
    filled = []
    for i in range(20):
        filled.append("n")
    #       "n" = 尚未填入   "star(&)" =紅星   (number) = 數字

    wait = []
    shuffle(alls)
    for i in range(20):    
        wait.append( alls[i] )  #決定發牌順序








    def calculate(train):    
        full = []
        ch = 0
        while True:        
            lens = 0
            while True:
                lens += 1
                
                if train[ch] > train[ch+1] :
                    ch +=1 
                    break
                ch +=1
                if ch >= 19:
                    lens += 1
                    break
                
            full.append(lens)
            if ch>= 19:
                break
        score = 0
        scoreboard = [0,0,1,3,5,7,9,11,15,20,25,30,35,40,50,60,70,85,100,150,300]             #read 1-20
        for i in range(len(full)):
            score += scoreboard[full[i]]
        return score
                
            
            
                
        




    def display(messege,mouse_pos,mouse_level):   #moise_pos: 1-19         mouse_level:   0(off) - 1-2-3
        intel_len = len(messege)
        intel_left = (64 - intel_len)/2
        intel_right = 64 - intel_len - intel_left

        system('cls')
        disp =  "------------------------------------------------------------------  \n"
        disp += "|                                                                |  \n" #64 spaces
        disp += "|"  +   " "*intel_left +   messege    +    " "*intel_right   +  "|  \n"
        disp += "|                                                                |  \n"
        disp += "|                                                                |  \n"
        disp += "|================================================================|  \n"
        disp += "|  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20   |  \n"
        disp += "|----------------------------------------------------------------|  \n"

        
            
        disp += "|  "
        for i in range(20):
            if filled[i] ==  "n":
                disp += "__ "
            elif filled[i] == "star(&)":
                disp += "&  "
            else:
                if filled[i] <= 9:
                    disp += str(filled[i])+"  "
                else:
                    disp += str(filled[i])+" "
        disp += "  |  \n"

            
        if mouse_level ==1:             #####
            disp += "|  "
            for i in range(20):
                if i == mouse_pos:
                    disp += "^  "
                else:
                    disp += "   "
            disp += "  |  \n"
            
        else:
            disp += "|                                                                |  \n"
            
        if mouse_level ==2:            #####
            
           
            
            disp += "|  "
            for i in range(20):
                if i == mouse_pos:
                    disp += "^  "
                else:
                    disp += "   "
            disp += "  |  \n"
            
        else:
            disp += "|                                                                |  \n"

        if mouse_level ==3:              #####

            
            
            disp += "|  "
            for i in range(20):
                if i == mouse_pos:
                    disp += "^  "
                else:
                    disp += "   "
            disp += "  |  \n"
            
        else:
            disp += "|                           ( switch with A/D ,SPACE to confirm )|  \n"
        
        disp += "------------------------------------------------------------------  \n"
        print(disp)
        
            


    '''               Table:

        ------------------------------------------------------------------
        |                                                                |
        |                          you got 12!                           |
        |                                                                |
        |                                                                |
        |----------------------------------------------------------------|
        |  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20   |
        |  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^    |
        |                                                                |
        |                                                                |
        ------------------------------------------------------------------
    '''








    mouse_pos = 0
    for i in range(20):      #正式遊戲循環
        while True:
            intel = "you got "+str(wait[i])


            display(intel,mouse_pos,1)
            confirm = False
            while True:     # to select
                if confirm == True:
                    break
                        
                display(intel,mouse_pos,0)                   #####
                for j in range(5):
                    sleep(0.02)

                    
                    if kbhit():
                        keyboard = ord(getch())
                        if keyboard == 97:     # 'a'
                            if mouse_pos>=1:
                                mouse_pos += -1
                                display(intel,mouse_pos,1)
                            
                        elif keyboard == 100:  # 'd'
                            if mouse_pos<= 18:
                                mouse_pos += 1
                                display(intel,mouse_pos,1)

                        elif keyboard == 32:   # 'space'
                            to_insert = mouse_pos + 1
                            confirm = True
                            break
                if confirm == True:
                    break
                
                display(intel,mouse_pos,1)                   #####
                for j in range(15):
                    sleep(0.04)

                    
                    if kbhit():
                        keyboard = ord(getch())
                        if keyboard == 97:     # 'a'
                            if mouse_pos>=1:
                                mouse_pos += -1
                                display(intel,mouse_pos,1)
                            
                        elif keyboard == 100:  # 'd'
                            if mouse_pos<= 18:
                                mouse_pos += 1
                                display(intel,mouse_pos,1)

                        elif keyboard == 32:   # 'space'
                            to_insert = mouse_pos + 1
                            confirm = True
                            break





                
            
                   
                    
                        
                           



                
            
            try:
                
                if filled[to_insert-1] != "n":
                    display("the blank is already filled",mouse_pos,1)
                    sleep(0.7)
                    continue
                else:
                    filled[to_insert-1] = wait[i]

                    
            except:
                display(" \033[0;31m something wrong\033[00m ",mouse_pos,1)
                sleep(2.7)
                continue
            if i == 19:
                display(intel,mouse_pos,1)
            break

    for i in range(20):
        if filled[i] =="star(&)":
            display("type the numer U would like \"&\" to be (1-30)",mouse_pos,0)
            filled[i] =input("")
    display("u've finished the blanks!! doing math on your score....",mouse_pos,0)
    sleep(1.5)

    score = calculate(filled)
    to_show = "your score is: " + str(score) + "   (press  SPACE to home)"
    sleep(3)
    display(to_show,mouse_pos,0)
    if ord(getch()) == 32:
        sleep(0)








    
    

