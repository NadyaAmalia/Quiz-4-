listGPA = [2.1,2.5,4,3]
for b in range (4):
    print(listGPA[b])

def bonus(a):
    bonus = a*500000
    return bonus

for a in listGPA:
    if a > 2.5:
        print("selamat anda mendapatkan bonus sebesar: ",bonus(a))
    else:
        print("maaf anda tidak mendapatkan bonus")
