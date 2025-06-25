import cv2
import numpy as np

# Global variable to store polygon points
polygon_points = []
polygon_complete = False


cap = cv2.VideoCapture("tvideo.mp4")

# Mouse callback to collect points
def mouse_callback(event, x, y, flags, param):
    global polygon_points, polygon_complete
    if event == cv2.EVENT_LBUTTONDOWN and not polygon_complete:
        polygon_points.append((x, y))
        print(f"Point Added: (X: {x}, Y: {y})")
    elif event == cv2.EVENT_RBUTTONDOWN:
        polygon_complete = True
        print("Polygon Completed!")

# Read first frame
ret, frame = cap.read()
if not ret:
    print("Failed to read video.")
    cap.release()
    exit()

frame = cv2.resize(frame, (1280, 720))

# Set up window and callback
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',mouse_callback )

while True:
    display_frame = frame.copy()

    # Draw current polygon
    if len(polygon_points) > 1:
        cv2.polylines(display_frame, [np.array(polygon_points)], isClosed=polygon_complete, color=(0, 255, 0), thickness=2)

    # Draw points
    for point in polygon_points:
        cv2.circle(display_frame, point, 5, (0, 0, 255), -1)

    cv2.imshow('Frame', display_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC to exit
        break
    elif key == 13:  # Enter to complete polygon
        polygon_complete = True
        print("Polygon Completed by Enter key!")

cap.release()
cv2.destroyAllWindows()

# Output polygon points
print("\nPolygon Points:")
for i, point in enumerate(polygon_points):
    print(f"Point {i+1}: X = {point[0]}, Y = {point[1]}")
