from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here's the {encode_or_decode}d result: {output_text}")


switch = True
while switch == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    try:
        shift = int(input("Type the shift number:\n"))
    except:
        pass
    try:
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    except:
        pass

    loop = input("Type 'yes' if you want to again. Otherwise type 'no'.\n").lower()
    if loop != "yes":
        switch = False



