def get_image_path():
    while True:
        image_path= input("enter the path to the bmp image file:")
        try:
            with open (image_path, 'rb') as f:
                f.read(1)
            return image_path
        except:
            print("error: image file not found or cannot be opened. please try again.")

