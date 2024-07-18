#!/usr/bin/env python

#### Load in modules ####

import argparse
from Bio import SeqIO
import statistics

#### create argument parser ####
parser = argparse.ArgumentParser(
                    prog='Get assembly stats',
                    description='A quick python script for getting basic assembly stats',
                    epilog='see GitHub for more help') #This creates the basic framework

parser.add_argument('-fasta', metavar='--fa', help='Fasta file with genome assembly of interest') #This adds in actual arguments
#-h for help is a default argument

args = parser.parse_args()

### Get some basic information on each of the contigs ###

lst_seq_leng=[]
for seq_record in SeqIO.parse(args.fasta, "fasta"):
	hold=len(seq_record)
	lst_seq_leng.append(hold)

lst_A=[]	
for seq_record in SeqIO.parse(args.fasta, "fasta"):
	holding=seq_record.seq.upper().count("A")
	lst_A.append(holding)

lst_T=[]	
for seq_record in SeqIO.parse(args.fasta, "fasta"):
	holding=seq_record.seq.upper().count("T")
	lst_T.append(holding)
    
lst_C=[]	
for seq_record in SeqIO.parse(args.fasta, "fasta"):
	holding=seq_record.seq.upper().count("C")
	lst_C.append(holding)    

lst_G=[]	
for seq_record in SeqIO.parse(args.fasta, "fasta"):
	holding=seq_record.seq.upper().count("G")
	lst_G.append(holding)
    
### Get the totals ###

Tot_A=sum(lst_A)
Tot_T=sum(lst_T)
Tot_C=sum(lst_C)
Tot_G=sum(lst_G)
Tot_tot=sum(lst_seq_leng)

### Calculate some Genome Stats ###

lst_seq_leng.sort(reverse=True) #This orders list from largest to smallest (should be that way to begin with but this is just in case) 

running_sum=[]
N50=[]
L50=[]
for i in lst_seq_leng:
	running_sum.append(i)
	if sum(running_sum) < sum(lst_seq_leng)/2:
		continue
	elif sum(running_sum) > sum(lst_seq_leng)/2:
		N50=i
		L50=len(running_sum)
		break
        
running_sum=[]
N90=[]
L90=[]
for i in lst_seq_leng:
	running_sum.append(i)
	if sum(running_sum) < sum(lst_seq_leng)*0.9:
		continue
	elif sum(running_sum) > sum(lst_seq_leng)*0.9:
		N90=i
		L90=len(running_sum)
		break

### Print the results ###
print("Genome Composition")
#print("There are a total of %d contigs with an average length of %f" % (len(lst_seq_leng) , statistics.mean(lst_seq_leng))
print("The largrst contig is %d" % (max(lst_seq_leng)))
print("The smallest contig is %d" % (min(lst_seq_leng)))
print("A makes up %f percent of the genome" % (Tot_A/Tot_tot))
print("T makes up %f percent of the genome" % (Tot_T/Tot_tot))
print("C makes up %f percent of the genome" % (Tot_C/Tot_tot))
print("G makes up %f percent of the genome" % (Tot_G/Tot_tot))

print("Genome statistics")
print("THe N50 is %d" % (N50))
print("The L50 is %d" % (L50))
print("THe N90 is %d" % (N90))
print("The L90 is %d" % (L90))
