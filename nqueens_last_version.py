
import sys
#Ther should be atomost one variable in the list L that should be true
def atmost_one_queen(L):
    temp=""
    for i in L:
        for j in L[L.index(i)+1:]:
            temp = temp +" -"+str(i)+" -"+str(j)+" 0\n"
    return temp

# For exactly one of the variables in list L to be true
def exactly_one_queen(L):
    temp=""
    temp=temp+atleast_one_queen(L)
    temp=temp+atmost_one_queen(L)
    return temp

#For atleast one of the variables in list L to be true
def atleast_one_queen(L):
    temp=""
    for i in L:
        temp = temp +" " +str(i)
    temp=temp+" 0\n"
    return temp

#function to map position of queen on the NxN board
def mapper(row,column,N):       
    return row*N+column+1

def Encoder():
    N = int(input('Number of queens: '))   
    if N < 1:
        print("Error! N is less than 1! ")
        sys.exit(0)        
    
    print("c SAT Expression for N="+str(N))
    positions = N*N
    print("c Board has "+str(positions)+" positions")

    #checking the constraints
    #There should be exactly 1 queen per row
    temp=""
    for row in range(0,N):
        L=[]
        for column in range(0,N):
            position = mapper(row,column,N)
            L.append(position)
        temp = temp+exactly_one_queen(L)
    
    #There should be exactly 1 queen per column
    for column in range(0,N):
        L=[]
        for row in range(0,N):
            position = mapper(row,column,N)
            L.append(position)
        temp = temp+exactly_one_queen(L)
    
    # There should be Atmost 1 queen per positive diagonal from right
    for row in range(N-1,-1,-1):
        L=[]
        for i in range(0,N-row):
            L.append(mapper(row+i,N-1-i,N))
        temp=temp+atmost_one_queen(L)
    
    #There should be Atmost 1 queen per positive diagonal from top
    for column in range(N-2,-1,-1):
        L=[]
        for i in range(0,column+1):
            L.append(mapper(i,column-i,N))
        temp=temp+atmost_one_queen(L)

    #There should be Atmost 1 queen per negative diagonal from left
    for row in range(N-1,-1,-1):
        L=[]
        for i in range(0,N-row):
            L.append(mapper(row+i,i,N))
        temp=temp+atmost_one_queen(L)
    
    #There should be Atmost 1 queen per negative diagonal from top
    for column in range(1,N):
        L=[]
        for i in range(0,N-column):
            L.append(mapper(i,column+i,N))
        temp=temp+atmost_one_queen(L)
     
    print('p cnf ' + str(N*N) + ' ' + str(temp.count('\n')))
    print(temp)

Encoder()
