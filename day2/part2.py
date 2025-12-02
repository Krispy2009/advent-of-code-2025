def find_invalid_product_ids(productIds):
    invalidProductIds = []
    for productId in range(int(productIds[0]), int(productIds[1]) + 1):
        if isInvalid(str(productId)):
            invalidProductIds.append(productId)
    return invalidProductIds

def isInvalid(productId):
    for i in range(len(productId)):
        sub_string = productId[0:i+1]
        if len(sub_string) > len(productId)//2:
            continue
        new_str = sub_string * (len(productId)//len(sub_string))
        # print("sub_string: ", sub_string)
        # print("new_str: ", new_str)
        if new_str == productId:
            return True
    
    return False

if __name__ == "__main__":
    
    productIdsRanges = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            for rg in line.split(","):
                productIdsRanges.append(tuple((rg.split("-")[0], rg.split("-")[1] )))

        invalidProductIds = []

        for productIdRange in productIdsRanges:
            invalidProductIds.extend(find_invalid_product_ids(productIdRange))

        # print("invalidProductIds: ", invalidProductIds)
        print("sum of invalidProductIds: ", sum(invalidProductIds))