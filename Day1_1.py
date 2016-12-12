N = int(raw_input())
X = [int(i) for i in raw_input().split(" ")]

X_sorted = sorted(X)
if N%2 == 0:
	X1_sorted = X_sorted[0:N/2]
	N1 = len(X1_sorted)
	Q1 = (X1_sorted[N1/2] + X1_sorted[N1/2 - 1])/2

	Q2 = (X_sorted[N/2] + X_sorted[N/2 - 1])/2

	X2_sorted = X_sorted[N/2:N]
	N2 = len(X2_sorted)
	Q3 = (X2_sorted[N2/2] + X2_sorted[N2/2 - 1])/2
	
else:
	X1_sorted = X_sorted[0:N/2]
	N1 = len(X1_sorted)
	Q1 = (X1_sorted[N1/2] + X1_sorted[N1/2 - 1])/2
	
	Q2 = X_sorted[N/2]

	X2_sorted = X_sorted[N/2 + 1:N]
	N2 = len(X2_sorted)
	Q3 = (X2_sorted[N2/2] + X2_sorted[N2/2 - 1])/2

print Q1
print Q2
print Q3