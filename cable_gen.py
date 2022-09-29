import string

alpha = list(string.ascii_uppercase)

column_num = 24
row_num = 8

S0_num = 12

PN_lbl = []

for c in range(column_num):
    if c < 9:
        c = '0' + str(c+1)
    else:
        c = str(c+1)
    for s in range(S0_num):
        if (s%2) == 0:
            sl = '1'
        if (s%2) == 1:
            sl = '2'
        for r in range(row_num):
            row = str(alpha[r])
            if (r%2) == 0:
                lbl = row + 'P'
            if (r%2) == 1:
                lbl = row + 'N'
            position_lbl = 'S' + c + '_' + sl + lbl
            PN_lbl.append(position_lbl)

print(PN_lbl)

clm_lbl = []
for c in range(column_num):
    c = 'C' + str(c+1)
    clm_lbl.append(c)

print(clm_lbl)

S0_lbl = []
for s in range(S0_num):
    if s < 9:
        s = 'S0' + str(s+1)
    else:
        s = 'S' + str(s+1)
    S0_lbl.append(s)

print(S0_lbl)