
# coding: utf-8

# In[60]:


def solution(people, limit):
    answer = 0
    p_list =sorted(people)
    escape = list()
    min_p =0
    max_p = len(p_list)-1
    while min_p <= max_p :
        print(p_list[min_p],p_list[max_p])
        if p_list[min_p]+p_list[max_p] > limit:
            max_p -=1
        else:
            min_p +=1
            max_p -=1
            
        answer +=1
       
                   
    
    return answer

solution([70, 50, 80, 50],100)
#solution([70, 80, 50],100)
#solution([40,40,40],100)

