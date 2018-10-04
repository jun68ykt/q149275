def count(name_id, indexes, data):
    name_index_ary = indexes[name_id]
    cnt = len(name_index_ary)

    for i in name_index_ary:
        code_id = data[i][1]
        code_index_ary = indexes[code_id]
        a = [j for j in code_index_ary if j > i]
        cnt += len(a)

    return cnt
