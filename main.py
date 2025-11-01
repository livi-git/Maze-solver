class Action():
    def __init__(self, parent, action, x, y):
        self.parent = parent
        self.action = action
        self.row = x
        self.column = y

    def toString(self):
        print("Row : "+str(self.row)+"\nColumn : "+str(self.column))            
        
class Main():
    def __init__(self, filename):
        with open(filename,'r') as file:
            self.maze=[]
            for line in file:
                self.maze.append([char for char in line.rstrip("\n")])
        self.availableActions=[]
        self.rows = len(self.maze)-1
        self.columns = len(self.maze[0])-1
        self.showMaze()

    def start(self):
        initAction = Action(None, None, 4, 0)
        self.availableActions.append(initAction)
        self.findAvailableActions()

    def findAvailableActions(self):
        completed = False
        while self.availableActions:
            final = self.findAllActionsForAction(self.availableActions[0])
            if isinstance(final, Action):
                completed = True
                break
        if completed:
            print("Reached")
            self.updateMaze(final)
            self.showMaze()
        else:
            print("No path available")

    def findAllActionsForAction(self, action):
        isCompleted = self.isCompleted(action)
        if isCompleted:
            return isCompleted
        
        #check left
        if self.isValidAction(action.row, action.column-1, action.parent):
            self.availableActions.append(Action(self.availableActions[0],"left", action.row, action.column-1))
        #check right
        if self.isValidAction(action.row, action.column+1, action.parent):
            self.availableActions.append(Action(self.availableActions[0],"right", action.row, action.column+1))
        #check top
        if self.isValidAction(action.row-1, action.column, action.parent):
            self.availableActions.append(Action(self.availableActions[0],"top", action.row-1, action.column))
        #check bottom
        if self.isValidAction(action.row+1, action.column, action.parent):
            self.availableActions.append(Action(self.availableActions[0],"bottom", action.row+1, action.column))
        self.availableActions.pop(0)

    def isValidAction(self, row, column, parent):
        if (row<0 or column<0 or row > self.rows or column > self.columns or (parent and (parent.row == row and parent.column == column))):
            return False
        elif self.maze[row][column] == "#":
            return False
        else:
            return True

    def isCompleted(self, action):
        if self.maze[action.row][action.column] == "B":
            return action
        else:
            return False
        
    def updateMaze(self, action):
        if self.maze[action.row][action.column] != "B" and self.maze[action.row][action.column] != "A":
            self.maze[action.row][action.column] = "*"
        elif action.parent == None:
            return None
        self.updateMaze(action.parent)
        
    def showMaze(self):
        for row in self.maze:
            print("-"*(len(row)*3))
            for column in range(len(row)*3):
                if column%3 !=0:
                    print(" ", end="")
                else:
                    print('\033[31m'+row[column//3]+'\033[0m' if row[column//3]=="*" else '\033[32m'+row[column//3]+'\033[0m' if row[column//3]=="A" or row[column//3]=="B" else row[column//3], end="")
            print("")
        
            



m=Main("maze_input.txt")
m.start()
