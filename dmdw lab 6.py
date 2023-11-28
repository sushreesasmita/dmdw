from itertools import combinations
from collections import defaultdict
transactions = [['M', 'O', 'N','K','E','Y'],
                ['D', 'O', 'N','K','E','Y'],
                ['M', 'A', 'K','E'],
                ['M', 'U','C','K','Y'],
                ['C','O','O','K','I','E']]
min_support = 3
item_counts = defaultdict(int)

for transaction in transactions:
    for item in transaction:
        item_counts[item] += 1
L1 = {item: count for item, count in item_counts.items() if count >= min_support}
C2 = list(combinations(L1.keys(), 2))

C2_counts = defaultdict(int)

for transaction in transactions:
    for itemset in C2:
        if all(item in transaction for item in itemset):
            C2_counts[itemset] += 1

L2 = {itemset: count for itemset, count in C2_counts.items() if count >= min_support}
C3 = list(combinations(L1.keys(), 3))


C3_counts = defaultdict(int)
for transaction in transactions:
    for itemset in C3:
        if all(item in transaction for item in itemset):
            C3_counts[itemset] += 1

L3 = {itemset: count for itemset, count in C3_counts.items() if count >= min_support}
print("C1 (Candidate 1-Itemsets):")
print(list(item_counts.keys()))
print("\nL1 (Frequent 1-Itemsets):")
print(L1)
print("\nC2 (Candidate 2-Itemsets):")
print(C2)
print("\nL2 (Frequent 2-Itemsets):")
print(L2)
print("\nC3 (Candidate 3-Itemsets):")
print(C3)
print("\nL3 (Frequent 3-Itemsets):")
print(L3)





