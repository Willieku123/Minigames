# -*- coding: utf-8 -*-
from time import*
from random import*
from os import*
from msvcrt import*
from threading import*


t=0
h=1
true_sys_z=0
sys_x=1
sys_y=1
sys_z=1
pre_sys_x=sys_x
pre_sys_z=sys_z
pre_true_sys_z=true_sys_z
re=1
now_type = "t"
pos_x = 5
pos_y = 0

disp=""
row=0
side="None"
first = True
check_aim = True
score = 0


height	= 25
hit = 0
x=1
list1 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list2 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list3 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list4 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list5 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list6 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list7 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list8 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list9 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list10=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list11=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0
list12=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #10個0



array=[list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12]
        #empty:0
        #moving:1
        #freezes:2

end_scene="--------------\n" 
for i in range(height-15):
                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "|   DEV by   |\n"
end_scene += "| Willieku123|\n"                                      
for i in range(height-12):                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "--------------"
print(end_scene)
sleep(1)

system('cls')
end_scene="--------------\n" 
for i in range(height-15):
                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "|            |\n"
end_scene += "|            |\n"                                      
for i in range(height-12):                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "--------------"
print(end_scene)
sleep(1)


















system('cls')
end_scene="--------------\n" 
for i in range(height-15):
                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "| idea from  |\n"
end_scene += "|            |\n"
end_scene += "|  Nintendo  |\n"                                      
for i in range(height-13):                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "--------------"
print(end_scene)
sleep(1)

system('cls')
end_scene="--------------\n" 
for i in range(height-15):
                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "|            |\n"
end_scene += "|            |\n"                                      
for i in range(height-12):                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "--------------"
print(end_scene)
sleep(1)





















        

system('cls')
end_scene="--------------\n" 
for i in range(height-15):
                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "|  special   |\n"
end_scene += "|   thanks   |\n"
end_scene += "|            |\n"  
end_scene += "|  my liver  |\n"                                      
for i in range(height-14):                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "--------------"
print(end_scene)
sleep(1)

system('cls')
end_scene="--------------\n" 
for i in range(height-15):
                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "|            |\n"
end_scene += "|            |\n"                                      
for i in range(height-12):                    
    end_scene += "|"
    for j in array:                          
        end_scene += " "                        
    end_scene += "|"+"\n"
end_scene += "--------------"
print(end_scene)
sleep(1)










game_end = False
while True:

    wait_for_s = False
    system('cls')        
    end_scene="--------------\n"
    end_scene += "|        v1.1|\n"
    for i in range(height-16):                        
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "|   TETRIS   |\n"
    end_scene += "|            |\n"
    end_scene += "|            |\n"   
    end_scene += "|     <s>    |\n"                                      
    for i in range(height-14):                    
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "--------------"
    print(end_scene)


    for i in range(10):
        sleep(0.03)
        if kbhit():
            if ord(getch()) == 115:
                wait_for_s = True
                break
    if wait_for_s == True:
        break


    system('cls')        
    end_scene="--------------\n"
    end_scene += "|        v1.1|\n"
    for i in range(height-16):                        
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "|   TETRIS   |\n"
    end_scene += "|            |\n"                                      
    for i in range(height-12):                    
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "--------------"
    print(end_scene)


    for i in range(10):
        sleep(0.03)
        if kbhit():
            if ord(getch()) == 115:
                wait_for_s = True
                break
    if wait_for_s == True:
        break









while True:

    wait_for_s = False
    system('cls')
    end_scene="--------------\n" 
    for i in range(height-17):
                        
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "|  controls: |\n"
    end_scene += "|  a left    |\n"
    end_scene += "|  d right   |\n"
    end_scene += "|  s down    |\n"
    end_scene += "| o/p spin   |\n"
    end_scene += "|            |\n"
    end_scene += "|    <s>     |\n"
    end_scene += "|            |\n"

    for i in range(height-16):                    
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "--------------"
    print(end_scene)


    for i in range(10):
        sleep(0.03)
        if kbhit():
            if ord(getch()) == 115:
                wait_for_s = True
                break
    if wait_for_s == True:
        break


    system('cls')
    end_scene="--------------\n" 
    for i in range(height-17):
                        
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "|  controls: |\n"
    end_scene += "|  a left    |\n"
    end_scene += "|  d right   |\n"
    end_scene += "|  s down    |\n"
    end_scene += "| o/p spin   |\n"
    end_scene += "|            |\n"
    end_scene += "|            |\n"
    end_scene += "|            |\n"

    for i in range(height-16):                    
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "--------------"
    print(end_scene)


    for i in range(10):
        sleep(0.03)
        if kbhit():
            if ord(getch()) == 115:
                wait_for_s = True
                break
    if wait_for_s == True:
        break












while True:

    wait_for_s = False
    system('cls')        
    end_scene="--------------\n"
    end_scene += "|        v1.1|\n"
    for i in range(height-16):                        
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "| use aimer? |\n"
    end_scene += "| (unstable) |\n"
    end_scene += "|            |\n"   
    end_scene += "|    <y/n>   |\n"                                      
    for i in range(height-14):                    
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "--------------"
    print(end_scene)


    for i in range(10):
        sleep(0.03)
        if kbhit():
            keyboard = ord(getch())
            if keyboard == 121:
                wait_for_s = True
                check_aim = True
                break
            elif keyboard == 110:
                wait_for_s = True
                check_aim = False
                break 
    if wait_for_s == True:
        break


    system('cls')        
    end_scene="--------------\n"
    end_scene += "|        v1.1|\n"
    for i in range(height-16):                        
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "| use aimer? |\n"
    end_scene += "| (unstable) |\n"
    end_scene += "|            |\n"   
    end_scene += "|            |\n"                                       
    for i in range(height-14):                    
        end_scene += "|"
        for j in array:                          
            end_scene += " "                        
        end_scene += "|"+"\n"
    end_scene += "--------------"
    print(end_scene)


    for i in range(10):
        sleep(0.03)
        if kbhit():
            keyboard = ord(getch())
            if keyboard == 121:
                wait_for_s = True
                check_aim = True
                break
            elif keyboard == 110:
                wait_for_s = True
                check_aim = False
                break
    if wait_for_s == True:
        break


      

def cube(x,y,head,type):
    if head==1:
        if type=="i":
            array[x-1][y]=1
            array[x][y]=1
            array[x+1][y]=1
            array[x+2][y]=1
        if type=="r":
            array[x+1][y]=1
            array[x][y]=1
            array[x][y+1]=1
            array[x][y+2]=1
        if type=="l":
            array[x-1][y]=1
            array[x][y]=1
            array[x][y+1]=1
            array[x][y+2]=1
        if type=="z":
            array[x-1][y]=1
            array[x][y]=1
            array[x][y+1]=1
            array[x+1][y+1]=1
        if type=="s":
            array[x-1][y+1]=1
            array[x][y+1]=1
            array[x][y]=1
            array[x+1][y]=1
        if type=="o":
            array[x-1][y+1]=1
            array[x-1][y]=1
            array[x][y+1]=1
            array[x][y]=1
        if type=="t":
            array[x-1][y]=1
            array[x][y]=1
            array[x][y+1]=1
            array[x+1][y]=1
            
                
    if head==2:
        if type=="i":
            array[x][y-1]=1
            array[x][y]=1
            array[x][y+1]=1
            array[x][y+2]=1
        if type=="r":
            array[x-1][y]=1
            array[x][y]=1
            array[x+1][y]=1
            array[x+1][y+1]=1
        if type=="l":
            array[x-1][y+1]=1
            array[x][y+1]=1
            array[x+1][y+1]=1
            array[x+1][y]=1
        if type=="z":
            array[x+1][y]=1
            array[x+1][y+1]=1
            array[x][y+1]=1
            array[x][y+2]=1
        if type=="s":
            array[x-1][y]=1
            array[x-1][y+1]=1
            array[x][y+1]=1
            array[x][y+2]=1
        if type=="o":
            array[x-1][y+1]=1
            array[x-1][y]=1
            array[x][y+1]=1
            array[x][y]=1
        if type=="t":
            array[x+1][y]=1
            array[x+1][y+1]=1
            array[x+1][y+2]=1
            array[x][y+1]=1 
            
            
    if head==3:
        if type=="i":
            array[x-1][y]=1
            array[x][y]=1
            array[x+1][y]=1
            array[x+2][y]=1
        if type=="r":
            array[x][y]=1
            array[x][y+1]=1
            array[x][y+2]=1
            array[x-1][y+2]=1
        if type=="l":
            array[x][y]=1
            array[x][y+1]=1
            array[x][y+2]=1
            array[x+1][y+2]=1
        if type=="z":
            array[x-1][y]=1
            array[x][y]=1
            array[x][y+1]=1
            array[x+1][y+1]=1
        if type=="s":
            array[x-1][y+1]=1
            array[x][y+1]=1
            array[x][y]=1
            array[x+1][y]=1
        if type=="o":
            array[x-1][y+1]=1
            array[x-1][y]=1
            array[x][y+1]=1
            array[x][y]=1
        if type=="t":
            array[x-1][y+1]=1
            array[x][y+1]=1
            array[x+1][y+1]=1
            array[x][y]=1 
            
            
    if head==4:
        if type=="i":
            array[x][y-1]=1
            array[x][y]=1
            array[x][y+1]=1
            array[x][y+2]=1
        if type=="r":
            array[x-1][y]=1
            array[x-1][y+1]=1
            array[x][y+1]=1
            array[x+1][y+1]=1
        if type=="l":
            array[x][y]=1
            array[x+1][y]=1
            array[x+2][y]=1
            array[x][y+1]=1
        if type=="z":
            array[x+1][y]=1
            array[x+1][y+1]=1
            array[x][y+1]=1
            array[x][y+2]=1
        if type=="s":
            array[x-1][y]=1
            array[x-1][y+1]=1
            array[x][y+1]=1
            array[x][y+2]=1
        if type=="o":
            array[x-1][y+1]=1
            array[x-1][y]=1
            array[x][y+1]=1
            array[x][y]=1
        if type=="t":
            array[x-1][y]=1
            array[x-1][y+1]=1
            array[x-1][y+2]=1
            array[x][y+1]=1                 

def display():
    global check_aim
    if check_aim == True:
        aim_x = []
        aim_y = []    
        for i in range(height - pos_y):
            if array[pos_x][i+pos_y] == 0:
                array[pos_x][i+pos_y]=3
                aim_x.append(pos_x)
                aim_y.append(i+pos_y)    
    system('cls')
    disp="--------------\n"
    if score <= 9:    
        disp += "|     score:"
    if score >= 10:
        disp += "|    score:"
    disp+=str(score)    
    disp+="|\n"
    for i in range(height-1):        
        disp += "|"
        for j in array:
           
            if j[i+1] == 0:
                if i+1 <= 3:
                    disp += "."
                else:
                    disp += " "
            if j[i+1] == 1:
                disp +="X"
            if j[i+1] == 2:
                disp += "X"
            if j[i+1] == 3:
                disp+="."
        disp += "|"+"\n"
    disp += "--------------"
    print(disp)

    if check_aim == True:
        for i in range(len(aim_x)):
            if array[aim_x[i]][aim_y[i]] == 3:
                array[aim_x[i]][aim_y[i]] = 0 


                         


while True:#遊戲循環

    while True:   #釋放循環      

        spawn_list=["i","l","r","s","o","z","t"]
        now_type = spawn_list[int(uniform(0,6.5))]
        cube(5,1,1,now_type)
        pos_y = 1
        now_head = 1
        shake = 0

        pos_x = 5
        hit=0
        lim_t = 0.4
        while x==1:       #掉落循環            
            display()
            t = 0            
            while t<=lim_t:
                if lim_t ==0:
                    break
                sleep(0.01)
                t+=0.01
                left_hit = 0
                right_hit = 0        
                for i in range(height):
                    if list1[i] == 1:
                        left_hit = 1
                    if list12[i] == 1:
                        right_hit = 1
                if kbhit():
                    keyboard = ord(getch())
                    
                    if keyboard == 97:  #"a"         
                        if left_hit == 0:
                            for i in range(len(array)-1):                    
                                for j in range(height):                       
                                    if array[i+1][height-j-1]==1:
                                        array[i+1][height-j-1]=0
                                        array[i][height-j-1]=1
                        display()
                        pos_x+=-1
                                          
                    elif keyboard == 100:  #"d"
                        if right_hit == 0:
                            for i in range(len(array)):
                                for j in range(height):                    
                                    if array[len(array)-i-1][height-j-1] == 1:
                                        array[len(array)-i-1][height-j-1]=0
                                        array[len(array)-i][height-j-1]=1
                        pos_x+=1
                        display()




                   
                    elif keyboard == 111:  #"o"           
                                                    
                        for i in range(len(array)):
                            for j in range(height):                    
                                if array[len(array)-i-1][height-j-1] == 1:                            
                                    array[len(array)-i-1][height-j-1]=0                    
                        if now_head == 1:
                            cube(pos_x,pos_y,4,now_type)
                            now_head = 4                        
                        elif now_head == 2:
                            sleep(1)
                            cube(pos_x,pos_y,1,now_type)
                            now_head = 1                        
                        elif now_head == 3:
                            sleep(1)
                            cube(pos_x,pos_y,2,now_type)
                            now_head = 2                        
                        elif now_head == 4:
                            sleep(1)
                            cube(pos_x,pos_y,3,now_type)
                            now_head = 3
                        shake = 1
                        
                    elif keyboard == 112:  #"p"
                            
                        for i in range(len(array)):
                            for j in range(height):                    
                                if array[len(array)-i-1][height-j-1] == 1:
                                    array[len(array)-i-1][height-j-1]=0

                        if now_head == 1:
                            cube(pos_x,pos_y,2,now_type)
                            now_head = 2
                        elif now_head == 2:
                            cube(pos_x,pos_y,3,now_type)
                            now_head = 3
                        elif now_head == 3:
                            cube(pos_x,pos_y,4,now_type)
                            now_head = 4
                        elif now_head == 4:
                            cube(pos_x,pos_y,1,now_type)
                            now_head = 1
                        single=1



                    elif keyboard == 115:  #"s"
                        lim_t = 0
                    
                







            
            for i in array:            
                for j in range(height):                             
                    if i[height-1] ==1 : 
                        hit=1      
                        for i in array:            
                            for j in range(height):              
                                if i[height-1-j] == 1 :
                                    i[(height-1-j)]=2     
                        
                        break
                    if i[height-1-j] == 1 :
                        
                        if i[height-j] ==2:                                            
                            hit=1
                            
            if hit ==1:
                break               
            if shake == 0:
                for i in array:
                    for j in range(height):
                        if i[(height-1-j)] ==1:   
                             
                            i[(height-j)] =1 
                            i[(height-1-j)]=0
            else:
                shake = 0
                                
                           
            
            pos_y+=1            
        if hit==1:
            for i in array:            
                for j in range(height):              
                    if i[height-1-j] == 1 :
                        i[(height-1-j)]=2
                      
                              
                        
      
            #判斷1下面有沒有2v
                #沒有:繼續v
                #有:breakv

            #將1下移一格v
        to_dump = []
        for i in range(height):
            
            filled=1
            for j in array:
                if j[i] !=2 :
                    filled=0
            if filled==1:
                for j in range(3):
                    for l in array:
                        l[i]=1
                    display()
                    sleep(0.1)
                    for l in array:
                        l[i]=0
                    display()
                    sleep(0.1)
                        
            if filled==1:          
                    for l in range(i):
                        
                        
                        for k in array:          
                                if k[i-l-1] ==2:       
                                    k[i-l-1] =0
                                    k[i-l]=2
                    score+=1
          





                                    
        for i in array:
            if i[0]==2 or i[1]==2 or i[2]==2 or i[3]==2: 
                system('cls')
                end_scene="--------------\n" 
                for i in range(height-15):
                    
                    end_scene += "|"
                    for j in array:                          
                        end_scene += " "
                        
                    end_scene += "|"+"\n"
                end_scene += "|  GameOver  |\n"
                
                
                        
                for i in range(height-11):
                    
                    end_scene += "|"
                    for j in array:                          
                        end_scene += " "
                        
                    end_scene += "|"+"\n"
                end_scene += "----------------"
                print(end_scene)
                game_end = True
                sleep(3)



                system('cls')
                end_scene="--------------\n" 
                for i in range(height-15):
                    
                    end_scene += "|"
                    for j in array:                          
                        end_scene += " "
                        
                    end_scene += "|"+"\n"
                end_scene += "|cuz U lose, |\n"
                end_scene += "|self destroy|\n"
                end_scene += "|  in:  3    |\n"
                
                
                        
                for i in range(height-13):
                    
                    end_scene += "|"
                    for j in array:                          
                        end_scene += " "
                        
                    end_scene += "|"+"\n"
                end_scene += "----------------"
                print(end_scene)
                game_end = True
                sleep(1)


                system('cls')
                end_scene="--------------\n" 
                for i in range(height-15):
                    
                    end_scene += "|"
                    for j in array:                          
                        end_scene += " "
                        
                    end_scene += "|"+"\n"
                end_scene += "|cuz U lose, |\n"
                end_scene += "|self destroy|\n"
                end_scene += "|  in:  2    |\n"
                
                
                        
                for i in range(height-13):
                    
                    end_scene += "|"
                    for j in array:                          
                        end_scene += " "
                        
                    end_scene += "|"+"\n"
                end_scene += "----------------"
                print(end_scene)
                game_end = True
                sleep(1)


                system('cls')
                end_scene="--------------\n" 
                for i in range(height-15):
                    
                    end_scene += "|"
                    for j in array:                          
                        end_scene += " "
                        
                    end_scene += "|"+"\n"
                end_scene += "|cuz U lose, |\n"
                end_scene += "|self destroy|\n"
                end_scene += "|  in:  1    |\n"
                
                
                        
                for i in range(height-13):
                    
                    end_scene += "|"
                    for j in array:                          
                        end_scene += " "
                        
                    end_scene += "|"+"\n"
                end_scene += "----------------"
                print(end_scene)
                game_end = True
                sleep(1)


                
                break
            
        if game_end == True:
            break
    if game_end == True:
        break

      
                    
                      
        #判斷有沒有可消橫排v
            #有:消除動畫,以上下移v
            #沒:跳過v
        #判斷有無超過頂
            #有:break
            #無:跳過       
        
        

    
    
    
    
    
