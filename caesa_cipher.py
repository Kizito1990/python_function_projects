alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


from art import logo
print(logo)


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def ceaser(start_text, shift_amount, ceaser_direction):
    end_text = ""
    if ceaser_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here is the {ceaser_direction}d result: {end_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    ceaser( start_text= text,shift_amount= shift, ceaser_direction= direction)

    restart = input("Type 'Yes' if you wnat to continue. Otherwise, Type 'No' \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")

