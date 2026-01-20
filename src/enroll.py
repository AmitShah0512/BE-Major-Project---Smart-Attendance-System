import cv2              #Imports OpenCV.Used for: Webcam access,Displaying frames,Drawing rectangles.
import face_recognition #Library used for: Detecting faces.Generating face encodings (numerical vectors).
import numpy as np      #Used for numerical array handling. Required by image and encoding operations.
import pickle           #Used to save Python objects to disk. Here: saves student face data (.pkl file).
import os               #Used for: Checking folders.Creating directories.Building file paths.

def enroll_student(student_name, enrollment_id, student_class, save_dir='../data/students', num_images=5):
    """
    Defines a function named enroll_student
    Purpose: Capture face data of one student
    Parameters:
    1)student_name → student’s name
    2)enrollment_id → unique ID
    3)student_class → class name
    4)save_dir → where data will be stored
    5)num_images → number of face samples to capture
    """

    if not os.path.exists(save_dir): #Checks whether the folder to save student data exists.
        os.makedirs(save_dir)        #Creates the folder if it does not exist.

    video_capture = cv2.VideoCapture(0) #Opens the default webcam (0).Used to capture live video frames.
    collected_encodings = []            #Empty list.Will store face encodings (numerical vectors).

    print(f"Enrolling student: {student_name} | Enrollment ID: {enrollment_id} | Class: {student_class}")
    print("Press 'c' to capture a frame when your face is clearly visible.")
    print("Press 'q' to quit early if needed.")

    count = 0 #Counter to track how many face samples are captured.
    while count < num_images: #Loop runs until required number of face samples are collected.
        ret, frame = video_capture.read() #Reads one frame from webcam; frame → image; ret → success flag (True/False).
        if not ret: #Checks if webcam frame capture failed.
            print("Failed to grab frame from webcam. Exiting...")
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) # Resizes the frame to 25% of original size.Purpose: faster face detection.
        rgb_small_frame = small_frame[:, :, ::-1]                 # Converts image from BGR to RGB.Required by face_recognition.
        rgb_small_frame = np.ascontiguousarray(rgb_small_frame)   # Ensures array is stored contiguously in memory.Prevents errors in face encoding.

        face_locations = face_recognition.face_locations(rgb_small_frame) #Detects faces in the current frame.Returns list of face bounding boxes.
        
        if len(face_locations) == 0: #Checks if no face was detected.
        
            #Displays message on webcam window.Red text indicates no face found.
            cv2.putText(frame, "No face detected", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        else: #Executes if at least one face is detected.
            
            #Displays instruction on webcam window.
            cv2.putText(frame, "Face detected! Press 'c' to capture", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            for (top, right, bottom, left) in face_locations: #Iterates over detected face coordinates.
                # Scales coordinates back to original frame size.Because frame was resized earlier.
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2) #Draws a green rectangle around detected face.

        cv2.imshow('Enrollment', frame) #Displays webcam window titled Enrollment.
        key = cv2.waitKey(1) & 0xFF     #Reads keyboard input. Checks if user pressed any key

        if key == ord('c'): #Executes when user presses c
            if face_locations:
                face_encoding = face_recognition.face_encodings(rgb_small_frame, face_locations)[0] #Converts detected face into numerical encoding. [0] → uses first detected face.
                collected_encodings.append(face_encoding) #Stores encoding in list.
                count += 1 #Increments captured image count.
                print(f"Captured image {count}/{num_images}")
            else:
                print("No face detected! Please try again.")
        elif key == ord('q'): #Executes when user presses q.
            print("Enrollment aborted by user.")
            break

    video_capture.release() #Releases webcam.
    cv2.destroyAllWindows() #Closes all OpenCV windows.

    if collected_encodings: #Checks whether any face encodings were captured.

        #Creates a dictionary containing student details and face encodings
        student_data = {
            "name": student_name,
            "enrollment_id": enrollment_id,
            "class": student_class,
            "encodings": collected_encodings
        }

        file_name = f"{enrollment_id}_{student_name.replace(' ', '_')}.pkl" #Creates filename for student data.Replaces spaces with '_'.(Example: enrollmentID_name.pkl)
        file_path = os.path.join(save_dir, file_name) #Builds full file path.
        
        #Saves student data to disk using pickle.
        with open(file_path, "wb") as f:
            pickle.dump(student_data, f)
        
        print(f"Student data saved to {file_path}")

    else: #Executes if no encodings were captured.
        print("No face data captured. Enrollment unsuccessful.")

if __name__ == '__main__': #Checks if file is run directly
    # Takes user input from terminal
    student_name = input("Enter student name: ").strip()
    enrollment_id = input("Enter enrollment ID: ").strip()
    student_class = input("Enter student class: ").strip()
    
    enroll_student(student_name, enrollment_id, student_class) #Calls enrollment function
