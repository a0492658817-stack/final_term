def INPUT():
    n=int(input())
    m=int(input())
    A=input().split()
    B=input().split()
    same=input().split()
    return n,m,A,B,same

def fill(List,n,num):
    k=0
    for i in range(n):
        for j in range(n):
            List[i][j]=num[k]
            k+=1
    

def count(List,n,same_set):
    total=0
    a=0
    b=0

    if all(List[i][i] in same_set for i in range(n)):
        total+=1
        a=1
    if all(List[i][n-i-1] in same_set for i in range(n)):
        total+=1
        b=1
    for i in range(n):
        if all(List[i][j] in same_set for j in range(n)):
            total += 1
    for j in range(n):
        if all(List[i][j] in same_set for i in range(n)):
            total += 1   
    if(a and b):
        total+=1
    if all(List[i][0] in same_set for i in range(n)) and all(List[n-1][j] in same_set for j in range(n)):
        total += 1
    return total

def main():
    n,m,A,B,same=INPUT()
    same_set=set(same)
    Alist=[[0]*n for i in range(n)]
    Blist=[[0]*n for i in range(n)]
    fill(Alist,n,A)
    fill(Blist,n,B)
    Ascore=count(Alist,n,same_set)                                                                                                                                                                                                                             
    Bscore=count(Blist,n,same_set)
    if(Ascore>Bscore):
        print("A Win")
    elif(Bscore>Ascore):
        print("B Win")
    else:
        print("Tie")
main()