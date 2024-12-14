import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# Load the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

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
  
  # Break the loop when 'q' is pressed
  if cv2.waitKey(1) & 0XFF == ord('q'):
    break
  
  # Release the webcam and close all OpenCV
  cap.release()
  cv2.destroyAllWindows()