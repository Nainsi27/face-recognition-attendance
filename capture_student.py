import cv2
import os

# Create folder if it doesn't exist
folder = "student_images"
os.makedirs(folder, exist_ok=True)

student_name = input("Enter Student Name: ")

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        break

    cv2.imshow("Press S to Save Image | Q to Quit", frame)

    key = cv2.waitKey(1)

    # Press S to save
    if key == ord('s'):
        filename = os.path.join(folder, f"{student_name}.jpg")
        cv2.imwrite(filename, frame)
        print("Image Saved:", filename)

    # Press Q to quit
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()