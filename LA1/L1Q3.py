from itertools import combinations

print("-"*25,"\nGowtham Karthikeyan S\n21BBS0157\nQuestion 3\n","-"*25)

transactions = [{'Orange Juice', 'Apple Juice'}, 
                {'Lemonade', 'Water', 'Oreo Milkshake'}, 
                {'Orange Juice', 'Lemonade'}, 
                {'Oreo Milkshake'}, 
                {'Apple Juice', 'Oreo Milkshake', 'Orange Juice'}, 
                {'Orange Juice', 'Apple Juice', 'Oreo Milkshake'}, 
                {'Oreo Milkshake', 'Lemonade'}, 
                {'Orange Juice', 'Lemonade', 'Water'}, 
                {'Apple Juice', 'Oreo Milkshake'}, 
                {'Water', 'Apple Juice'}, 
                {'Orange Juice', 'Water'}, 
                {'Lemonade', 'Apple Juice'}, 
                {'Oreo Milkshake', 'Water'}, 
                {'Orange Juice', 'Apple Juice', 'Lemonade'}, 
                {'Oreo Milkshake', 'Apple Juice'}, 
                {'Lemonade', 'Water'}]

min_support = 0.3
min_confidence = 0.4

def calculate_support(itemset, transactions):
    count = sum(1 for transaction in transactions if itemset.issubset(transaction))
    return count / len(transactions)

def generate_candidates(itemsets, length):
    return set(frozenset(i) for i in combinations(set().union(*itemsets), length))

def apriori(transactions, min_support):
    itemsets = [set([item]) for transaction in transactions for item in transaction]
    itemsets = list(set(frozenset(item) for item in itemsets))

    frequent_itemsets = {item: calculate_support(item, transactions) for item in itemsets}
    frequent_itemsets = {k: v for k, v in frequent_itemsets.items() if v >= min_support}

    length = 2
    while frequent_itemsets:
        current_frequent_itemsets = frequent_itemsets
        frequent_itemsets = {}

        candidates = generate_candidates(current_frequent_itemsets, length)
        for candidate in candidates:
            support = calculate_support(candidate, transactions)
            if support >= min_support:
                frequent_itemsets[candidate] = support

        if not frequent_itemsets:
            break

        length += 1

    return current_frequent_itemsets

def generate_rules(frequent_itemsets, transactions, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        subsets = [frozenset(x) for x in combinations(itemset, len(itemset) - 1)]
        for subset in subsets:
            confidence = frequent_itemsets[itemset] / calculate_support(subset, transactions)
            if confidence >= min_confidence:
                rules.append((subset, itemset - subset, confidence))
    return rules

frequent_itemsets = apriori(transactions, min_support)

rules = generate_rules(frequent_itemsets, transactions, min_confidence)
for rule in rules:
    print(f"Rule: {rule[0]} -> {rule[1]} (Confidence: {rule[2]:.2f})")
