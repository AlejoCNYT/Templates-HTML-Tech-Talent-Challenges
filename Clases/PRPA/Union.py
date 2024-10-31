group_a = set(['perro','gato','serpiente'])
group_b = {'loro','mona','liebre','gato'}
group_c = {'gato','serpiente','cerdito','liebre'}

print("\n", group_a)
print(group_b)
print(group_c, "\n")

total_group = group_a.union(group_b).union(group_c)

print(total_group, "\n")

a_n_b = group_a.intersection(group_b)
a_n_c = group_a.intersection(group_c)
b_n_c = group_b.intersection(group_c)

print(a_n_b)
print(b_n_c)
print(a_n_c, "\n")

all_n = group_a.intersection(group_b).intersection(group_c)

print(all_n, "\n")

b_minus_a = group_b.difference(group_a)

print(b_minus_a, "\n")


