#%% Lambda function
def summ(a,b):
    return a+b
print("dev=",summ(12,25))
N=lambda x,y: x+y
print("lambda=",N(12,25))
fact=lambda x: print([i for i in x])
fact([1,2,3,4,5,6,7,8,9,10])
#%%
fact=lambda x: print([i*i for i in x])
fact([1,2,3,4,5,6,7,8,9,10])

#%%
sonlar = [1,2,3,4,5,6,7,8,9,10]
juft = list(filter(lambda x : x%2==0, sonlar))
toq = list(filter(lambda x: x%2!=0, sonlar))
print('juft sonlar = ', juft)
print("toq sonlar = ",toq)
#%%



