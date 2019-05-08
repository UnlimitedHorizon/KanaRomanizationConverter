import os
import json

from .romanization_list import romanization_list

def str_kana_to_roman(s):
    s_split = list(s)
    for i in range(len(s)):
        c = s[i]
        unicode_str = str(c.encode("unicode_escape"))
        if len(unicode_str) != 10:
            continue
        unicode_num = int(unicode_str[5:-1], 16)
        if 0 <= unicode_num - 0x3041 < len(romanization_list):
            s_split[i] = romanization_list[unicode_num - 0x3041]
        elif 0 <= unicode_num - 0x30a1 < len(romanization_list):
            s_split[i] = romanization_list[unicode_num - 0x30a1]
    else:
        return s_split

def char_kana_to_roman(c):
    unicode_str = str(c.encode("unicode_escape"))
    if len(unicode_str) != 10:
        return c
    unicode_num = int(unicode_str[5:-1], 16)
    if 0 <= unicode_num - 0x3041 < len(romanization_list):
        return romanization_list[unicode_num - 0x3041]
    elif 0 <= unicode_num - 0x30a1 < len(romanization_list):
        return romanization_list[unicode_num - 0x30a1]
    return c
