# filename = "test.txt"
#
#
# for each_line in open(filename):
#     print each_line
#     for each_word in each_line.split():
#         print each_word
#     print "=============="

import csv
csv_file = "test.csv"

csv_obj = csv.reader(csv_file)
for row in csv_obj:
    print row


