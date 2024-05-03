#!/usr/bin/env python3

from Bio import SeqIO
import argparse

#### create argument parser ####
parser = argparse.ArgumentParser(
                    prog='Get assembly stats',
                    description='A quick python script filtering fasta files',
                    epilog='see GitHub for more help') #This creates the basic framework

parser.add_argument('fasta', metavar='--fa', help='Fasta file to be filtered') 
parser.add_argument('remove', metavar='--R', help='A text file with a list of sequences to remove. The names should not start with the > character')
parser.add_argument('out', metavar='--O', help='Name of the output file.')
#-h for help is a default argument

args = parser.parse_args()

#The list of headers to remove gets saved as a set names remove
remove = set()
with open(args.remove) as f:
    for line in f:
        line = line.strip()
        if line != "":
            remove.add(line) #The last if loop is to make sure no blank lines are included in the set 

#Biopython removes > by default, so need to make sure the list to remove does not include this character either 

print("Notice: the following sequences will be removed:")
for i in remove:
    print(i)



with open(args.out, "w") as f: #
    for seq in SeqIO.parse(args.fasta,'fasta'):
        nuc = str(seq.id)
        if nuc not in remove and len(nuc) > 0:
            SeqIO.write([seq], f, "fasta")
            
print("Notice the following seqeuences were retained:")
for seq in SeqIO.parse(args.out,'fasta'): print(seq.id)