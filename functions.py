from PIL import Image
import numpy as np
import colorsys
import cv2

### Transform a color heatmap into a grayscale heatmap

def rgb_to_perceived_color(rgb_values):
    # Normalize RGB values to the range [0, 1]
    normalized_rgb = [x / 255.0 for x in rgb_values]

    # Convert RGB to HSL
    h, l, s = colorsys.rgb_to_hls(*normalized_rgb)

    return h, l, s

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

### Compare two heatmaps
    
def calculate_metrics(Hu, Hs):
    # Normalize Hu to ensure values are between 0 and 1
    Hu = np.clip(Hu, 0, 1)

    intersection = cv2.bitwise_and(Hu, Hs)
    union = cv2.bitwise_or(Hu, Hs)
    
    
    # Calculate coverage (E1)
    coverage = np.sum(intersection) / np.sum(Hu)

    # Calculate outside_gaze (E2)
    outside_gaze = np.sum(Hu - intersection) / np.sum(Hu)

    # Calculate unseen_saliency (E3)
    unseen_saliency = np.sum(Hu - intersection) / np.sum(Hs)

    return coverage, outside_gaze, unseen_saliency
    