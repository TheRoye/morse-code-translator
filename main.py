from equivalencies import equivalencies



def text_to_morse(text):
    morse = ''
    for char in text:
        if char == ' ':
            morse += '| '
        else:
            morse += equivalencies[char.upper()] + ' '
    return morse

def get_key_from_value(dictionary, val):
    keys = [k for k, v in dictionary.items() if v == val]
    if keys:
        return keys[0]
    return None


def morse_to_text(morse):
    text = ''
    morse_list = morse.split()
    for letter in morse_list:
        if letter == '|':
            text += ' '
        else:
            char = get_key_from_value(equivalencies, letter)
            text += char
    return text.capitalize()
    
while True:
    translation_type = ''
    while translation_type != 'T' and translation_type != 'M':
        translation_type = input("Do you want translate morse to text (m) or text to morse (t)?: ").upper()
        
    var_text = input('Text to translate: ')
    if translation_type == 'T':
        print(text_to_morse(var_text))
    else:
        print(morse_to_text(var_text))
    
    again=''
    
    while again != 'Y' and again != 'N':
        again = input('Another translation? (Y) for yes /(N) for no: ').upper()
    
    if again == 'N':
        break

print('Bye!') 
    
    
        