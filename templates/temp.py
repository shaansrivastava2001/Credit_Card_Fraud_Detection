nums=[1,2,3,4,5,6,7]
k=3

ans=nums[-k:]
        
x=len(nums)-k

l2=nums[:x]

for i in l2:
    ans.append(i)

print(ans)