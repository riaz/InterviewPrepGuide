if __name__ == '__main__':
    lst = [1,2,3,4,5]
    it = iter(lst) # or it = lst.__iter__()

    while True:
        try:
            val = next(it) # or val = it.__next__()
            print(val)
        except StopIteration:
            break

    print("The list was iterated over")