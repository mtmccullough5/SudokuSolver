#Sudoku Solver


def SudokuSolver(PuzzleState):
    # Main Solver
##    while PuzzleSum < 405
##        for number in Numbers
##            PuzzleState = CheckNum(self)
    
    def TruthMaker(ArrayStates, Number):
        TruthMatrix = [
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True]]
        PuzzleState = ArrayStates[0]
        HorzState = ArrayStates[0]
        VertState = ArrayStates[1]
        BlockState = ArrayStates[2]
        
        ## Check Vertival and Horizontal Lines
        for y in range(9):
            for x in range(9):
                if Number in HorzState[x] or Number in VertState[y]:
                    TruthMatrix[x][y] = False

        ## Check Blocks           
        for x in range(3):
            for y in range(3):
                if Number in BlockState[0]:
                    TruthMatrix[x][y] = False
        for x in range(3,6):
            for y in range(3):
                if Number in BlockState[1]:
                    TruthMatrix[x][y] = False
        for x in range(6,9):
            for y in range(3):
                if Number in BlockState[2]:
                    TruthMatrix[x][y] = False
        for x in range(3):
            for y in range(3,6):
                if Number in BlockState[3]:
                    TruthMatrix[x][y] = False
        for x in range(3,6):
            for y in range(3,6):
                if Number in BlockState[4]:
                    TruthMatrix[x][y] = False
        for x in range(6,9):
            for y in range(3,6):
                if Number in BlockState[5]:
                    TruthMatrix[x][y] = False
        for x in range(3):
            for y in range(6,9):
                if Number in BlockState[6]:
                    TruthMatrix[x][y] = False
        for x in range(3,6):
            for y in range(6,9):
                if Number in BlockState[7]:
                    TruthMatrix[x][y] = False
        for x in range(6,9):
            for y in range(6,9):
                if Number in BlockState[8]:
                    TruthMatrix[x][y] = False

        ## Check if a number is already there
        for x in range(9):
            for y in range(9):
                if PuzzleState[x][y] > 0:
                    TruthMatrix[x][y] = False
        return TruthMatrix
    
    def Indexer(PuzzleState):
        # PuzzleState is identical to Horizontal Arrays
        HorzState = PuzzleState
        # Vertical State
        VertState = []
        for x in range(9):
            VertArr = []
            for y in range(9):
                VertArr.append(PuzzleState[y][x])
            VertState.append(VertArr)
        # Block State
        b1 = []
        b2 = []
        b3 = []
        b4 = []
        b5 = []
        b6 = []
        b7 = []
        b8 = []
        b9 = []
        for x in range(3):
            for y in range(3):
                b1.append(PuzzleState[x][y])
            for y in range(3,6):
                b2.append(PuzzleState[x][y])
            for y in range(6,9):
                b3.append(PuzzleState[x][y])
        for x in range(3,6):
            for y in range(3):
                b4.append(PuzzleState[x][y])
            for y in range(3,6):
                b5.append(PuzzleState[x][y])
            for y in range(6,9):
                b6.append(PuzzleState[x][y])
        for x in range(6,9):
            for y in range(3):
                b7.append(PuzzleState[x][y])
            for y in range(3,6):
                b8.append(PuzzleState[x][y])
            for y in range(6,9):
                b9.append(PuzzleState[x][y])
        BlockState = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
        return [HorzState,VertState,BlockState]

    def MatrixSum(PuzzleState):
        PuzzleSum = 0
        for arr in PuzzleState:
            PuzzleSum += sum(arr)
        return PuzzleSum

    def FindArray(PuzzleState, TruthMat):
        # Create Truth Arrays
        TruthArrays = Indexer(TruthMat)
        HorzState = TruthArrays[0]
        VertState = TruthArrays[1]
        BlockState = TruthArrays[2]
        
        # Check arrays
        for x in range(9):
            if HorzState[x].count(True) == 1:
                return HorzReplace(PuzzleState,x)
            if VertState[x].count(True) == 1:
                return [x,"vert"]
            if BlockState[x].count(True) == 1:
                return [x,"block"]
        
    def HorzReplace(PuzzleState, x):
        # This array is equal to the PuzzleState
        return PuzzleState


    def VertReplace(PuzzleState, x):
        # This array I need to switch Indices
        return PuzzleState

    def BlockReplace(PuzzleState, x):
        # Special Indexing requirements
        return PuzzleState
    
    ArrayStates = Indexer(PuzzleState)
    PuzzleSum = MatrixSum(PuzzleState)
    TruthMat = TruthMaker(ArrayStates, 6)
    



############################################################
GivenPuzzle = [
    [0,0,0,8,0,5,1,3,0],
    [0,0,0,0,0,0,6,8,0],
    [0,5,6,0,0,0,9,0,2],
    [0,9,3,0,5,7,0,0,0],
    [5,0,2,3,0,6,7,0,4],
    [0,0,0,9,1,0,5,6,0],
    [9,0,5,0,0,0,3,7,0],
    [0,6,1,0,0,0,0,0,0],
    [0,2,4,6,0,3,0,0,0]
    ]
PuzzleSolution = SudokuSolver(GivenPuzzle)
