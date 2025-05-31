def tupleSameProduct(nums):
    product_map = {}
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = nums[i] * nums[j]
            if product in product_map:
                count += product_map[product]
                product_map[product] += 1
            else:
                product_map[product] = 1
    return product_map , ' ' , count 

# Example usage
nums = [2, 3, 4, 6]
print(tupleSameProduct(nums))  # Output will be the number of such tuples
