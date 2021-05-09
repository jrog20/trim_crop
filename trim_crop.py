from simpleimage import SimpleImage

"""
This function returns a new SimpleImage which is a trimmed and
cropped version of the original image by shaving trim_size pixels
from each side (top, left, bottom, right) of the image.
"""

def main():
    image = SimpleImage('images/kitten.jpg')
    trimmed_img = trim_crop_image(image, 30)
    image.show()
    trimmed_img.show()

def trim_crop_image(original_img, trim_size):
    new_width = original_img.width - trim_size * 2
    new_height = original_img.height - trim_size * 2

    new_image = SimpleImage.blank(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):
            original_x = x + trim_size
            original_y = y + trim_size
            original_pixel = original_img.get_pixel(original_x, original_y)
            new_image.set_pixel(x, y, original_pixel)

    return new_image


if __name__ == '__main__':
    main()
