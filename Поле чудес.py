words = ["автомобиль", "кот", "гитара", "река", "книга", "солнце", "дерево", "компьютер", "путешествие", "искусство"]
guessed_letters = []
attempts = 7
word_index = 0  
print("Добро пожаловать в игру 'Поле чудес!'")
print("Сегодня у нас на кону замечательные призы!")
while attempts > 0:
    secret_word = words[word_index]  
    print("\nУгадайте слово, которое состоит из " + str(len(secret_word)) + " букв.")
    current_word = ''
    for letter in secret_word:
        if letter in guessed_letters:
            current_word += letter
        else:
            current_word += '_'
    print("Слово: ", current_word)
    entered_letter = input("Введите букву: ").lower()
    if len(entered_letter) != 1 or not ('а' <= entered_letter <= 'я' or entered_letter == 'ё'):
        print("Пожалуйста, введите одну русскую букву.")
        continue
    if entered_letter in guessed_letters:
        print("Вы уже называли эту букву. Попробуйте другую.")
        continue
    guessed_letters.append(entered_letter)
    if entered_letter in secret_word:
        print("Поздравляем! Буква '" + entered_letter + "' есть в слове.")
    else:
        attempts -= 1
        print("К сожалению, буквы '" + entered_letter + "' нет в слове. Осталось попыток: " + str(attempts))
    word_guessed = True
    for letter in secret_word:
        if letter not in guessed_letters:
            word_guessed = False
            break
    if word_guessed:
        print("Поздравляем! Вы выиграли: '" + secret_word + "'")
        break
else:
    print("Вы проиграли! Загаданное слово было: '" + secret_word + "'")
