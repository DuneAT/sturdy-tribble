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

# Include the time by considering T successive images

T = 3

urls_u = ["C:/Users/dunea/Documents/Projet_Julia/0101/extracted_heatmap.png", "C:/Users/dunea/Documents/Projet_Julia/0102/extracted_heatmap.png", "C:/Users/dunea/Documents/Projet_Julia/0103/extracted_heatmap.png"]
urls_s = ["C:/Users/dunea/Documents/Projet_Julia/0101/saliency.png", "C:/Users/dunea/Documents/Projet_Julia/0101/saliency.png", "C:/Users/dunea/Documents/Projet_Julia/0101/saliency.png"]

Hu_List = []
Hs_List = []
for i in range(T):
    Hu_List.append(np.array(Image.open(urls_u[i])))
    Hs_List.append(np.array(Image.open(urls_s[i])))

Hu_total = np.zeros(Hu_List[0].shape)
Hs_total = np.zeros(Hs_List[0].shape)

for i in range(T):
    Hu_total += Hu_List[i]
    Hs_total += Hs_List[i]

Hu_total = Hu_total / T
Hs_total = Hs_total / T

# Call the function
E1, E2, E3 = calculate_metrics(Hu_total, Hs_total)

# Print or use the results
print("E1, How much the gaze is within a predicted salient region : ", E1)
print("E2, How much the gaze is outside all predicted salient region : ", E2)
print("E3, How much salient region is not seen by the gaze : ", E3)