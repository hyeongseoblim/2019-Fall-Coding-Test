
# coding: utf-8

# In[ ]:


import copy

def find_root(airport,key,root):
    idx =0
    count = list()
    count2 =list()
    airport2 = copy.deepcopy(airport)
    if len(airport[key])!=0:#빈공항 아닌경우
        if len(root) == 0:
            root.append(key)
        if len(airport[key]) >1 : # 다음꺼에서 갈수 있는 경우가 둘다 하나인 경우
            if len(airport[airport[key][idx]]) == 1 and len(airport[airport[key][idx+1]]) == 1:
                count.append(0)
                count2.append(0)
                find_depth(airport2,key,0,count)
                airport2 = copy.deepcopy(airport)
                find_depth(airport2,key,1,count2)
                if count[0]<count2[0]:
                    a= airport[key].pop(idx+1)
                else:
                    print(airport)
                    a= airport[key].pop(idx)            
                root.append(a)
            else:#
                a= airport[key].pop(idx)
                root.append(a)
            return a
        else:    
            a= airport[key].pop(idx)
            root.append(a)
            return a   
    else:
        return None
    
def find_depth(airport, key, idx, count):
    length = count[0]
    if len(airport[key]) !=0:
        temp_key=airport[key].pop(idx)
        if len(airport[temp_key]) != 0:
            length +=1
            temp_key= airport[temp_key].pop(0)
            count[0] = length
            find_depth(airport,temp_key,0,count)
        else:
            length +=1
            count[0] = length
            return 
        
def solution(tickets):
    answer = []
    airport_list=dict()
    root_list =list()
    length = 0
    for idx in range(len(tickets)):
        if tickets[idx][0] not in airport_list:
            airport_list[tickets[idx][0]]=list()
            airport_list[tickets[idx][0]].append(tickets[idx][1])
            length +=1
            if tickets[idx][1] not in airport_list:
                airport_list[tickets[idx][1]]=list()
        else:
            if tickets[idx][1] not in airport_list[tickets[idx][0]]: 
                airport_list[tickets[idx][0]].append(tickets[idx][1])
                length +=1
            else:
                break
        airport_list[tickets[idx][0]]=sorted(airport_list[tickets[idx][0]])
    keys = list(airport_list.keys())
    root ="ICN"
    count = 0
    while (length != count):        
        if root != None :
            root = find_root(airport_list,root,root_list)
        count+=1
    answer=root_list
    return answer


solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
#solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
#solution([["ICN", "COO"], ["COO", "ICN"], ["COO", "ICN"]])
#solution([["ICN","COO"],["ICN","BOO"],["COO","ICN"],["BOO","DOO"]])
#solution([["ICN","BOO"],["ICN","COO"],["COO","DOO"],["DOO","COO"],["BOO","DOO"],["DOO","BOO"],["BOO","ICN"],["COO","BOO"]])

