N = int(raw_input())
X = [float(i) for i in raw_input().split(" ")]
W = [int(i) for i in raw_input().split(" ")]

weighted_sum = sum([i*j for i,j in zip(X,W)])
weight_sum = sum(W)
weighted_mean = round(weighted_sum/weight_sum ,1)
print weighted_mean