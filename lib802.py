import lab06_5

"""Return number of vowels in a file"""

def countVowelsInFile(file_name):
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
    # print countVowelsInFile('notes.py')
    print countVowelsInFile(raw_input("Enter filename"))

main()
