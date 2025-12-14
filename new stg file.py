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

