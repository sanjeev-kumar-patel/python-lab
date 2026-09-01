t = (['a', 'b', 'c'], ['d', 'e', 'f'])

t[0].append('z')
t[1].remove('e')

t[0][1] = 'B'
t[1][0] = 'E'
t[1][1] = 'F'

print(t)