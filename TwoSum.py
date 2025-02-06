def twoSum(target, nums):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] +nums[j] == target:
                    return[nums[i],nums[j]] # [i,j] se quiser os indices e [nums[i],nums[j]] caso seja os números
        return [] 

nums = list(map(int,input("Digite uma lista de números inteiros separados por espaço: ").split()))
target = int(input("Digite o número alvo ,possível dentro da lista,que deseja: "))
print(twoSum(target,nums))