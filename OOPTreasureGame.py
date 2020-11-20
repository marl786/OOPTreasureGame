import random
bold= '\33[1m'
red='\33[41m'
green= '\33[42m'
end= '\33[0m'
class Treasure:
    def __init__(self):
        Sand="."
        Treasure="T"
        self.__Grid=[[Sand for i in range(5)] for j in range(5)]
        for quantity in range(3):
            x = random.randint(0,4)
            y = random.randint (0,4)
            while self.__Grid[y][x]=="T":
                x = random.randint(0,4)
                y = random.randint (0,4)
            self.__Grid[y][x]="T"
    def singleoutput(self, x, y):
        if self.__Grid[x][y]=="X":
            print(green+self.__Grid[x][y]+end)
        else:
            print(red+self.__Grid[x][y]+end)
    def digGrid(self, x, y):
        if self.__Grid[x][y]=="T":
            self.__Grid[x][y]="X"
        elif self.__Grid[x][y]==".":
            self.__Grid[x][y]="O"
    def userinput(self):
        for quantity in range(3):
            
            r=int(input("Enter a row (1 to 5): "))-1
            c=int(input("Enter a column (1 to 5): "))-1
            while r>4 or r<0 or c>4 or c<0:
                if r>4 or r<0 and c>=0 and c<=4:
                    r=int(input("Re-Enter a row: "))-1
                elif c>4 or c<0 and r>=0 and r<=4:
                    c=int(input("Re-Enter a column: "))-1
                else:
                    r=int(input("Re-Enter a row: "))-1
                    c=int(input("Re-Enter a column: "))-1
            self.digGrid(r, c)
            self.singleoutput(r, c)
            print("\n")
    
    def display(self):
        for x in range(5):
            for y in range(5):
                print(self.__Grid[x][y], end='      ')
            print("\n")
a=Treasure()
a.userinput()
a.display()
