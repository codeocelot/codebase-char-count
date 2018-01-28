import os
import sys
import collections
import operator
import csv

embargoed = [" ", "\n", "\t"]

if __name__ == "__main__":
    rootdir = sys.argv[1]
    d = ''

    for folder, subs, files in os.walk(rootdir):
        for filename in files:
            with open(os.path.join(folder, filename), 'r') as src:
                s = src.read()
                d += s

    # print('done with {} lines'.format(d.split('\n')))
    alphas = collections.Counter()

    for char in list(d):
        if char not in embargoed:
            alphas[char] += 1

    count = sum(alphas.values())
    print(count)

    sorted_alphas = sorted(alphas.items(), key=operator.itemgetter(1))
    sorted_alphas.reverse()
    
    with open(os.path.join('./char-counts.csv'), 'w') as csv_out:
        csv_out.write('character,count,frequency\n')
        writer = csv.writer(csv_out)
        for key, value in sorted_alphas:
            writer.writerow([key, value, value/count])

