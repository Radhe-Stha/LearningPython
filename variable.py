#store your expenses from sunday to saturday and find total expenses and find average expenses
print(f"Day  \t \t Expenses(Rs.)")
print()
exp_sun = 1000
exp_mon = 800
exp_tue = 800
exp_wed = 1000
exp_thur = 700
exp_fri = 500
exp_sat = 1000

total_exp = exp_sun + exp_mon + exp_tue + exp_wed + exp_thur + exp_fri + exp_sat

avg_exp = total_exp / 7

print(f"Sunday   \t=  {exp_sun}")
print(f"Monday    \t=  {exp_mon}")
print(f"Tuesday    \t=  {exp_tue}")
print(f"Wednesday    \t=  {exp_wed}")
print(f"Thursday    \t=  {exp_thur}")
print(f"Friday   \t=  {exp_fri}")
print(f"Saturday    \t=  {exp_sat}")
print()
print(f"Total expenses  \t=  Rs. {total_exp}")
print(f"Average expenses  \t=  Rs. {avg_exp}")
