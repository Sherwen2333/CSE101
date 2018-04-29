def shortest(names):
    ak=[]
    for i in range(len(names)):
        ez=min(names)
        if len(ez)<5:
            names.remove(ez)
    return min(names)
print(shortest(["ak","aaaaa","akskkkk","asdsadhqwekhss"]))
