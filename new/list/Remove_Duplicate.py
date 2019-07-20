def check_duplicate(List):
    dup_list = []
    for i in List:
        if i not in dup_list:
            dup_list.append(i)
        else:
            return True
    return False

def duplicate_position(dup_list):
    dup_items = []
    dup_list.sort()
    print ("Given List after Sorting {0}".format(dup_list))
    for item in range(0,len(dup_list)-1):
        if dup_list[item] == dup_list[item+1]:
            print ("Same Item Found at the position {0} ".format(item))
            dup_items.append(dup_list[item])
        else:
            pass
    print("Duplicate Items {0}".format(dup_items))

def remove_duplicate(List):
    result = []
    for item in List:
        if item not in result:
            result.append(item)

    print("List after duplicate Removal {0}".format(result))

def main():
    List = [1,22,2,3,3,4]
    result = check_duplicate(List)
    if result:
        duplicate_position(List)
        remove_duplicate(List)
    else:
        print("not Duplicate Found")

if __name__ == '__main__':
    main()
