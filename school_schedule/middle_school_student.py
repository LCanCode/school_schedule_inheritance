from .student import Student

# add MiddleSchoolStudent here

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
    
    def summary(self):
        student_summary = super().summary()
        transportation_status = self.gets_transportation
        return f"{student_summary}. {self.student} gets transportation: {transportation_status}"
        



# Update the summary method to include information about the student's transportation status
# Include tests for the additional functionality
# There is one test provided (currently commented out)
# Uncomment the test and implement the MiddleSchoolStudent class so that it passes
# If there is time, implement additional tests for the MiddleSchoolStudent class (review the HighSchoolStudent class for ideas)
