f = open('input.txt')
c = f.read().split()
f.close()
total = int(c[0]) + int(c[1]) ** 2
f = open('output.txt', 'w')
f.write(str(total))
f.close()