#1. Определение количества различных подстрок с использованием хэш-функции.
#Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
#Требуется найти количество различных подстрок в этой строке.

def findsubs(instr):
  subdictionary={}
  for i in range(len(instr)):
    for j in range(i+2, len(instr)+1):
      subdictionary[instr[i:j]] = subdictionary.get(instr[i:j],0) + 1
  return subdictionary

word = 'geekbrains'
print (findsubs(word))

#2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

def frequency(s):
    chars = {}
    for char in s:
        chars.update({char: chars[char] + 1 if char in chars else 1})
    return chars

three_words = 'some three words'
print(f'Частота букв{frequency(three_words)}')