import os
import sys


class LCS:
    def __init__(self,x:str,y:str):
        self.x=x
        self.y=y     #test with upper and lowerbase as well
        self.m=len(self.x)
        self.n=len(self.y)
        self.c=[[0]*(self.n) for i in range(self.m)]
        self.b=[[0]*(self.n+1)for i in range(self.m+1)]

    def lcslength(self):
        '''This method calculates b and c array
        for x and y arguments passed to this class 
        for finding LCS length
        ''' 
        x=self.x
        y=self.y
        b=self.b
        c=self.c
        m=self.m
        n=self.n
        for i in range(m):
            for j in range(n):
                if (x[i]==y[j]):
                    b[i][j]=b[i-1][j-1]+1
                    c[i][j]="\\"
                elif (b[i-1][j]>=b[i][j-1]):
                    b[i][j]=b[i-1][j]
                    c[i][j] ="^"
                else:
                    b[i][j]=b[i][j-1]
                    c[i][j]="<"
        return c,b
    
    def printlcs (self,i: int,j: int):
        '''This method prints the LCS of the 
        x and y arguments of this class
        ''' 
        c=self.c
        x=self.x
        if(i==-1 or j==-1):
            return
        if(c[i][j]=="\\"):
            self.printlcs(i-1,j-1)
            print( x[i], end="")
        elif c[i][j]=="^":
            self.printlcs(i-1,j)
        else:
            self.printlcs(i,j-1)


class LCSresult:
    def LCS_DP_CB(arg1,arg2):
        '''This method calls LCS DP method and LCS print method 
        from 'LCS' class for the given two arguments 
        '''  
        a=LCS(arg1,arg2)
        a.lcslength()
        for i in range((a.n*3)+8):
            print('-',end="")
        print()
        print('    |   ',end=" ")
        for j in range(1,a.n+1):
            print(f'{j} ',end=" ")
        print()
        print('    | Y',end=" ")
        for j in range(a.n):
            print(f' {a.y[j]}',end=" ")
        print()
        for i in range((a.n*3)+8):
            print('-',end="")
        print()
        print('   X|',end=" ")
        for j in range(a.n+1):
            print(f'{a.b[-1][j]} ',end=" ")
        print()
        for i in range(a.m):
            print(f' {i+1} {a.x[i]}| {a.b[i][-1]}',end=" ")
            for j in range(0,a.n):
                print(f'{a.c[i][j]}{a.b[i][j]}',end=" ")
            print()
        for i in range((a.n*3)+8):
            print('-',end="")
        print()
        print(f'Length of the Longest Common Subsequence is: {a.b[a.m-1][a.n-1]}')
        print(f'The Longest Common Subsequence of "{a.x}" and "{a.y}" is ',end="")
        print('"',end="")
        a.printlcs(a.m-1,a.n-1)
        print('"',end="")



"""The following code read the line from LCS1/txt file 
and pass the two arguments from each line of file to 'LCSresult'
class to calculate LCS length and print LCS
"""
file1=open(os.path.join(sys.path[0],"LCS1.txt"),"r")
lines=file1.readlines()
for line in lines:
    list1=line.rstrip('\n').split(',')
    arg1=list1[0]
    arg2=list1[1]
    print('\n')
    print(f'X="{arg1}"  Y="{arg2}"')
    res=LCSresult.LCS_DP_CB(arg1,arg2)

