
num =  [1,2,3,4,5,6,7,8,9]
current_marker='X'
current_player='1'
def print_board():
        
        line1="{}|{}|{}"
        print(line1.format(num[0],num[1],num[2]))
        line2="{}|{}|{}"
        print(line1.format(num[3],num[4],num[5]))
        line3="{}|{}|{}"
        print(line1.format(num[6],num[7],num[8]))
        
        
        

def change():
    global current_marker
    global current_player
    if current_marker =='X':
        current_marker = 'O'
             
    else:
         current_marker= 'X'
        
    if current_player =='1':
        current_player= '2'
             
    else:
        current_player= '1'  
        
    print("PLAYER("+current_player+") play your move")  
    

def winner():
    if num[0]==num[1] and num[1]==num[2]:
        return True
    if num[3]==num[4] and num[4]==num[5]:
        return True
    if num[5]==num[6] and num[6]==num[7]:
        return True
    if num[0]==num[4] and num[4]==num[8]:
        return True
    if num[2]==num[4] and num[4]==num[6]:
        return True
    if num[0]==num[3] and num[3]==num[6]:
        return True
    if num[1]==num[4] and num[4]==num[7]:
        return True
    if num[2]==num[5] and num[5]==num[8]:
        return True


print_board()
print("PLAYER(1) marker is : 'X' and PLAYER(2) marker is : 'O'  ")
marker=input("PLAYER("+current_player+") : choose marker ")
current_marker=marker
i=1
while i<=9:
    move=(input("Enter the move : "))
    if int(move)>9:
        print("Enter a valid move between 1-9 : ")
        i-=1
        continue
    if num[int(move)-1]=='X'or num[int(move)-1]=='O':
        print("Already chosen....move again")
        i-=1
        continue
    num[(int(move))-1]=current_marker
    print_board()
    if winner():
      print("congrats you won!")
      break
    if not winner() and i==9:
      print("match draw...Try again")
      break
    change()
    i+=1

