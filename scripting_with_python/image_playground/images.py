from PIL import Image, ImageFilter

# Blurred Mountains
img = Image.open('./mountains.jpg')
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.save('blurred_image.jpg', 'jpeg')

# Grayscaled Ocean
img2 = Image.open('./ocean.jpg')
grayscaled_img = img2.convert('L')
grayscaled_img.save('grayscaled_image.jpg', 'jpeg')

# Rotated Sky
img3 = Image.open('./sky.jpg')
rotated_img = img3.rotate(90)
rotated_img.save('rotated_image.jpg', 'jpeg')

# Resized Image
img4 = Image.open('./sky.jpg')
resized_img = img4.resize((300, 300))
resized_img.save('resized_image.jpg', 'jpeg')

# Cropped Image
img5 = Image.open('./mountains.jpg')
box = (100, 100, 400, 400)
cropped_img = img5.crop(box)
cropped_img.save('cropped_image.jpg', 'jpeg')

# Resized astro.jpg to a thumbnail size
astro_img = Image.open('./astro.jpg')
# thumbnail() retains aspect ratio
astro_img.thumbnail((400, 200))
astro_img.save('astro_thumbnail.jpg', 'jpeg')
astro_img.show()
