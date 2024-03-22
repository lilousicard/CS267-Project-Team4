from PIL import Image

# Define the color mapping
color_map = {
    'a': (0, 0, 255),  # Blue
    'b': (0, 255, 0),  # Green
    'c': (255, 0, 0)   # Red
}

block_size = 8

# Input string
input_string = "abcaac"

# Create an image of the appropriate size
image_width = len(input_string) * block_size
image_height = block_size
image = Image.new('RGB', (image_width, image_height))

# Set the pixels according to the input string
for i, char in enumerate(input_string):
    for x in range(block_size):
        for y in range(block_size):
            pixel_x = i * block_size + x
            pixel_y = y  # Since height is just one block
            image.putpixel((pixel_x, pixel_y), color_map[char])

# Save or display the image
image.save('output.png')
image.show()

