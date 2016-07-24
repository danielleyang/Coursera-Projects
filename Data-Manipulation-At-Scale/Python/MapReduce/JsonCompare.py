import json
import sys

# This file is used to compare my result to the solutions line by line
if __name__ == '__main__':
    file1 = open(sys.argv[1])
    file2 = open(sys.argv[2])
    for line1 in file1:
        for line2 in file2:
            record1 = json.loads(line1)
            record2 = json.loads(line2)
            if record1 == record2:
                break
            else:
                print "There is a difference. Line1 is %s. Line 2 is %s" % (record1, record2)
