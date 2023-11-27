
import functools

def compare(num1, num2):
    return num1 - num2

lst = [1,2,3,8,6,45,3]

print("Before sorting")
print(lst)

lst.sort(key=functools.cmp_to_key(compare))

print("After sorting")
print(lst)
