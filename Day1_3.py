N = int(raw_input())
X = [float(i) for i in raw_input().split(" ")]

mean = round(sum(X)/N, 1)

X_mean_sq = [round((i-mean)**2,1) for i in X] 

sum_X_mean_sq = round((sum(X_mean_sq)/N)**0.5, 1)

print sum_X_mean_sq
