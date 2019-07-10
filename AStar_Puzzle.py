import time
import heapq 

result = []
        
def right(OGpuz, index):
    oldPuz = OGpuz +[]
    oldPuz[index], oldPuz[index+1] = oldPuz[index+1], oldPuz[index]
    return oldPuz

def left(OGpuz, index):
    oldPuz = OGpuz +[]
    oldPuz[index], oldPuz[index-1] = oldPuz[index-1], oldPuz[index]
    return oldPuz

def up(OGpuz, index):
    oldPuz = OGpuz +[]
    oldPuz[index], oldPuz[index-3] = oldPuz[index-3], oldPuz[index]
    return oldPuz

def down(OGpuz, index):
    oldPuz = OGpuz +[]
    oldPuz[index], oldPuz[index+3] = oldPuz[index+3], oldPuz[index]
    return oldPuz

def readFile(name):
    file = open(name,'r')
    puzList = []
    puz = []
    for line in file:
        line = line.replace(' ','')
        line = line.replace(',','')
        line = line.replace('\n','')
        for i in line:
            puz.append(int(i))
        puzList.append(puz + [])
        puz = []
    return puzList

def print_path(result):
    i = 0
    print("\nSolution:")
    for puz in result:
        for col in puz:
            if i == 3:
                print()
                i = 0
            print(col, end = ' ')
            i += 1
        if(puz != [0,1,2,3,4,5,6,7,8]):
            print("\n\nto")
    print()
    
def amount_of_misplaced(puz):
    i = 1
    misplaced = 0
    for pos in puz[1:]:
        if pos != i:
            misplaced += 1
        i +=1
    return misplaced

def Manhattan_Distance_amount(puz):
    total = 0
    for i in puz:
        if i != 0:
            total += abs(int(puz.index(i)/3)  - int(i/3)) + abs(puz.index(i) % 3 - i % 3)
    return total

#implementation of function "A Star Misplaced"

def A_Star_Misplaced(nameOfFile):
    print("running A Star Misplaced\n")
    puzList = readFile(nameOfFile)
    DepthTotal = 0
    j = 1
    TTime = 0
    firstPath = []
    OverAllStart = time.time()
    for puz in puzList:
        print("Solving please wait...")
        start = time.time()
        Path, Depth = Misplaced_helper(puz)
        if(len(firstPath) == 0 ):
            firstPath = Path +[]
        end = time.time()
        DepthTotal += Depth
        #print_path(Path)
        print("Solved puzzle #",j,sep = '')
        print()
        #print(Depth)
        j += 1
        TTime += end-start
    OverAllEnd = time.time()
    TTime = TTime/(j-1)
    print("Misplaced Results")
    print("\nAvg Depth:", DepthTotal/(j-1), "    Avg time:  ", int(((TTime)/60)/60), ":", int((TTime)/60),":", int((TTime)%60), sep = '', end = '')
    print("    Total Run Time:  ", int(((OverAllEnd-OverAllStart)/60)/60), ":",int((OverAllEnd-OverAllStart)/60), ":", int((OverAllEnd-OverAllStart)%60), sep = "")
    print()
    return [firstPath, DepthTotal/(j-1),TTime]
    
def Misplaced_helper(puz):
    Path = {}#keeps track of all the childrens parents. will also double as out unique paths seen
    startState = puz + []
    temp = Misplaced_solver(puz, Path)
    if temp == [0,1,2,3,4,5,6,7,8]:
        #do stuff then return path
        print("Reached goal state.")
        P = []
        PathLen = 0
        P.append(temp)
        while temp != startState:
            PathLen += 1
            temp = Path[tuple(temp)][0]
            P.append(temp)
        P.reverse()
        return P, PathLen
            
        
    return "FAILED!!!!!!!!!!!!!!!!!!"


def Misplaced_solver(puz, Path):
    #path needs to add a list that will keep track of the path, depth the lower the depth the better.
    #in its in the path check its depth if its lower then replace the value with the new value
    depth = 0
    amount_State = [amount_of_misplaced(puz), puz + [], depth ]   #amount_State is a list of the amount of misplaced tiles plus the curent state
    pQueue = [amount_State + []]
    heapq.heapify(pQueue)                       #we will place into a heap the state and the amount of misplaced tiles.
    i = 0
    j = 0
    
    while len(pQueue) != 0:
        #print(pQueue)
        i += 1
        j += 1
        popedItem = heapq.heappop(pQueue)
        curState = popedItem[1]
        depth = popedItem[2]
        if curState == [0,1,2,3,4,5,6,7,8]:
            return curState

        
        #print(j)
        
        Pos = curState.index(0)
                             
        if Pos == 0:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
            
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
                
        elif Pos == 1:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
            
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
                    
        elif Pos == 2:
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
            
            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
                
        elif Pos == 3:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
            
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
                    
        elif Pos == 4:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
            
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
        elif Pos == 5:
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
                
        elif Pos == 6:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
            
        elif Pos == 7:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
                
            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

        elif Pos == 8:
            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [amount_of_misplaced(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, depth]  
                
            elif depth < Path[tuple(temp)][1]:
                Path[tuple(temp)] = [curState, depth]
                
        else:
            print("error happened")
            exit(0)

        
    print("error", i)
    return i

#implementation of function "A Star Manhattan_Distance"

def A_Star_Manhattan_Distance(nameOfFile):
    print("running A Star Manhattan Distance\n")
    puzList = readFile(nameOfFile)
    DepthTotal = 0
    j = 1
    TTime = 0
    OverAllStart = time.time()
    for puz in puzList:
        print("Solving please wait...")
        start = time.time()
        Path, Depth = Manhattan_Distance_helper(puz)
        end = time.time()
        DepthTotal += Depth
        #print_path(Path)
        print("Solved puzzle #",j,sep = '')
        #print(Depth)
        print()
        j += 1
        TTime += end-start
    OverAllEnd = time.time()
    TTime = TTime/(j-1)
    print("Manhattan_Distance Results")
    print("\nAvg Depth:", DepthTotal/(j-1), "    Avg time:  ", int(((TTime)/60)/60), ":", int((TTime)/60),":", int((TTime)%60), sep = '', end = '')
    print("    Total Run Time:  ", int(((OverAllEnd-OverAllStart)/60)/60), ":",int((OverAllEnd-OverAllStart)/60), ":", int((OverAllEnd-OverAllStart)%60), sep = "")
    print()
    return [DepthTotal/(j-1), TTime]
    
def Manhattan_Distance_helper(puz):
    Path = {}#keeps track of all the childrens parents. will also double as out unique paths seen
    startState = puz + []
    temp = Manhattan_Distance_solver(puz, Path)
    if temp == [0,1,2,3,4,5,6,7,8]:
        #do stuff then return path
        print("Reached goal state.")
        P = []
        PathLen = 0
        P.append(temp)
        while temp != startState:
            PathLen += 1
            temp = Path[tuple(temp)][0]
            P.append(temp)
        P.reverse()
        return P, PathLen
            
        
    return "FAILED!!!!!!!!!!!!!!!!!!"


def Manhattan_Distance_solver(puz, Path):
    
    depth = 0
    amount_State = [Manhattan_Distance_amount(puz), puz + [], depth ]   #amount_State is a list of the  Manhattan_Distance amount plus the curent state and depth
    pQueue = [amount_State + []]
    heapq.heapify(pQueue)                       #we will place into a heap the state and the amount of misplaced tiles.
    i = 0
    j = 0
    
    while len(pQueue) != 0:
        #print(pQueue)
        i += 1
        j += 1
        popedItem = heapq.heappop(pQueue)
        curState = popedItem[1]
        depth = popedItem[2]
        if curState == [0,1,2,3,4,5,6,7,8]:
            return curState

        
        #print(j)
        
        Pos = curState.index(0)
                             
        if Pos == 0:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
            
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
                
        elif Pos == 1:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
            
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp) + depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
                    
        elif Pos == 2:
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
            
            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
                
        elif Pos == 3:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
            
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
                    
        elif Pos == 4:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
            
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
        elif Pos == 5:
            temp = down(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
                
        elif Pos == 6:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
            
        elif Pos == 7:
            temp = right(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
                
            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

        elif Pos == 8:
            temp = left(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                

            temp = up(curState,Pos)
            if tuple(temp) not in Path:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]  
                
            elif Manhattan_Distance_amount(temp)+ depth < Path[tuple(temp)][1]:
                amount_State = [Manhattan_Distance_amount(temp)+ depth, temp + [], depth + 1 ]
                heapq.heappush(pQueue, amount_State+[])
                Path[tuple(temp)] = [curState, Manhattan_Distance_amount(temp)+ depth]
                
        else:
            print("error happened")
            exit(0)

        
    print("error", i)
    return i

#implementation of function "print_result(result)"
def print_result(result):
    Manhattan_Distance_time = result[len(result) - 1]
    del result[len(result) - 1]
    Manhattan_Distance_avg = result[len(result) - 1]
    del result[len(result) - 1]
    
    Miss_Placed_time = result[len(result) - 1]
    del result[len(result) - 1] 
    Miss_Placed_avg = result[len(result) - 1]
    del result[len(result) - 1]

    print("\nSolution to puzzle #1")
    
    print_path(result[0])
    
    print("\nMiss Placed Results\t", end = '')
    print("Avg Depth:", Miss_Placed_avg, "    Avg time:  ", int(((Miss_Placed_time)/60)/60), ":", int((Miss_Placed_time)/60),":", Miss_Placed_time%60, sep = '')
    print("Manhattan Distance\t", end = '')
    print("Avg Depth:",  Manhattan_Distance_avg, "    Avg time:  ", int(((Manhattan_Distance_time)/60)/60), ":", int((Manhattan_Distance_time)/60),":", Manhattan_Distance_time%60, sep = '')
    

    
        
result += A_Star_Misplaced("Input8PuzzleCases.txt")
result += A_Star_Manhattan_Distance("Input8PuzzleCases.txt")

print_result(result)
