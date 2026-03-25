SIZE=4
pit=(4,3)
wumpus=(2,3)
gold=(1,4)
agent=(4,1)
def show_grid(agent):
 print("\nCurrent World Grid:\n")
 for i in range(1,SIZE+1):
 for j in range(1,SIZE+1):
 if(i,j)==agent:
 print("A",end=" ")
 elif(i,j)==pit:
 print("P",end=" ")
 elif(i,j)==wumpus:
 print("W",end=" ")
 elif(i,j)==gold:
 print("G",end=" ")
 else:
 print("-",end=" ")
 print()
 print()
def adjacent(a,b):
 return abs(a[0]-b[0])+abs(a[1]-b[1])==1
print("----- WUMPUS WORLD (4X4)-----")
print("lEGEND:A= Agent , P=Pit,W=Wumpus,G=Gold")
print("Agent starting at (1,1)")
show_grid(agent)
while True:
 r=int(input("enter next row(1-4): "))
 c=int(input("enter the column(1-4): "))
 if r<1 or r>4 or c<1 or c>4:
 print("Invalid position!")
 continue
 agent=(r,c)
 show_grid(agent)
 if agent==pit:
 print("Danger! Agent fell into PIT.")
 break
 elif agent==wumpus:
 print("Wumpus killed the agent !")
 break
 elif agent==gold:
 print("Agent found the gold! YOU WIN !")
 break
 else:
 if adjacent(agent,pit):
 print("Breeze detected(PIT nearby)")
 if adjacent(agent,wumpus):
 print("Stench detected (Wumpus nearby)")
 if not adjacent(agent,pit) and not adjacent(agent,wumpus):
 print("Safe Zone")
