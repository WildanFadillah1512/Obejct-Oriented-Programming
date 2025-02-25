class Student:
    def _init_(self,name,student_id):
        self.name = name
        self.student_id = student_id

    def display_info(self):
        print(f'Student: {self.name}, ID: {self.student_id}')


student1 = Student('budi','12345')
student1.display_info()