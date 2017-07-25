from fairlib import *
import sys

order = ['F', 'A', 'I', 'R']
if sys.argv:
    try:
        doi = sys.argv[1]
    except:
        doi = "http://dx.doi.org/10.17632/crnmszmb8h.1"
        doi = "http://dx.doi.org/10.17632/yjrpmr5mwn.1"
        #doi = "http://dx.doi.org/10.17632/nhtjgdkft4.1"

data = fair_ranking(doi)
print doi
for c in order:
    print "%s %s" % (c, data[c])
