from collections import defaultdict, Counter

transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]

trans_dict = defaultdict(list)
for account, amount in transactions:
    trans_dict[account].append(amount)


print(trans_dict)
trans_dict = {account: [sum(amount)] for account, amount in trans_dict.items()}
print(trans_dict)