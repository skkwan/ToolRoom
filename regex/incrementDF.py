import re 

with open("temp.txt", "r") as f:
    for line in f.readlines():
        line = line.strip("\n")
        matches = re.findall("df_(\d+)", line)
        newline = line
        for num in matches: 
            old_str = "df_" + num 
            new_str = "df_" + str(int(num) + 1)
            newline = newline.replace(old_str, new_str)
        print(newline)
