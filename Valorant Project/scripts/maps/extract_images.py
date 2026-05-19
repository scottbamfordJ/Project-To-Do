import cv2
import os
import numpy as np 


INPUT_DIR = r"C:\Users\scott\Documents\Project-To-Do\Valorant Project\maps\raw"
OUTPUT_DIR = r"C:\Users\scott\Documents\Project-To-Do\Valorant Project\maps\mask"
os.makedirs(OUTPUT_DIR, exist_ok=True)


SIZE = 384
RADIUS = SIZE // 2
X_OFFSET = 15  # pixels from left
Y_OFFSET = 35  # pixels from top

# Create circular mask once
circle_mask = np.zeros((SIZE, SIZE), dtype=np.uint8)
cv2.circle(circle_mask, (RADIUS, RADIUS), RADIUS, 255, -1)

for fname in os.listdir(INPUT_DIR):
    if not fname.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    img = cv2.imread(os.path.join(INPUT_DIR, fname), cv2.IMREAD_COLOR)
    
    # Correct offset crop
    crop = img[Y_OFFSET:Y_OFFSET + SIZE, X_OFFSET:X_OFFSET + SIZE]

    # Convert to BGRA to add transparency
    crop = cv2.cvtColor(crop, cv2.COLOR_BGR2BGRA)
    crop[:, :, 3] = circle_mask  # alpha channel

    out_path = os.path.join(OUTPUT_DIR, os.path.splitext(fname)[0] + ".png")
    cv2.imwrite(out_path, crop)