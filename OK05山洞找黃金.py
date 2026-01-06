def INPUT():
    number_of_caves,entry_number=map(int,input().split())
    bag_weight=int(input())
    ALL=[]
    for i in range(number_of_caves):
        line=input().split()
        ALL.append(int(k) for k in line)
    return entry_number,bag_weight,ALL

def dfs(cur,cur_value,cur_wight,bag_weight,cave,visited):
    if(cur not in cave):
        return cur_value
    if(cur in visited):
        return cur_value
    value,weight,next1,next2=cave[cur]
    new_weight=cur_wight+weight
    if(new_weight>bag_weight):
        return cur_value
    new_value=cur_value+value
    best=new_value
    visited.add(cur)
    if(next1 !=0):
        cand=dfs(next1,new_value,new_weight,bag_weight,cave,visited)
        if(best<cand):
            best=cand
    if(next2 !=0):
        cand=dfs(next2,new_value,new_weight,bag_weight,cave,visited)
        if(best<cand):
            best=cand
    visited.remove(cur)
    return best
def main():
    entry_number,bag_weight,ALL=INPUT()
    cave={}
    for row in ALL:
        cave_id,value,weight,next1,next2=row
        cave[cave_id]=value,weight,next1,next2
    visited=set()
    ans=dfs(entry_number,0,0,bag_weight,cave,visited)
    print(ans)
main()