# Capture 20 Images Automatically
import cv2
import os

folder = "student_images"
os.makedirs(folder, exist_ok=True)

student_name = input("Enter Student Name: ")

student_folder = os.path.join(folder, student_name)
os.makedirs(student_folder, exist_ok=True)

camera = cv2.VideoCapture(0)

count = 0

while True:
    success, frame = camera.read()

    if not success:
        break

    cv2.imshow("Student Capture", frame)

    key = cv2.waitKey(1)

    if key == ord("c"):
        count += 1

        filename = os.path.join(
            student_folder,
            f"{student_name}_{count}.jpg"
        )

        cv2.imwrite(filename, frame)

        print(f"Captured Image {count}")

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()