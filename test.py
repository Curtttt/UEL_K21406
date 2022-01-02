start, end, quantity, j = [], [], [], 0
p = int(input())
m = input()
n = m.split()

while j<p-1:
    if int(n[j])*int(n[j+1]) < 0:
        start.append(j)
        i = j
        while i<p-1:
            if int(n[i])*int(n[i+1]) > 0:
                end.append(i)
                break
            else:
                i += 1
                if i+1 == p:
                    end.append(i)
        j = i + 1
    else:
        j += 1

for i in range(len(end)):
    quantity.append(end[i] - start[i] + 1)

x = quantity.index(max(quantity))
print("\n" + str(quantity[x]))
for i in range(start[x], end[x]+1):
    print(n[i], end=" ")




