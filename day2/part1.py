def find_invalid_product_ids(productIds):
    invalidProductIds = []
    for productId in range(int(productIds[0]), int(productIds[1]) + 1):
        if isInvalid(str(productId)):
            invalidProductIds.append(productId)
    return invalidProductIds

def isInvalid(productId):
    # check if it has exactly 2 repeating sequences of digits
    # e.g 11, 12341234, 9595 are invalid

    if len(productId) % 2 != 0:
        return False
    
    first, second = productId[0:len(productId)//2], productId[len(productId)//2:]
    if first == second:
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