#!/usr/bin/python3
import os
import operator
from collections import defaultdict
from itertools import combinations, chain


class Apriori:

    def __init__(self, minSupport):
        #Constructor
        self.support_count = defaultdict(int)
        self.minSupport = minSupport

    def read_transactions_from_file(self, transaction_file):
        #Read transactions from the input file.
        with open(transaction_file, "r") as infile:
            transactions = [set(line.rstrip("\n").split(";"))
                            for line in infile]

            return transactions

    def get_one_itemset(self, transactions):
        #Gets unique items from the list of transactions.
        one_itemset = set()
        for transaction in transactions:
            for item in transaction:
                one_itemset.add(frozenset([item]))

        return one_itemset

    def self_cross(self, Ck, itemset_size):        
        #Takes union of a set with itself to form bigger sets.
        Ck_plus_1 = {itemset1.union(itemset2)
                     for itemset1 in Ck for itemset2 in Ck
                     if len(itemset1.union(itemset2)) == itemset_size}
        return Ck_plus_1

    def prune_Ck(self, Ck, Lk_minus_1, itemset_size):
        # a set of k-itemsets with Ck's whose Ck_minus_1's are in Lk_minus_1
        Ck_ = set()
        for itemset in Ck:
            Ck_minus_1 = list(combinations(itemset, itemset_size-1))
            flag = 0
            for subset in Ck_minus_1:
                if not frozenset(subset) in Lk_minus_1:
                    flag = 1
                    break
            if flag == 0:
                Ck_.add(itemset)
        return Ck_

    def get_min_supp_itemsets(self, Ck, transactions):
        #Returns those itemsets whose support is > minSupport
        temp_freq = defaultdict(int)
        # update support count of each itemset
        for transaction in transactions:
            for itemset in Ck:
                if itemset.issubset(transaction):
                    temp_freq[itemset] += 1
                    self.support_count[itemset] += 1

        N = len(transactions)
        Lk = [itemset for itemset, freq in temp_freq.items()
              if freq/N > self.minSupport]
        return set(Lk)

    def frequent_item_set(self, transactions):
        #returns each itemset in K_itemset has support > minSupport
        K_itemsets = dict()
        Ck = self.get_one_itemset(transactions)
        Lk = self.get_min_supp_itemsets(Ck, transactions)
        k = 2
        while len(Lk) != 0:
            K_itemsets[k-1] = Lk
            Ck = self.self_cross(Lk, k)
            Ck = self.prune_Ck(Ck, Lk, k)
            Lk = self.get_min_supp_itemsets(Ck, transactions)
            k += 1

        return K_itemsets

    def subsets(self, iterable):
        #Returns subsets of a set.
        list_ = list(iterable)
        subsets_ = chain.from_iterable(combinations(list_, len)
                                       for len in range(len(list_)+1))
        subsets_ = list(map(frozenset, subsets_))

        return subsets_

    def write_part_1(self, K_itemsets):   
        #Writes Length 1 frequent itemsets with their support to a file.   
        main_dir = "./results/part_A - L1 Frequent Categories"
        if not os.path.exists(main_dir):
            os.makedirs(main_dir)

        outfile_path = "./results/part_A - L1 Frequent Categories/patterns.txt"
        with open(outfile_path, "w") as outfile:
            for key, values in K_itemsets.items():
                if key > 1:
                    break
                for value in values:
                    support_ct = self.support_count[value]
                    outfile.write("{support}:{label}\n".format(
                        support=support_ct,
                        label=";".join(list(value))
                    ))

    def write_part_2(self, K_itemsets):        
        #Writes the frequent itemsets with their support to a file.     
        main_dir = './results/part_B - All Frequent Categories'
        if not os.path.exists(main_dir):
            os.makedirs(main_dir)

        outfile_path = "./results/part_B - All Frequent Categories/patterns.txt"
        with open(outfile_path, "w") as outfile:
            for key, values in K_itemsets.items():
                for value in values:
                    support_ct = self.support_count[value]
                    outfile.write("{support}:{label}\n".format(
                        support=support_ct,
                        label=";".join(list(value))
                    ))


if __name__ == "__main__":
    print("Assignment 2 | CSOE17 Big Data Analytics | 114117098")
    print("Processing...")

    in_transaction_file = "./categories.txt"
    ap = Apriori(minSupport=0.01) #given in problem statement
    transactions = ap.read_transactions_from_file(in_transaction_file)
    K_itemsets = ap.frequent_item_set(transactions)
    ap.write_part_1(K_itemsets)  
    ap.write_part_2(K_itemsets)
  
    print("•○| Results generated, they can be found at /results |○•")