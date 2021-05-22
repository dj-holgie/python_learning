# Basic Tic Tac Toe for hyperskill.org learning
selection = input("Enter cells:")
print("---------")
print("| " + selection[0] + " " + selection[1] + " " + selection[2] + " |")
print("| " + selection[3] + " " + selection[4] + " " + selection[5] + " |")
print("| " + selection[6] + " " + selection[7] + " " + selection[8] + " |")
print("---------")
input_list = [selection[0], selection[1], selection[2], selection[3], selection[4], selection[5], selection[6], selection[7], selection[8]]
input_matrix = [[selection[0],selection[1],selection[2]],[selection[3],selection[4],selection[5]],[selection[6],selection[7],selection[8]]]
#print(input_matrix)

# print(input_matrix)
# [['X', 'X', 'X'], ['O', 'O', '_'], ['_', 'O', '_']]
count_x = input_list.count('X')
count_o = input_list.count('O')
count__ = input_list.count('_')

def check_impossible():
    if check_winner('X') == 'X' and check_winner('O') == 'O':
      return "Impossible"
    elif count_x - count_o > 1 or count_o - count_x > 1:
      print(count_x,count_o)
      return "Impossible"

def check_winner(name):
    global winner
    if input_matrix[0].count(name) == 3:
        winner = name
        return name
    elif input_matrix[1].count(name) == 3:
        winner = name
        return name
    elif input_matrix[2].count(name) == 3:
        winner = name
        return name
    elif input_matrix[0][0] == name and input_matrix[1][0] == name and input_matrix[2][0] == name:
        winner = name
        return name
    elif input_matrix[0][1] == name and input_matrix[1][1] == name and input_matrix[2][1] == name:
        winner = name
        return name
    elif input_matrix[0][2] == name and input_matrix[1][2] == name and input_matrix[2][2] == name:
        winner = name
        return name
    elif input_matrix[0][0] == name and input_matrix[1][1] == name and input_matrix[2][2] == name:
        winner = name
        return name
    elif input_matrix[2][0] == name and input_matrix[1][1] == name and input_matrix[0][2] == name:
        winner = name
        return name

if check_impossible() == 'Impossible':
    print("Impossible")
elif check_winner('X') == 'X' or check_winner('O') == 'O':
    print (f'{winner} wins')
elif count__ > 0:
    print("Game not finished")
else:
    print("Draw")

