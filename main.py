import tkinter
import random

#'game0ver' will tell the computer when the game ends. It must be set to False for the game to begin with
game0ver = False
score = 0
squaresToClear = 0

#when you paly the game, the computer will
def play_bombdodger():
#create a body-trapped field
  create_bombfield(bombfield)
#bring up tkinter graphics window and daw the field in it
  window = tkinter.Tk()
  layout_window(window) 
  window.title("Minesweeper")
#run the game
  window.mainloop()

#[] creates a list called 'bombfield'
bombfield = []
def create_bombfield(bombfield):
#global tells the computer to use 'global' varibles which you set up at the start
  global squaresToClear
#this for loop run ten times
  for row in range (0, 20):
#creating an empty lits(or row) each time
    rowList = []
    for column in range(0,20):
#inside every row list, another for loop adds 10 numbers (or columns)  
#this generates a random number from 1-100. if the number is less then 20, the computer adds a 1 (bomb) to the 'rowList'
      if random.randint(1, 100) < 20:
        rowList.append(1)
      else: 
#otherwise, it adds a 0 (safe square) to the 'rowList' AND adds 1 to 'squaresToClear'
        rowList.append(0)
        squaresToClear = squaresToClear + 1
#this attaches each fnished 'rowList' to the original list
    bombfield.append(rowList)
#it will display the list in the windows shell  
  printfield(bombfield)

def printfield(bombfield):
  for rowList in bombfield:
#will display each 'rowList' in the field in turn
    print(rowList)

#the tkinter window pops up when you sen the game
def layout_window(window):
#the outer for loop goes down the row
  for rowNumber, rowList in enumerate(bombfield):
  #the inner for loop goes through the columns
    for columnNumber, columnEntry in enumerate(rowList):
#enumerate() finds the index numbers for the items in each 'rowList'fand pairs each index number wit hits item, this makes it easier for the computer to look up parts of the list 
      
#if the random number is less then 25, the square will be darkgreen
      if random.randint(1, 100) <25:
        square = tkinter.Label(window, text = "    ", bg = "darkgreen")
#elif the number is over 75 then the square will be sea green
      elif random.randint(1, 100) > 75:
        square = tkinter.Label(window, text = "    ", bg = "seagreen")
#else for anyother number, the square will just be green
      else: 
#tkinter.Label() creates a label(which forms the square)
#windows liks the square to the tk window
#the 4 spaces in the parameters will be the width of the square
#the grid belongs to the square, grid() fundction has alot of built-in parameters,
        square = tkinter.Label(window, text = "    ", bg = "green")

      square.grid(row = rowNumber, column = columnNumber)
      #bind() links the event (the mouse-click) and the computer's response (a new function called click()) to the square 
      #each time you click the function named on_click()  will run      
      square.bind("<Button-1>", on_click)

#play_bombdodger()
#event refers t othe clikc on the sqaure  
def on_click(event): 
#the global command allows this function to change these variables, tho the variables were created outside this function
  global score
  global game0ver
  global squaresToClear
  square = event.widget
#square.grid_info() pulls out information about the sqauare from the grid
#int makes sure the computer treats that imformation as a number
  row = int (square.grid_info()["row"])
  column = int(square.grid_info()["column"])
#cget("text") looks up an existing text
  currentText = square.cget("text")
  if game0ver == False:
#checks for a bomb (1 = mine, 0 = safe)
    if bombfield[row][column] == 1:
#ends the game
      game0ver = True 
      square.config(bg = "red")
#will display your socre which is the number of squares clicked before you died
      print("Game Over! You hit a bomb!")
      print("Your score was: ", score)

#if the four spaces in the paramaters still contians then the sqaure has not yet been clicked
    elif currentText == "    " :
      square.config(bg = "brown")
      totalBombs = 0

      if row < 19:
#if there is a bomb below, the computer adds 1 to the total number of bombs
        if bombfield[row+1][column] == 1:
          totalBombs = totalBombs + 1
            
      if row > 0:
        if bombfield[row-1][column] ==1:
          totalBombs = totalBombs + 1
          
      if column > 0:
        if bombfield[row][column-1] == 1:
          totalBombs = totalBombs + 1
            
      if column < 19:
        if bombfield[row][column+1] == 1:
          totalBombs = totalBombs + 1
            
      if row > 0 and column > 0:
        if bombfield[row-1][column-1] ==1:
          totalBombs = totalBombs +1
            
      if row < 19 and column > 0:
        if bombfield[row+1][column-1] ==1:
          totalBombs = totalBombs + 1
            
      if row > 0 and column < 19:
        if bombfield[row-1][column+1] == 1:
          totalBombs = totalBombs + 1
          
      if row < 19 and column < 19:
        if bombfield[row+1][column+1] == 1:
          totalBombs = totalBombs + 1

#the numbers of  bombs around the clicked square into a string, using the str(), and displays it on the square itself
      square.config(text = " " + str(totalBombs) + " ")
      squaresToClear = squaresToClear - 1
      score = score + 1
      if squaresToClear == 0:
        game0ver = True
        print ("Well done! You found all the safe squares!")
        print("Your score was:", score)

play_bombdodger()