integers = [1,1,0,-1,-1]
def plusminus(integers):
    a=0
    positive= 0
    negative= 0
    zero=0
    count=0
    for i in integers:
        count+=1
        if integers[a]>=1:
            positive+=1
        if integers[a]==0:
            zero+=1
        if integers[a]<=-1:
            negative+=1
        a+=1
    positive = positive / count
    zero = zero / count
    negative = negative / count
    print (f"Positive ratio: {positive}, Zero ratio: {zero}, Negative ratio: {negative}")
plusminus(integers)