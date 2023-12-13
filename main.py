# list1 = ["I", "V", "X", "L", "C", "D", "M"]
#
#
# number = input("Rome number:")
#
# number1 = 0
#
# list2 = list(number)
# i = 0
#
# while i < len(list2)-1:
#     if i != len(list2)-1:
#         if i != len(list2)-2 and dict1[list2[i]] + dict1[list2[i+1]] < dict1[list2[i+2]]:
#             number1 = number1 + dict1[list2[i + 2]] - dict1[list2[i+1]]-dict1[list2[i]]
#             i+=3
#         elif dict1[list2[i]] < dict1[list2[i+1]]:
#             number1 =number1 + dict1[list2[i + 1]]-dict1[list2[i]]
#             i+=2
#         else:
#             number1 = number1 + dict1[list2[i]]
#             i+=1
#
# print(number1)


#
class Queue:
    def __init__(self, list1: list):
        self.list1 = list1

    def enqueue(self, value):
        self.list1.append(value)
        return self.list1

    def dequeue(self):
        self.list1.pop(0)
        return self.list1


queue = Queue([1, 3, 4])

print(queue.enqueue(6))

print(queue.dequeue())















































