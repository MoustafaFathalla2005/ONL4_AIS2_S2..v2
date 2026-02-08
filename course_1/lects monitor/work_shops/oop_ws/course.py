class Course:
    _id_counter = 1
    
    def __init__(self, name):
        self.course_id = Course._id_counter
        Course._id_counter += 1
        self.name=name
        self.enrolled_student = []
    
    def __repr__(self):
        return f"Course ID : {self.course_id}, Name = {self.name}, Enrolled : {len(self.enrolled_student)} "
    
    def enroll_student(self, student):
        if student not in self.enroll_student:
            self.enroll_student.append(student)
            print ("student enrolled successfully!.")
        else :
            print ("student already enrolled!.")
            
    def remove_student(self, student):
        if student in self.enroll_students:
            self.enrolled_students.remove(student)
            print("student removed successfully.")
        else :
            print("student not found in this course")
        