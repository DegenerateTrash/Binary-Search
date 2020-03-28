import time


def genList():
    import random as r
    ls = []
    start_time = time.time()
    for i in range(0,20000001,1):
        ls.append(i)
        #ls.append(str(r.randint(0,100)))
    #for i in range(0,500,1):
        #ls.append(str(r.randint(0,100000)))
    ls.sort()
    print("Creating list: %s seconds" % (time.time() - start_time))
    return ls

def getfile():
    file = open("warpeace.txt","r", encoding="utf8")
    text = file.read()
    text = text.split(" ")
    return text

def linsearch():
    ls = getfile()
    itm = str(input("Item: "))
    start_time = time.time()
    for x in ls:
        if x == itm:
            print("{0} found at position".format(itm))
            print("Linear Search: %s seconds" % (time.time() - start_time))
            return
            

def binsearch():
    ls = getfile()
    ls.sort()
    itm = str(input("Item: "))
    start_time = time.time()
    while 0 == 0:
        try:
            midpoint = (len(ls) + 1) // 2
            #print("{0} | {1} | {2} | {3}".format(len(ls), midpoint, ls[midpoint], ls))
            if ls[midpoint] == itm:
                print("{0} found at position {1}".format(itm, midpoint))
                break
            elif ls[midpoint] < itm:
                ls = ls[midpoint:]
            elif ls[midpoint] > itm:
                ls = ls[:midpoint]
            if len(ls) == 1 and ls[midpoint] != itm:
                print("Item not found")
                break
        except IndexError:
            print("Item not found")
            break
    print("Binary Search %s seconds" % (time.time() - start_time))

linsearch()
binsearch()