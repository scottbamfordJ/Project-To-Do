import cv2
import numpy as np
from pathlib import Path

# ============================================
# PROJECT ROOT
# ============================================

ROOT = Path(__file__).resolve().parents[2]

# ============================================
# INPUT / OUTPUT DIRECTORIES
# ============================================

RAW_DIR = ROOT / "agents" / "raw"

ALLY_DIR = ROOT / "script_modified_icons" / "ally"
ENEMY_DIR = ROOT / "script_modified_icons" / "enemy"
PLAYER_DIR = ROOT / "script_modified_icons" / "player"

# Ensure output folders exist
ALLY_DIR.mkdir(parents=True, exist_ok=True)
ENEMY_DIR.mkdir(parents=True, exist_ok=True)
PLAYER_DIR.mkdir(parents=True, exist_ok=True)

# ============================================
# COLOR SETTINGS
# ============================================

LOWER_YELLOW = np.array([20, 120, 120])
UPPER_YELLOW = np.array([40, 255, 255])

ALLY_HUE = 85
ENEMY_HUE = 0

# ============================================
# RECOLOR FUNCTION
# ============================================

def recolor_icon(input_path, output_path, target_hue):

    img = cv2.imread(str(input_path), cv2.IMREAD_UNCHANGED)

    if img is None:
        print(f"Could not load: {input_path}")
        return

    # Preserve alpha
    if img.shape[2] == 4:
        bgr = img[:, :, :3]
        alpha = img[:, :, 3]
    else:
        bgr = img
        alpha = None

    hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

    # Yellow mask
    mask = cv2.inRange(hsv, LOWER_YELLOW, UPPER_YELLOW)

    # Change hue only
    hsv[:, :, 0][mask > 0] = target_hue

    result_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Restore alpha
    if alpha is not None:
        result = np.dstack((result_bgr, alpha))
    else:
        result = result_bgr

    cv2.imwrite(str(output_path), result)

# ============================================
# PROCESS ALL RAW ICONS
# ============================================

supported_extensions = [".png", ".jpg", ".jpeg", ".webp"]

for icon_path in RAW_DIR.iterdir():

    if icon_path.suffix.lower() not in supported_extensions:
        continue

    filename = icon_path.name

    # Ally
    recolor_icon(
        icon_path,
        ALLY_DIR / filename,
        ALLY_HUE
    )

    # Enemy
    recolor_icon(
        icon_path,
        ENEMY_DIR / filename,
        ENEMY_HUE
    )

    # Player/default
    original = cv2.imread(str(icon_path), cv2.IMREAD_UNCHANGED)

    cv2.imwrite(
        str(PLAYER_DIR / filename),
        original
    )

    print(f"Processed: {filename}")

print("\nFinished generating icons.")