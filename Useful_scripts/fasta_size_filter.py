#!/usr/bin/env python3

from Bio import SeqIO
import argparse

#### create argument parser ####
parser = argparse.ArgumentParser(
                    prog='Get assembly stats',
                    description='A quick python script filtering fasta files',
                    epilog='see GitHub for more help') #This creates the basic framework

parser.add_argument('-fasta', metavar='--fa', help='Fasta file to be filtered') 
parser.add_argument('-sizeFilter', metavar='--S',type=int, help='The minimum size of sequeneces to retain')
parser.add_argument('-out', metavar='--O', help='Name of the output file.')
#-h for help is a default argument

args = parser.parse_args()

print("Notice, sequences shorter than %d will be removed" % args.sizeFilter)
with open(args.out, "w") as f: #
    for seq in SeqIO.parse(args.fasta,'fasta'):
        if len(seq.seq) > args.sizeFilter:
            SeqIO.write([seq], f, "fasta")
            
print("Notice, the following seqeuences were retained:")
for seq in SeqIO.parse(args.out,'fasta'): print(seq.id)
