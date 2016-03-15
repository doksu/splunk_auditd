#!/usr/bin/env python

import csv
import sys
import socket

def main():
    if len(sys.argv) != 4:
        print "Usage: python category_clearance.py [scontext_category_set] [tcontext_category_set] [category_clearance]"
        sys.exit(1)

    scontext_category_set = sys.argv[1]
    tcontext_category_set = sys.argv[2]
    category_clearance = sys.argv[3]

    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
    w.writeheader()

    # for each event
    for result in r:

        if tclass == 'file':


	elif tclass == 'dir':

	elif tclass == 'fifo_file':

	elif tclass in Set(['lnk_file', 'chr_file', 'blk_file', 'sock_file']):

	elif tclass in Set(['chr_file', 'blk_file', 'sock_file', 'fifo_file']):

	elif tclass == 'dir':
	elif tclass == 'dir':
	elif tclass == 'dir':
	elif tclass == 'dir':
	elif tclass == 'dir':
	

        if result[scontext_category_set] and result[tcontext_category_set]:
            # both fields were provided
            # MUST ADD HANDLER FOR COMMA SEPARATED LIST OF CATEGORY SPECS, e.g.: c0.c10,c400,c.450.c1023
            a = result[scontext_category_set].split(".")[0]
            b = result[scontext_category_set].split(".")[1]
            c = result[tcontext_category_set].split(".")[0]
            d = result[tcontext_category_set].split(".")[1]
	    result[category_clearance] = set(range(int(a.replace('c','')), int(b.replace('c','')))).issuperset(set(range(int(c.replace('c','')),int(d.replace('c','')))))
            w.writerow(result)

        elif result[scontext_category_set]:
            # only scontext_category_set was provided, return the same
            w.writerow(result)

        elif result[tcontext_category_set]:
            # only tcontext_category_set was provided, return the same
            w.writerow(result)

main()
