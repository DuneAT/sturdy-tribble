from PIL import Image
import numpy as np

import colorsys

def rgb_to_perceived_color(rgb_values):
    # Normalize RGB values to the range [0, 1]
    normalized_rgb = [x / 255.0 for x in rgb_values]

    # Convert RGB to HSL
    h, l, s = colorsys.rgb_to_hls(*normalized_rgb)

    return h, l, s

# Example usage:
rgb_values = [255, 255, 0]  # Replace with the RGB values of your pixel
perceived_color = rgb_to_perceived_color(rgb_values)

print("Perceived Color (H, L, S):", perceived_color)

def heatmap_to_grayscale(input_path, output_path):
    # Load the image and convert it to grayscale
    image = Image.open(input_path)
    image_array = np.array(image)
    new_image_array = np.empty(image_array.shape)
    for i in range(len(image_array)):
        for j in range(len(image_array[i])):
            h, l, s = rgb_to_perceived_color(image_array[i][j])
            if h < 0.041666666666667 or h >= 0.9:
                a = 1
            elif h >= 0.041666666666667 and h < 0.125:
                a = 0.75
            elif h >= 0.125 and h < 0.208:
                a = 0.5
            elif h >= 0.208 and h < 0.458:
                a = 0.25
            elif h >= 0.458 and h < 0.9:
                a = 0.1
            if l > 0.98 :
                a = 0

            alpha = int(a*255)
            new_image_array[i][j] = [alpha,alpha,alpha]



    new_image_array_uint8 = new_image_array.astype(np.uint8)

    new_image = Image.fromarray(new_image_array_uint8, "RGB")
    new_image.save(output_path)

# Example usage:
input_path = "C:/Users/dunea/Documents/Projet_Julia/extracted_heatmap.png"
output_path = "C:/Users/dunea/Documents/Projet_Julia/output_grey_scale.png"
heatmap_to_grayscale(input_path, output_path)
