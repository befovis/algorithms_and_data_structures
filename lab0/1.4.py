f = open("scr/input.txt")
a, b = map(int, f.readline().split())
f.close()
res = str(a + b**2)
w = open("scr/output.txt", 'w')
w.write(res)
w.close()