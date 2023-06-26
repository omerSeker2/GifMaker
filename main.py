from PIL import Image

my_image = Image.open("Sun.png")
my_image = my_image.resize((500, 500))
flipped = my_image.transpose(Image.FLIP_LEFT_RIGHT)
my_image.show()
flipped = my_image.rotate(180)
flipped.show()