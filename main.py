# This is a sample Python script.
#
# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.
# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
# Додатково:
# Створіть програму, яка перевіряє текст на неприпустимі слова.
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
# За підсумками роботи програми необхідно показати статистику дій.
# Наприклад, якщо й у нас є такий текст:
# To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of
# outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep;
# No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to,
# 'tis a consummation Devoutly to be wish'd. To die, to sleep.
# Неприпустиме слово: die.
# Результат:
# To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of
# outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To ***: to sleep;
# No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to,
# 'tis a consummation Devoutly to be wish'd. To ***, to sleep.
# Статистика: 2 заміни слова die.
# Нотатка:
# Текст для всіх завдань можна написати самостійно або взяти з Інтернету.
# Логіка має працювати з будь-яким текстом.


with open("text1.txt", "w") as text_any:
    text_any.write("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer "
                   "The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles,"
                   " And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The"
                   " heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation"
                   " Devoutly to be wish'd. To die, to sleep.")

#


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
    words = line.split()
    word_count = 0
    for word in words:
        word_count += 1
print(f"Your text has total {word_count} words")


