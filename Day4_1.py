import math as m
Ratio = [float(i) for i in raw_input().split(" ")]
B_Ratio = Ratio[0]
G_Ratio = Ratio[1]

p = B_Ratio/(B_Ratio+G_Ratio) # probability of boy
q = 1 - p # probability of girl

Pr_3B_6 = m.factorial(6)/(m.factorial(3)*m.factorial(3)) * p**3 * q**3
Pr_4B_6 = m.factorial(6)/(m.factorial(4)*m.factorial(2)) * p**4 * q**2
Pr_5B_6 = m.factorial(6)/(m.factorial(5)*m.factorial(1)) * p**5 * q**1
Pr_6B_6 = m.factorial(6)/(m.factorial(6)*m.factorial(0)) * p**6 * q**0

Pr = Pr_6B_6+Pr_5B_6+Pr_4B_6+Pr_3B_6
print round(Pr,3)