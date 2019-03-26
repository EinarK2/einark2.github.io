n, r, c = [int(x) for x in input().split()]
l1 = []
l2 = []
l3 = []
for x in range(r):
    radirnofn = input()
    l1.append(radirnofn)
for x in l1:
    l3.extend(x.split())

for x in range(n):
    nofn = input()
    l2.append(nofn)
if l3[:c] == l2[:c]:
    print("left")
else:
    print("right")

if l3[c:] == l2[c:]:
    print("left")
else:
    print("right")
