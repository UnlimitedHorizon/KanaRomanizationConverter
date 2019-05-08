
import os
import json

from .romanization_list import romanization_list


def generate_dictionary():
    path = os.path.dirname(os.path.abspath(__file__))

    char_dict_list = list()

    # 0x3041-0x309f
    for i in range(0x3041, 0x309f):
        if i-0x3041 >= len(romanization_list):
            continue
        s1 = "\\u{:0>4}".format(hex(i)[2:])
        s2 = "\\u{:0>4}".format(hex(i + 0x60)[2:])
        # obj = [<hiragana>, <hiragana_utf-8>, <katakana>, <katakana_utf-8>, <romanization>]
        obj = list()
        obj.append(s1)
        obj.append(s1.encode('latin-1').decode('unicode_escape'))
        obj.append(s2)
        obj.append(s2.encode('latin-1').decode('unicode_escape'))
        obj.append(romanization_list[i-0x3041])

        char_dict_list.append(obj)

    json_str = str(char_dict_list)
    json_str = json_str.replace("\'", "\"")
    json_str = json_str.replace("\\\\", "\\")
    json_str = json_str.replace("[[", "[\n\t[", 1)
    json_str = json_str.replace("], [", "],\n\t[")
    json_str = json_str.replace("]]", "]\n]")
    
    with open(path + "/dictionary.json", "w") as output_file:
        output_file = open(path + "/dictionary.json", "w")
        output_file.write(json_str)

if __name__ == "__main__":
    generate_dictionary()
