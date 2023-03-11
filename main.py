import re
from pprint import pprint
# Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# Ваш код
contacts_list_correct = contacts_list
phone_list = []
occupation_list = []
status_list = []
for string in contacts_list:
    for sub_string in string:
        name_pattern = re.compile(r"([А-ЯЁ]\w+)?[\,\s]?([А-ЯЁ]\w+)?[\,\s]?([А-ЯЁ]\w+)")
        name = re.search(name_pattern, sub_string)
        name_replace = "\\1, \\2, \\3"
        result_name = re.sub(name_pattern, name_replace, sub_string)
        # if name is not None:
        #     contacts_list_correct.append(result_name.split(', '))
        pprint(result_name)
        occupation_pattern = re.compile(r"\,([А-ЯЁ]\w+)\,[а-яё\,]")
        occupation = re.search(occupation_pattern, sub_string)
        if occupation is not None:
            occupation_replace = "\\1"
            result_occupation = re.sub(occupation_pattern, occupation_replace, result_name)

        phone_pattern = re.compile(r"\+?([78])?\s?\(?(\d{3}?)\)?[\s-]?(\d{3})"
                                   r"[\s-]?(\d{2})[\s-]?(\d{2})\)?\s?(\(?доб?\.?\s(\d+)\)?)?")
        phone = re.search(phone_pattern, sub_string)
        if phone is not None:
            if len(phone.group()) > 20:
                phone_replace = "+7 (\\2) \\3-\\4-\\5 доп. \\7"
            else:
                phone_replace = "+7 (\\2) \\3-\\4-\\5"
            result_phone = re.sub(phone_pattern, phone_replace, result_name)
            pprint(result_phone)
i = 0
for j in occupation_list:
    contacts_list_correct[i].append(j)
    i += 1
i = 0
for k in phone_list:
    contacts_list_correct[i].append(k)
    i += 1

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')

    # Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)
