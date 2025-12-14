def get_image_path():
    while True:
        image_path= input("enter the path to the bmp image file:")
        try:
            with open (image_path, 'rb') as f:
                f.read(1)
            return image_path
        except:
            print("error: image file not found or cannot be opened. please try again.")

def get_message(max_bits):
    while True:
        message = input("Enter the secret message to hide:")
        bits=''.join(format(ord(c),'08b') for c in message)+'00000000'
        if len(bits)> max_bits:
            print("Error: message too long for this image. Please enter a shorter message. ")
        else:
            return bits

def encode_message(image_path):
    with open(image_path,'rb') as f:
        data = f.read()

    header_size = 54
    max_bits = (len(data) - header_size)  # 1 bit per byte
    bits = get_message_bits(max_bits)

    out = bytearray(data)
    bit_index = 0
    for i in range(header_size, len(out)):
        if bit_index >= len(bits):
            break
        out[i] = (out[i] & 0xFE) | int(bits[bit_index])
        bit_index += 1

    output_path = "hidden_message.bmp"
    with open(output_path, 'wb') as f:
        f.write(out)
    print("Message hidden successfully in:", output_path)    


def decode_message(image_path):
    with open(output_path,'rb')as f:
        data = f.read()

    header_size = 54
    bits = ''
    for i in range(header_size, len(data)):
        bits += str(data[i] & 1)

    # Convert bits to text until NULL terminator
    message = ''
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if byte == '00000000':
            break
        message += chr(int(byte, 2))

    print("Decoded message:", message)

def main():
    choice= input(" do you want to hide a message or reveal a message?").strip().lower()
    if choice not in ['hide','reveal']:
        print("error. Please restart the program.")
        return 
    
    image_path= get_image_path()

    if choice == 'hide':
        encode_message(image_path)
    else:
        decode_message(image_path)
    
if__name_=="__main__":
    main()