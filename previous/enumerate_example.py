# -*- coding: utf-8 -*-

# Returns a tuple with the item and the index value from an iterable

import sys

occurence_line_number = []

def grep_word_from_files():
    number_of_occurance = 0
    word = sys.argv[1]
    
    for filename in sys.argv[2:]:
        with open(filename) as file:
            for lino , line in enumerate(file,start=1):
                if word in line:
                    print "{0}:{1}:{2:.40}".format(filename,lino,line.rstrip())
                    number_of_occurance += 1
                    occurence_line_number.append(lino)
                    
                    
    print "Total number of Occurance is {0}".format(number_of_occurance)
    
    for lines in occurence_line_number:
        print "Line number ==>",0lines
                    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Wrong Usage"
        sys.exit()
        
    else:
        grep_word_from_files()