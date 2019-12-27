def reachPawn(knightpos, pawnpos):
    
    knightmove = ([1,2], [1,-2], [-1,2], [-1,-2], [2, 1], [-2, 1], [-2, -1], [2, -1])
    check = []
    
    for j in range(len(knightmove)):
        if knightmove[j][0] + knightpos[0] == pawnpos[0] and knightmove[j][1] + knightpos[1] == pawnpos[1]:
            check = ((knightmove[j][0] + knightpos[0], knightmove[j][1] + knightpos[1]))
            
        else:
            pass
        
    return check
        

def solvable(knightpos, setofpawns):
    if len(setofpawns) == 0:
        return True
    
    else:
        listofpawns = list(setofpawns)
        for item in range(len(setofpawns)):
            
            if reachPawn(knightpos, listofpawns[item]) != []:
                knightmove = reachPawn(knightpos, listofpawns[item])
                tup = (listofpawns[item][0], listofpawns[item][1])
                tupSet = {tup}
                
                if solvable(knightmove, set(listofpawns) - tupSet) == True:
                    return True
                    

                else:
                    pass
            else:
                pass
                
    return False

       

def findpath():
    pass

   
def findstart(setofpawns):
    knightmovement = set()
    for y in range(1, 9):
        for x in range(1, 9):
            tup = (x, y)
            if tup not in setofpawns:
                if solvable(tup, setofpawns):
                    knightmovement.add(tup)     
                   
    return knightmovement
    
pawns = {(2,2), (2,3), (2,4), (3,2), (3,4), (4,2), (4,3), (4,4), (5,5), (5,6), (5,7), (6,5), (6,7), (7,5), (7,6), (7,7)}
print(findstart(pawns))
