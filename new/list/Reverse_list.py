def print_reverse(List):
    print ("Given List {0}".format(List))
    lst = []
    count = 1
    for i in range(0,len(List)):
        lst.append(List[len(List)-count])
        count += 1

    lst = str(lst)
    lst = ''.join(lst)
    return lst

def main():
    List = [10,21,30,1,4]
    result = print_reverse(List)
    print ("List after reverse {0}".format(result))


if __name__ == '__main__':
    main()
