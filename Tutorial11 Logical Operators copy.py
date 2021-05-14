has_high_income = False
has_good_credit = True

# the 'and' operator states that both circumstances have to be true to work
# the 'or' operator states that even if either circumstances are true, it will work.


if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
