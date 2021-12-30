''''Write a Python function to sum all the numbers in a list.

Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''



def summ(num):
    
    sum= 0
    for i in num:
        sum=sum+i
    return sum

print(summ(list([8,2,3,0,7])))


















