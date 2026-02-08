class Student :
    _id_counter = 1 #local variable (can make it global)
    
    
    def __init__(self, name):
        self.student_id = Student._id_counter #to access local variable
        Student._id_counter += 1
        self.name = name
        self.grades = {}
        self.enrolled_courses = []
        
    def __str__(self): 
        return f"Student ID : {self.student_id}, Name : {self.name}, Grades : {self.grades} "
      
    def __repr__(self):  # see rapr and str
        return f"Student ID : {self.student_id}, Name : {self.name}, Grades : {self.grades} "
    
    def add_garde(self, course_id, grade):
        self.grades[course_id] = grade

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course) 