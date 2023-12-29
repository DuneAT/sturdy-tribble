import numpy as np
from PIL import Image
import cv2

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
    


# Example usage:
# Assuming Hu and Hs are 2D numpy arrays representing heatmaps

input_user_path = "C:/Users/dunea/Documents/Projet_Julia/output_grey_scale.png"
input_system_path = "C:/Users/dunea/Documents/Projet_Julia/saliency.png"
input_system_path = "C:/Users/dunea/Documents/Projet_Julia/output_grey_scale.png"

Hu = np.array(Image.open(input_user_path))
Hs = np.array(Image.open(input_system_path))

# Hu and Hs with continuous values between 0 and 1
Hu = Hu / 255
Hs = Hs / 255

# Call the function
E1, E2, E3 = calculate_metrics(Hu, Hs)

# Print or use the results
print("E1, How much the gaze is within a predicted salient region : ", E1)
print("E2, How much the gaze is outside all predicted salient region : ", E2)
print("E3, How much salient region is not seen by the gaze : ", E3)
