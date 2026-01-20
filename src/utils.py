import os # Used for: Checking folders,Listing files,Creating directories,Handling file paths.
import pickle # Used to: Load saved .pkl files,Convert stored binary data back into Python objects.

def load_student_data(directory='../data/students'):
    """
    Load all student data from the specified directory.

    Args:
        directory (str): Path to the directory containing student .pkl files.

    Returns:
        list: A list of dictionaries with student information and encodings.
    """
    student_data = [] #Creates an empty list.This list will eventually store ALL students’ data.
    
    
    if not os.path.exists(directory):  # os.path.exists(directory) -> Checks whether ../data/students folder exists or not. 
        os.makedirs(directory)  # If it does NOT exist: os.makedirs(directory) creates it.

    for filename in os.listdir(directory): # os.listdir(directory) → Returns all file names inside ../data/students.
        if filename.endswith('.pkl'): # Ensures we only open student data files
            
            file_path = os.path.join(directory, filename) # Build Full File Path.Combines folder + file name.Required because pickle.load() needs full path

            with open(file_path, 'rb') as file:
                '''
                Opens file safely
                1)'rb' means: read
                2)binary mode (required for pickle)

                📌 with ensures:
                1)File automatically closes after reading
                2)No memory leaks
                '''
                data = pickle.load(file) #Reads the '.pkl' file.Converts stored binary data back into Python dictionary.
                student_data.append(data) #Adds one student’s dictionary to student_data list.
    return student_data #Sends the complete list back to caller.
    '''
    Used in recognize.py like this:
    student_data = load_student_data()
    
    📌 After this:
    1)Face recognition has known faces
    2)Attendance marking becomes possible
    '''