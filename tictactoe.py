import random
def printbox(list) :
    i=0
    while i<3 :
        print(list[i][0],"|",list[i][1],"|",list[i][2])
        if i<2 :
            print("_"*6)
            print("")
        i+=1  

#checking the winner function 
def win(p) :
   w1=0
   w2=[0,0,0]
   w3=[0,0,0]
   w4=0
   i=0
   if [0,2] in p:
      w4+=1
   if [1,1] in p:
      w4+=1
   if [2,0] in p:
      w4+=1        

   i=0
   while i<3 :
      if [i,i] in p :
         w1+=1
      i+=1     
   i=0     
   while i<3 :
      j=0
      while j<3 :
        if [i,j] in p:
           w2[i]+=1
        j+=1    
      i+=1    
   i=0      
   while i<3 :
      j=0
      while j<3 :
         if [j,i] in p:
            w3[i]+=1
         j+=1
      i+=1           
   if (w1==3) or (3 in w2) or (3 in w3) or (w4==3) :
      return 1  
   return 0   
    




def tictactoe(t):
    list=[["","",""],["","",""],["","",""]]   
    printbox(list)
    count=0
    list1=[]
    p1=[]
    p2=[]
    if t==0 :
      print("welcome to tic tac toe")
    print("Your coin is X and computer coin is O")
    while count<5 :
        i=int(input("Enter the row(0-2):"))
        j=int(input("Enter the column(0-2):"))
        
        new_row=[i,j]
        if count>0 :
           while (new_row in list1) or (new_row[0]>2) or (new_row[0]<0) or (new_row[1]>2) or (new_row[1]<0):
              i=int(input("Enter the correct input in row(0-2):"))
              j=int(input("Enter the correct input in column(0-2):"))
              new_row=[i,j]
              
        list[i][j]="X"
        list1.append(new_row)
        p1.append(new_row)
        printbox(list)
        if count>=2 :
            x=win(p1)
            y=win(p2) 
            if x==1:
              print("You Win..!! :)")
              return 0
            if y==1:
              print("You Lose....!! :(")
              return 0
        print("Now it's computer's turn\n")
        i=0
        j=0
        if count<4 :
          while new_row in list1 :
            i+=random.randint(0,2)
            j+=random.randint(0,2)
            i%=3
            j%=3
            new_row=[i,j]    
        list[i][j]="O"    
        list1.append(new_row)
        p2.append(new_row)
        printbox(list) 
        count+=1 
        
    print("Match drawn :|")
    return 0

t=0    
x=1
while x==1  :
   tictactoe(t)
   x=int(input("Do you want to play agian(0-No,1-Yes)??:"))
   t+=1
print("Thanks for playing :)")
