def get_image_path():
    while True:
        image_path= input("enter the path to the bmp image file:")
        try:
            with open (image_path, 'rb') as f:
                f.read(1)
            return image_path #try opening a bmp file and reading a byte if suceeds then this file is acessible
        except:
            print("error: image file not found or cannot be opened. please try again.")
            #if fail shows an error message explaining to the user. 
def get_message(max_bits):
    while True: # asks for the secret message and makes sure it fits in the bmp image 
        message = input("Enter the secret message to hide:")
        bits=''.join(format(ord(c),'08b') for c in message)+'00000000' #turns each character into 8 bits then adds a null terminator 
        if len(bits)> max_bits:
            print("Error: message too long for this image.") #appears if message is too big 
        else:
            return bits

def encode_message(image_path): # hides the message in the bmp image 
    with open(image_path,'rb') as f: # reads the whole bmp image as bytes 
        data = f.read()

    header_size = 54
    max_bits = (len(data) - header_size)  #geet a message that fits 
    bits = get_message(max_bits)

    out = bytearray(data)
    bit_index = 0
    for i in range(header_size, len(out)):
        if bit_index >= len(bits):
            break
        out[i] = (out[i] & 0xFE) | int(bits[bit_index])# clear the LSB and set it to the message bit    
        bit_index += 1 # move to the next bit

    output_path = "hidden_message.bmp" # save the new image with the hidden message
    with open(output_path, 'wb') as f:
        f.write(out)
    print("Message hidden successfully in:", output_path)   # tell the user it worked 
    print(f"saved as '{output_path}'.")
    return output_path



def decode_message(image_path): #reads the hidden bits and rebuilds the original message 
    with open(image_path,'rb')as f:
        data = f.read()

    header_size = 54 # skips the header 
    bits = '' #collects LSBs into a big string of '0' and '1's 
    for i in range(header_size, len(data)):
        bits += str(data[i] & 1)

    message = '' #turns each 8 bits into a character until it hits the end marker 
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if byte == '00000000': #stop when it sees the null terminator 
            break
        message += chr(int(byte, 2)) # converts the 8 bits to a character and adds it to the message

    print(f"Decoded message:", {message})
    
def main(): #seeing what the user wants to do
    choice = input("do you want to hide a message or reveal a message or exit the program?").strip().lower()

    if choice not in ['hide', 'reveal', 'exit']: # if its not a valid option, stop the program 
        print("error. Please restart the program.")
        return

    if choice == 'exit':
        print("exiting program.")
        return

    image_path = get_image_path()

    if choice == 'hide':
        stego_path = encode_message(image_path)
        if stego_path:
            print(f"\nSaved as '{stego_path}'. Do you want to decode it now? ")
            decode_message(stego_path)
    elif choice == 'reveal':
        decode_message(image_path)

    
if __name__=="__main__":
    main() 