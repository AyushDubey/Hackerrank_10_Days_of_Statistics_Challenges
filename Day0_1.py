# Enter your code here. Read input from STDIN. Print output to STDOUT
# reading input data 
N = int(raw_input())
X = [float(i) for i in raw_input().split(" ")]
X_sorted = sorted(X)

# mean
print round(sum(X)/N, 1)

# median
if N%2 == 0:
	print round((X_sorted[N/2] + X_sorted[N/2 - 1])/2 ,1)
else:
	print round((X_sorted[N/2] + X_sorted[N/2 + 1])/2 ,1)

# mode
X_dict = {i:X.count(i) for i in X}
max_val = max(X_dict.values())
a = []
for k,v in X_dict.items():
	if v == max_val:
		a.append(k)
print int(min(a))