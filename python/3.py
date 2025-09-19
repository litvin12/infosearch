# Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,
# находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Напишите программу,
# которая реализует шифрование Цезаря. Входные данные: путь до изначального файла с текстом, требуемый сдвиг
# и язык текста(на выбор английский либо русский). Результат работы - новый файл с зашифрованным текстом.

def caesar_encrypt(text, shift, lang):
    result = ""
    ranges = {
        'русский': [(1040, 1071), (1072, 1103), 32],
        'английский': [(65, 90), (97, 122), 26]
    }
    upper, lower, size = ranges[lang]
    
    for char in text:
        code = ord(char)
        if upper[0] <= code <= upper[1]:
            result += chr((code - upper[0] + shift) % size + upper[0])
        elif lower[0] <= code <= lower[1]:
            result += chr((code - lower[0] + shift) % size + lower[0])
        else:
            result += char
    return result

# Основная программа
file_path = input("Путь к файлу: ")
shift = int(input("Сдвиг: "))
language = input("Язык (русский/английский): ").lower()

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

encrypted = caesar_encrypt(text, shift, language)
output_file = file_path.replace('.txt', '_encrypted.txt') or file_path + '_encrypted'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(encrypted)

print(f"Зашифрованный файл: {output_file}")