import lab06_5
import os
"""Return number of vowels in a directory"""

def countVowelsInDir(file_name):
    try:
        file_object = open(file_name)
        vowel_count = 0
        for line in file_object:
            vowel_count += lab06_5.CountVowels(line)
            # print vowel_count, line
        file_object.close()
        return vowel_count
    except IOError, info:
        print info

def main():
    global_vowel_count = 0
    for (current_dir, dir_list, file_list) in os.walk('testdir'):
        # print list of directories
        # print os.path.abspath(current_dir)
        for file_name in file_list:
            # print list of files with their vowel coutns
            # print file_name, countVowelsInDir(file_name)
            global_vowel_count += countVowelsInDir(file_name)
    print global_vowel_count

main()
