conj_A = {1,2,3,4}
conj_B = {2,9,8,3}

conj_Union = set()

print(conj_A)
print(conj_B)

for ele_a in conj_A:
    if ele_a in conj_B:
        conj_Union.add(ele_a)

print(conj_Union)
