# Custom exception classes
class CourseRegistrationError(Exception):
    """Base exception for course registration errors"""
    pass

class CourseNotAvailableError(CourseRegistrationError):
    def __init__(self, course):
        message = f"⚠️ The course '{course}' is not offered this semester."
        super().__init__(message)

class MaxSKSExceededError(CourseRegistrationError):
    def __init__(self, message="⚠️ The number of credits exceeds the maximum limit (24 credits)."):
        super().__init__(message)

class UnpaidTuitionError(CourseRegistrationError):
    def __init__(self, message="❌ The student has not paid the tuition. Please pay the tuition first."):
        super().__init__(message)

class CourseAlreadyRegisteredError(CourseRegistrationError):
    def __init__(self, message="❗ The course has already been registered."):
        super().__init__(message)

# Course registration simulation
class Student:
    def __init__(self, name, tuition_paid):
        self.name = name
        self.tuition_paid = tuition_paid
        self.registered_courses = []
        self.max_sks = 24
        self.total_sks = 0

    def register_course(self, course, sks, available_courses):
        if not self.tuition_paid:
            raise UnpaidTuitionError()
        if course not in available_courses:
            raise CourseNotAvailableError(course)
        if course in self.registered_courses:
            raise CourseAlreadyRegisteredError()
        if self.total_sks + sks > self.max_sks:
            raise MaxSKSExceededError()

        self.registered_courses.append(course)
        self.total_sks += sks
        print(f"✅ Successfully registered for {course.title()} ({sks} credits). Total credits: {self.total_sks}")

# Main program
def main():
    available_courses = {
        "algoritma dan pemrograman": 3,
        "sistem operasi": 3,
        "kalkulus": 4,
        "kecerdasan buatan": 3,
        "manajemen proyek": 3,
        "jaringan komputer": 3,
        "pemrograman web": 3,
        "struktur data": 3,
        "rekayasa perangkat lunak": 3,
        "basis data": 3,
        "keamanan siber": 3
    }

    print("=== COMPUTER SCIENCE COURSE REGISTRATION SYSTEM ===")
    nama = input("Enter student name: ")

    # Validate y/n input
    while True:
        status_ukt = input("Has the tuition been paid? (y/n): ").lower().strip()
        if status_ukt in ('y', 'n'):
            break
        print("⚠️ Please enter 'y' for yes or 'n' for no.")

    tuition_paid = status_ukt == 'y'
    mahasiswa = None

    try:
        mahasiswa = Student(name=nama, tuition_paid=tuition_paid)

        if not tuition_paid:
            raise UnpaidTuitionError()

        while True:
            print("\n📚 Available courses:")
            for course, sks in available_courses.items():
                print(f"- {course.title()} ({sks} credits)")

            course_input = input("\nEnter course name (or type 'done' to exit): ").lower().strip()

            if course_input == "done":
                break

            try:
                if course_input not in available_courses:
                    raise CourseNotAvailableError(course_input)

                sks = available_courses[course_input]
                mahasiswa.register_course(course_input, sks, available_courses)

                if mahasiswa.total_sks == mahasiswa.max_sks:
                    print("🛑 Maximum credit limit reached.")
                    break

            except CourseRegistrationError as e:
                print(e)

    except CourseRegistrationError as e:
        print(e)
    finally:
        print("\n📌 Registration completed.")
        print(f"Student: {nama}")
        print("Registered courses:")
        if mahasiswa and mahasiswa.registered_courses:
            for mk in mahasiswa.registered_courses:
                print(f"- {mk.title()}")
        else:
            print("No courses have been registered.")
        if mahasiswa:
            print(f"Total credits: {mahasiswa.total_sks} / {mahasiswa.max_sks}")

if __name__ == "__main__":
    main()
