import cv2
import os

# Folder to save cropped face images
faces_folder = "registered_faces"
os.makedirs(faces_folder, exist_ok=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("Press 's' to save the detected face and 'q' to quit.")

while True:
  # Read each frame from the webcam
  ret, frame = cap.read()
  
  # Convert to grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  # Detect faces
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
  
  # Draw rectangles around faces
  for(x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
  # Display the video feed with detected faces
  cv2.imshow('Face Detection', frame)
  
  key = cv2.waitKey(1) & 0xFF
  
  # Save the detected face
  if key == ord('s'):
    if len(faces) > 0:
      for idx, (x, y, w, h) in enumerate(faces):
        cropped_face = frame[y:y+h, x:x+w]
        name = input("Enter the for the detected face: ").strip()
        name = "".join(c for c in name if c.isalnum()) # Clean the name to be alphanumeric
        image_filename = f"{name}_{idx + 1}.jpg" # Add index to handle multiple faces
        image_path = os.path.join(faces_folder, image_filename)
        cv2.imwrite(image_path, cropped_face)
        print(f"Face saved for {name}. Image saved as: {image_filename}")
  
  # Quit the program 
  if key == ord('q'):
    break
  
  
  # Release the webcam and close all OpenCV
  cap.release()
  cv2.destroyAllWindows()