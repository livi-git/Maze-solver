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
        print(self.maze)
        self.availableActions=[]
        self.rows = len(self.maze)-1
        self.columns = len(self.maze[0])-1

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
        else:
            print("No path available")

    def findAllActionsForAction(self, action):
        print("findAllActionsForAction :: enter")
        isCompleted = self.isCompleted(action)
        if isCompleted:
            print(len(self.availableActions))
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
        print("findAllActionsForAction :: exit")

    def isValidAction(self, row, column, parent):
        print("isValidAction :: enter")
        if (row<0 or column<0 or row > self.rows or column > self.columns or (parent and (parent.row == row and parent.column == column))):
            print("isValidAction :: exit 1")
            return False
        elif self.maze[row][column] == "#":
            print("isValidAction :: exit 2")
            return False
        else:
            print("isValidAction :: exit 3")
            return True

    def isCompleted(self, action):
        print("isCompleted :: enter")
        if self.maze[action.row][action.column] == "B":
            print("isCompleted :: exit 1")
            return action
        else:
            print("isCompleted :: exit 2")
            return False



m=Main("maze_input.txt")
m.start()
