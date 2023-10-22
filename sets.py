#  12 files in total (2 intitial -> 4 sets -> 8 sorted sets)
arsh, arco = [], []
with open("shell.txt", "r") as shell, open("comb.txt", "r") as comb:
    arsh, arco = shell.read().split('\n'), comb.read().split('\n')
    sarsh, sarco = set(arsh), set(arco)
    

    union = sarsh.union(sarco)
    shnco = sarsh.intersection(sarco)
    diff = sarsh.difference(sarco)
    # diffr = sarco.difference(sarsh)
    symdiff = sarsh.symmetric_difference(sarco)
with open("union.txt", "w+") as f_union, open("inters.txt", "w+") as f_inters, open("diff.txt", "w+") as f_diff, open("symdiff.txt", "w+") as f_symdiff:
    for ele in union:
        f_union.write(str(ele)+'\n')
    for ele in shnco:
        f_inters.write(str(ele)+'\n')
    for ele in diff:
        f_diff.write(str(ele)+'\n')
    for ele in symdiff:
        f_diff.write(str(ele)+'\n')
    print(len(diff))
    print(len(symdiff))
    print(len(shnco))
    print(len(union))