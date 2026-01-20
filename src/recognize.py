import cv2                          #Imports OpenCV - Used for: Webcam access,Drawing rectangles,Showing video window
import face_recognition             #Library for: Detecting faces,Creating face encodings,Comparing faces
import numpy as np                  #Numerical operations. Used for: Array handling,Distance calculations,Image manipulation
import pickle                       #Used to save/load trained data(Not used directly in this file, but common in pipeline)
import os                           #File and directory handling - Used for:Checking folders,Creating folders,File paths
from datetime import datetime       #Used to get: Current date,Current time
import pandas as pd                 #Used for: Creating tables(DataFrames),Writing Excel files
import threading                    #Used to run popup in background.Prevents webcam freezing
import tkinter as tk                #Used only for popup notification
from utils import load_student_data #SHORTNOTE (utils.py) : load_student_data() → Returns student data including: name,enrollment_id,class,face encodings

# Global subject variable. 
SUBJECT = "Data Visualization" #Stores subject name,Written into attendance Excel file,Used as categorical data later.

def show_popup(message="Attendance Marked Successfully", duration=5000): #Defines popup notification function. Used after attendance is marked

    def popup():                   #Inner function. Runs inside a separate thread
        root = tk.Tk()             #Creates a Tkinter window.
        root.title("Notification") #Sets popup window title.
        
        #Centers popup on screen
        window_width = 300
        window_height = 100
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        label = tk.Label(root, text=message, font=("Arial", 12)) #Creates a text label with the message.
        label.pack(expand=True, fill="both")                     #Places the label inside the popup window.
        root.after(duration, root.destroy)                       #Automatically closes popup after given time.
        root.mainloop()                                          #Displays the popup window.
    threading.Thread(target=popup, daemon=True).start()          #Runs popup without blocking webcam


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#ATTENDANCE STORAGE FUNCTION (DATA PIPELINE)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def mark_attendance(student_name, enrollment_id, student_class, subject, attendance_dir='../data'): #Core data storage function. Writes attendance into Excel.
    """
    Mark the attendance of a student in an Excel file.
    The file is named with the current date and subject (e.g. attendance_Machine Learning_YYYY-MM-DD.xlsx)
    and has columns: Enrollment, Name, Class, Subject, Time Stamp.
    
    Args:
        student_name (str): Name of the student.
        enrollment_id (str): Unique enrollment ID.
        student_class (str): The class of the student.
        subject (str): Subject for which attendance is being marked.
        attendance_dir (str): Directory where attendance files are stored.
    """
    if not os.path.exists(attendance_dir):                                                #Checks if attendance folder exists
        os.makedirs(attendance_dir)                                                       #Creates attendance folder if missing
    current_date = datetime.now().strftime('%Y-%m-%d')                                    #Gets today’s date. Format: YYYY-MM-DD
    file_path = os.path.join(attendance_dir, f"attendance_{subject}_{current_date}.xlsx") #Attendance file name. One file per subject per day
    timestamp = datetime.now().strftime('%I:%M:%S %p')                                    #Gets current time(12-hour format).
    
    #Starts creating a new attendance record.
    new_row = { 
        #Attendance data values.
        'Enrollment': enrollment_id,
        'Name': student_name,
        'Class': student_class,
        'Subject': subject,
        'Time Stamp': timestamp
    }  

    if os.path.exists(file_path): #Checks if today’s attendance file already exists.
        try:
            df = pd.read_excel(file_path) #Loads existing attendance data.
        except Exception as e:
            print("Error reading the existing attendance file:", e)
            df = pd.DataFrame(columns=['Enrollment', 'Name', 'Class', 'Subject', 'Time Stamp'])
    else: #If file does not exist
        df = pd.DataFrame(columns=['Enrollment', 'Name', 'Class', 'Subject', 'Time Stamp']) #Creates empty attendance table.
    
    if enrollment_id in df['Enrollment'].values: #Prevents duplicate attendance. Checks if student already marked today. 
        print(f"Attendance already marked for {student_name}.")
    else:
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True) #Adds new attendance row to table
        df.to_excel(file_path, index=False)                              #Saves attendance table to Excel file.
        print(f"Attendance marked for {student_name} at {timestamp} for subject: {subject}")
        show_popup() # Display popup message


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#FACE RECOGNITION FUNCTION (CORE LOGIC)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def recognize_students(video_source=0, subject="Data Visualization"): #Main function.Runs webcam face recognition
    """ 
    Recognize students from the video feed and mark their attendance.
    If a face is not recognized, a red rectangle is drawn and "Unknown" is displayed.
    
    Args:
        video_source (int or str): Video source (default is 0 for webcam).
        subject (str): The subject name to use when marking attendance.
    """
    student_data = load_student_data() #SHORTNOTE (utils.py): Returns a Returns list of students:name,enrollment_id,class,face encodings.
    
    known_encodings = [] # To store numerical face features - Face encodings (numbers)
    student_info = []    # To store metadata (name, id, class)
    
    # Prepare known encodings and student info (including class): Flattens all face encodings, Aligns each encoding with student details
    for data in student_data:
        known_encodings.extend(data['encodings'])
        student_info.extend([
            {
                'name': data['name'],
                'enrollment_id': data['enrollment_id'],
                'class': data.get('class', 'N/A')
            }
        ] * len(data['encodings']))

    video_capture = cv2.VideoCapture(video_source) #Starts webcam
    recognized_students = set()                    #Stores already marked students. Prevents duplicate attendance in same session.
    print("Starting video stream for subject:", subject, ". Press 'q' to quit.")
    
    while True: #Infinite loop (live video)
       
        #Reads frame.Stops if webcam fails
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame from webcam. Exiting...")
            break
        
        #----------------------------------------------------------------------------------------------------------------------------------------------------------
        #OpenCV (cv2) loads images by default in BGR (Blue, Green, Red) format. This is a legacy convention from its original development.
        #Most other ML and image display libraries, such as Matplotlib, TensorFlow, and Pillow (PIL), expect images to be in RGB (Red, Green, Blue) format. 
        #----------------------------------------------------------------------------------------------------------------------------------------------------------
        # Downscales frame for faster processing and convert from BGR to RGB.
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        rgb_small_frame = np.ascontiguousarray(rgb_small_frame)

        # Detect faces and compute encodings.
        face_locations = face_recognition.face_locations(rgb_small_frame)                 #Detects faces
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) #Converts faces → numerical vectors

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            #Compares input face with known faces.Finds closest match.
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]: #Checks if match is valid
                
                #Extracts student details
                student = student_info[best_match_index]
                name = student['name']
                enrollment_id = student['enrollment_id']
                student_class = student.get('class', 'N/A')
                
                #Marks attendance once per session
                if enrollment_id not in recognized_students:
                    mark_attendance(name, enrollment_id, student_class, subject)
                    recognized_students.add(enrollment_id)
                rect_color = (0, 255, 0)  # Green for recognized
            else:
                name = "Unknown"
                rect_color = (0, 0, 255)  # Red for unknown

            # Scale back up face location coordinates.
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw rectangle and label on the frame.
            cv2.rectangle(frame, (left, top), (right, bottom), rect_color, 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, rect_color, 2)

        #Shows video.Exits on q
        cv2.imshow('Attendance Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #Releases resources
    video_capture.release()
    cv2.destroyAllWindows()

#Script entry point
if __name__ == '__main__':
    recognize_students()
