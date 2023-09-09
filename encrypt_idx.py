f = open("module1.py", "r")
code_lines = f.readlines()
f.close()

encryption_idx = []
for i in range(len(code_lines)):
    encryption_idx.append("1\n")

f = open("encryption_idx_csv.csv", "w")
f.writelines(encryption_idx)
