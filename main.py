import random

#1.
p = random.sample(range(101), 9)
print("pole:", p)

#2. p[0] a p[-1] ma znamenat prvni a posledni hodnotu a prostredni hodnotu dostaneme jenom s deleni ji pres 2
h1 = p[0]
ph = p[len(p) // 2]
poh = p[-1]
#f pred zavorkama oznacuje ze je tam vlozena hodnota promene ale slo by taky pouzit + str(neco)
print(f"prvni hodnota: {h1}")
print(f"prostredni hodnota: {ph}")
print(f"posledni hodnota: {poh}")

#3.
p[4] = 34
print (p)

#4.
print (p[6])

#5.
dp = len(p)
print (dp)

#6.
mh = min(p)
mah = max(p)
print (mh)
print (mah)

#7
p2 = random.sample(range(301), 5)
print ("pole 2:", p2)

#8
clp = sum(p2)
print (clp)

#9
pl = p2[1] + p2[4]
print (pl)