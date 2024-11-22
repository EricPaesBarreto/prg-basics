# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
total_per_week = []
total_expense = [0, 0, 0]
total = 0
for week in monthly_expenses:
    sum = 0
    for expense in range(len(week)):
        total_expense[expense] += week[expense]
        sum += week[expense]
        total += week[expense]
    total_per_week.append(sum)


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',total_expense[0])
print('Transport:',total_expense[1])
print('Utilities:',total_expense[2])
print('Week 1:',total_per_week[0])
print('Week 2:',total_per_week[1])
print('Week 3:',total_per_week[2])
print('Week 4:',total_per_week[3])
print('---------------')
print('TOTAL:',total)