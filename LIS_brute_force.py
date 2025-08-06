def find_subseq(nums,ind,res,temp):
    if ind==len(nums):
        res.append(temp)
        return
    else:
        find_subseq(nums,ind+1,res,temp+[nums[ind]])
        find_subseq(nums,ind+1,res,temp)

res = []
nums = [10,9,2,5,3,7,101,18]
find_subseq(nums,0,res,[])

max_len = 0
inc_sub = []

for r in res:
    for i in range(1,len(r)):
        if r[i]<=r[i-1]:
            break
    else:
        inc_sub.append(r)
        max_len= max(max_len, len(r))

print("Total number of sub sequences:\n",inc_sub)
print("Maximum length of increasing subsequence: ",max_len)


# Note this can be solved easily by LIS
