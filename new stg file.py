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
        file_content =f.read()

    width=int.from_bytes(file_content[18:22], byteorder='little')
    height=int.from_bytes(file_content[22:26],byteorder='little')
    bytes_offset=int.from_bytes(file_content[10:14],byteorder='little')
    bits_per_pixel=int.from_bytes(file_content[28:30],byteorder='little')
    bytes_per_pixel= bits_per_pixel//8 
    n= bytes_per_pixel

    max_bits= width * height * n 
    bits =get_message(max_bits)

    file_content=list(file_content)
    bits_index=0 
    for i in range (bytes_offset, len(file_content),byteorder='little'):
        for channel in range (n):
            if bits_index <len(bits):
                file_content[i + channel] =(file_content[i + channel]&~1) | int(bits[bit_index]) 
                bits_index+=1
            else:
                break
        if bit_index>=len(bits):
            break
    output_path="hidden_message.bmp"
    with open(image_path,'wb') as f:
        f.write(bytes(files_content))
    print(f"Message hidden successfully in {output_path}")


def decode_message(image_path):
    with open(output_path,'rb')as f:
        file_content=f.read()

        bytes_offset=int.from_bytes(file_content[10:14],byteorder='little')
        bits_per_pixel=int.from_bytes(file_content[28:30],byteorder='little')
        bytes_per_pixel=bits_per_pixel//8
        n=bytes_per_pixel

        bits=''
        for i in range(bytes_offset,len(file_content),bytes_per_pixel):
            for channel in range(n):
                bits+= str(file_content[i + channel]& 1 )

        decode_message=''
        for i in range(0,len(bits),8):
            byte =bits[i:i +8]
            if byte=='00000000':
                break
            decoded_message+= chr(int(byte,2))
        
        print("Decoded message:", decoded_message )

