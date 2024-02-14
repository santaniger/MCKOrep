#какое счастье, что VS Code отказывается устанавливать кит для c++
data = []

with open ("space.txt", "r", encoding="utf-8") as file:
    # skip the line 1
    line = file.readline()
    i = 0
    # read lines 2 - 101
    while (i < 100):
        line = file.readline()
        # "LOСА-302*Голевард*x y*xd yd" -> ['LOСА-302', 'Голевард', 'x y', 'xd yd']
        line = line.strip().split("*")
        # 'LOСА-302' -> ['LOСА', '302']
        line[0] = line[0].split("-")
        # "x y" -> ['x', 'y']
        line[2] = line[2].split(" ")
        # "xd yd" -> ['xd', 'yd']
        line[3] = line[3].split(" ")
        n = int(line[0][1][0])
        m = int(line[0][1][1])
        t = len(line[1])
        xd = int(line[3][0])
        yd = int(line[3][1])
        if (line[2][0] == '0'):
            if (int(line[0][1][0]) > 5):
                line[2][0] = str(n + xd)
            if (int(line[0][1][0]) <= 5):
                line[2][0] = str(-1*(n + xd) * 4 + t)

        if (line[2][1] == '0'):
            if (int(line[0][1][1]) > 3):
                line[2][1] = str(m + t + yd)
            if (int(line[0][1][1]) <= 3):
                line[2][1] = str(-1 * (n + yd) * m)
        data.append(line)
        i += 1

with open ("space_new.txt", "w", encoding="utf-8") as file:
    for line in data:
        file.write('<' + line[0][0] + '-' + line[0][1] + '> - (<' + line[2][0] + '>, <' + line[2][1] + '>)\n')
        if (line[0][0][3] == "V") :
            print(('<' + line[0][0] + '-' + line[0][1] + '> - (<' + line[2][0] + '>, <' + line[2][1] + '>)'))

