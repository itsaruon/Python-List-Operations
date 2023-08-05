import random
order = []

for i in range(0,5):
    order.append(random.randint(1,10))
    
print("Old List :", order )

def alterFirstAndLast(order):
    temp = order[0];
    order[0] = order[len(order)-1]
    order[len(order) - 1] = temp
    return order

#Line below switches first and last elements
order = alterFirstAndLast(order)
print("New List after swapping first and last elements in Old List: ", order)
#order = alterFirstAndLast(order)
reverseList = order[::-1]
print("After reversing New List elements: ", reverseList)
