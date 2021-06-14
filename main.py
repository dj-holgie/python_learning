# write your code here
selection = "_________"
input_list = [selection[0], selection[1], selection[2], selection[3], selection[4], selection[5], selection[6], selection[7], selection[8]]
input_matrix = [[selection[0],selection[1],selection[2]],[selection[3],selection[4],selection[5]],[selection[6],selection[7],selection[8]]]

def show_grid():
    print("---------")
    print("| " + input_matrix[0][0] + " " + input_matrix[0][1] + " " + input_matrix[0][2] + " |")
    print("| " + input_matrix[1][0] + " " + input_matrix[1][1] + " " + input_matrix[1][2] + " |")
    print("| " + input_matrix[2][0] + " " + input_matrix[2][1] + " " + input_matrix[2][2] + " |")
    print("---------")

show_grid() 
game_running = True

def make_a_move(player): 
    global game_running
    while True:
       try:
         move_x, move_y = input("Enter the coordinates:").split()       
         move_x = int(move_x)
         move_y = int(move_y) 
       except ValueError:
         print("You should enter numbers!")
         continue
       if move_x > 3 or move_y > 3 or move_x < 1 or move_y < 1:
         print("Coordinates should be from 1 to 3!")    
         continue
       elif input_matrix[move_x-1][move_y-1] != '_':
         print("This cell is occupied! Choose another one!")    
         continue         
       else:
         break     
    input_matrix[move_x-1][move_y-1] = player    
    show_grid()
    if check_winner(player) == True:
      print("Player", player, "wins")   
      game_running = False
      return
    if sum(x.count('_') for x in input_matrix) == 0:
        print("Draw")
        game_running = False
        return
    print(player, "turn finished")
    return
  
def check_winner(name):
    if input_matrix[0].count(name) == 3:        
        return True
    elif input_matrix[1].count(name) == 3:        
        return True
    elif input_matrix[2].count(name) == 3:        
        return True
    elif input_matrix[0][0] == name and input_matrix[1][0] == name and input_matrix[2][0] == name:        
        return True
    elif input_matrix[0][1] == name and input_matrix[1][1] == name and input_matrix[2][1] == name:    
        return True
    elif input_matrix[0][2] == name and input_matrix[1][2] == name and input_matrix[2][2] == name:  
        return True
    elif input_matrix[0][0] == name and input_matrix[1][1] == name and input_matrix[2][2] == name:
        return True
    elif input_matrix[2][0] == name and input_matrix[1][1] == name and input_matrix[0][2] == name:    
        return True
    return False

while game_running == True:
    make_a_move('X')
    if game_running == True:
        make_a_move('O')
