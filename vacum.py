#Vacuum Cleaner Problem
#Clean is 0 and Dirty is 1

def vacuumcleaner(rooms,n):
        i = 0
        j = 0
        clean = 0    
        while(clean < n):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            if(rooms[i][j] == 1):
                print("Cell",i,j,"is dirty")
                print("Performing suck...")
                rooms[i][j] = 0
                clean = clean + 1
                print("Cell",i,j,"is clean")
                    
            elif(rooms[i][j] == 0):
                clean = clean + 1
                print("Cell",i,j,"is already clean")
                    
            if(j==0):
                j+=1
                print("Moving Right....")
            elif(j==1 and i==0):
                i+=1
                j=0
                print("Moving Down......")
              
            
if __name__ == "__main__":
    n = 4
    clean = 0
    rows = 2
    cols = 2
    rooms = []
    print("Enter the room matrix with one entry in each line:")
    for i in range(rows):        
        a =[]
        for j in range(cols):     
            a.append(int(input()))
        rooms.append(a)
        
    d = vacuumcleaner(rooms,n)
