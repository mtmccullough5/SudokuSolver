#Sudoku Solver

def SudokuSolver(PuzzleState):
    def TruthMaker(ArrayStates, Number):
        TruthMatrix = []
        for x in range(9):
            TruthMatrix.append(
                [True, True, True, True, True, True, True, True, True])
        PuzzleState = ArrayStates[0]
        HorzState = ArrayStates[0]
        VertState = ArrayStates[1]
        BlockState = ArrayStates[2]
        
        ## Horizontal Lines
        for x in range(9):
            if Number in HorzState[x]: 
                TruthMatrix[x] = [True, True, True, True, True, True, True, True, True]
        
        ## Check Vertical Line
        for y in range(9):
            if Number in VertState[y]:
                for x in range(9):
                    TruthMatrix[x][y] = True

        ## Check Blocks
        for j in range(9):
            if Number in BlockState[j]:
                SuperRow = (j-j%3)/3
                SuperCol = j%3
                x1 = int(SuperRow*3)
                x2 = int(SuperRow*3+3)
                y1 = int(SuperCol*3)
                y2 = int(SuperCol*3+3)
                for x in range(x1,x2):
                    for y in range(y1,y2):
                        TruthMatrix[x][y] = False

        ## Check if a number is already there
        for x in range(9):
            for y in range(9):
                if PuzzleState[x][y] != 0:
                    TruthMatrix[x][y] = False

        return TruthMatrix

    def Indexer(PuzzleState):
        ## PuzzleState is identical to Horizontal Arrays
        HorzState = PuzzleState
        ## Vertical State
        VertState = []
        for x in range(9):
            VertArr = []
            for y in range(9):
                VertArr.append(PuzzleState[y][x])
            VertState.append(VertArr)
        ## Block State
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
        IndexedArrays = [HorzState,VertState,BlockState]
        return IndexedArrays

    def MatrixSum(PuzzleState):
        Sum = 0
        PuzzleSum = True
        for arr in PuzzleState:
            for index in arr:
                if isinstance(index,int):
                    Sum += index
        if Sum == 405:
            PuzzleSum = False
        return PuzzleSum

    def FindIndex(TruthMat):
        # Create Truth Arrays
        TruthArrays = Indexer(TruthMat)
        HorzState = TruthArrays[0]
        VertState = TruthArrays[1]
        BlockState = TruthArrays[2]
        index = [ 10, 10]
        # Check arrays
        for x in range(9):
            if HorzState[x].count(True) == 1:
                index = [ x, HorzState[x].index(True)]
                print("hit horz")
                break
            if VertState[x].count(True) == 1:
                index = [ VertState[x].index(True), x]
                print("hit vert")
                break
            if BlockState[x].count(True) == 1:
                SuperRow = (x-x%3)/3
                SuperCol = x%3
                K = BlockState[x].index(True)
                BlockRow = (K-K%3)/3
                BlockCol = K%3
                index = [ int(3*SuperRow + BlockRow), int(3*SuperCol + BlockCol)]
                print("hit block")
                break
        return index

    def Replacer(PuzzleState, Index, TestNumber):
        PuzzleState[Index[0]][Index[1]] = TestNumber
        return PuzzleState

    PuzzleSum = True
    loopindex = 0
    while PuzzleSum:
        for x in range(1,10):
            ArrayStates = Indexer(PuzzleState)
            TruthMat = TruthMaker(ArrayStates, x)
            Index = FindIndex(TruthMat)
            if Index != [10,10]:
                print(x)
                print(Index)
                print("Puzzle")
                print(PuzzleState[0])
                print(PuzzleState[1])
                print(PuzzleState[2])
                print(PuzzleState[3])
                print(PuzzleState[4])
                print(PuzzleState[5])
                print(PuzzleState[6])
                print(PuzzleState[7])
                print(PuzzleState[8])
                print("Truth Matrix in solver")
                print(TruthMat[0])
                print(TruthMat[1])
                print(TruthMat[2])
                print(TruthMat[3])
                print(TruthMat[4])
                print(TruthMat[5])
                print(TruthMat[6])
                print(TruthMat[7])
                print(TruthMat[8])
                PuzzleState = Replacer(PuzzleState, Index, x)
                print("New Puzzle")
                print(PuzzleState[0])
                print(PuzzleState[1])
                print(PuzzleState[2])
                print(PuzzleState[3])
                print(PuzzleState[4])
                print(PuzzleState[5])
                print(PuzzleState[6])
                print(PuzzleState[7])
                print(PuzzleState[8])
                Index = [10,10]
                break
            PuzzleSum = MatrixSum(PuzzleState)
        loopindex+=1

    return PuzzleState
    

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

PuzzleState = SudokuSolver(GivenPuzzle)
print("Done")
print(PuzzleState[0])
print(PuzzleState[1])
print(PuzzleState[2])
print(PuzzleState[3])
print(PuzzleState[4])
print(PuzzleState[5])
print(PuzzleState[6])
print(PuzzleState[7])
print(PuzzleState[8])