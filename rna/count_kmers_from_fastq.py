#!/usr/bin/env python

import os, sys

from sequence_to_kmer_list import *
from fastq_file_to_sequence_list import *
from shannon_entropy import *

## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }

def count_kmers(kmer_list):

    kmer_count_dict = dict()
    for kmers in kmer_list:
        for kmer in kmers:
            if kmer in kmer_count_dict:
                kmer_count_dict[kmer] += 1
            else:
                kmer_count_dict[kmer] = 1

    return kmer_count_dict


def main():

    progname = sys.argv[0]

    usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(
        progname
    )

    if len(sys.argv) < 4:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    kmer_length = int(sys.argv[2])
    num_top_kmers_show = int(sys.argv[3])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    all_kmers = []
    for sequence in seq_list:
        all_kmers.append(sequence_to_kmer_list(sequence,kmer_length))

    kmer_count_dict = count_kmers(all_kmers)
    unique_kmers = [sorted(kmer_count_dict.items(), key = lambda pair: pair[1], reverse = True)[i][0] for i in range(len(kmer_count_dict))]
    
    kmer_ent_dict = {}
    for kmers in all_kmers:
        for kmer in kmers:
            if kmer not in kmer_ent_dict:
                kmer_ent_dict[kmer] = entropy(kmer)

    ## printing the num top kmers to show
    top_kmers_show = unique_kmers[0:num_top_kmers_show]

    print('kmer\tcount\tentropy')
    for kmer in top_kmers_show:
        print("{}:\t{}\t{}".format(kmer, kmer_count_dict[kmer], kmer_ent_dict[kmer]))

    sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
    main()
