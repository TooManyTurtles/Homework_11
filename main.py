
# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.
# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.

# To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of
# outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep;
# No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to,
# 'tis a consummation Devoutly to be wish'd. To die, to sleep.



with open("text1.txt", "w") as text_any:
    text_any.write("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer "
                   "The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles,"
                   " And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The"
                   " heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation"
                   " Devoutly to be wish'd. To die, to sleep.")


# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.

with open("text7.txt", "w") as text7:
    with open("text1.txt", "r") as text_any:
        for line in text_any:
            line = line.strip()
            line = line.translate(line.maketrans(',', ' '))
            line = line.translate(line.maketrans('.', ' '))
            words = line.split()
            for word in words:
                if len(word) >= 7:
                    text7.write(f"{word} ")

with open("text7.txt", "r") as text7:
    print(f"These are seven or more letter words in your file: {text7.read()}")

# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.


with open("text1.txt", "r") as text_any:
    for line in text_any:
        result = len(line.split(" "))
    print(result)




