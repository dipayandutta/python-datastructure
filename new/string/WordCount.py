def wordCount(message,key):
    count = 0
    for word in message:
        print (word)
        if word == key:
            count += 1
    print("Total Count {0}".format(count))


if __name__ == '__main__':
    wordCount("Hello","l")

