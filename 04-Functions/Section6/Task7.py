def is_binary(bin_num):
    str_bin_num = str(bin_num)
    if str_bin_num.count('0') + str_bin_num.count('1') == len(str_bin_num):
        return True
    else:
        return False