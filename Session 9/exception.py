# Custom exception classes
class CourseRegistrationError(Exception):
    """Base exception for course registration errors"""
    pass

class CourseNotAvailableError(CourseRegistrationError):
    def __init__(self, course):
        message = f"⚠️ Course '{course}' is not available this semester."
        super().__init__(message)

class MaxSKSExceededError(CourseRegistrationError):
    def __init__(self, message="⚠️ Total credits exceed the maximum limit (24 credits)."):
        super().__init__(message)

class UnpaidTuitionError(CourseRegistrationError):
    def __init__(self, message="❌ Tuition has not been paid. Please pay the tuition first."):
        super().__init__(message)

class CourseAlreadyRegisteredError(CourseRegistrationError):
    def __init__(self, message="❗ This course has already been registered."):
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
        "algorithms and programming": 3,
        "operating systems": 3,
        "calculus": 4,
        "artificial intelligence": 3,
        "project management": 3,
        "computer networks": 3,
        "web programming": 3,
        "data structures": 3,
        "software engineering": 3,
        "database systems": 3,
        "cybersecurity": 3
    }

    print("=== COMPUTER SCIENCE COURSE REGISTRATION SYSTEM ===")
    name = input("Enter student name: ")

    # Validate y/n input
    while True:
        tuition_status = input("Has the tuition been paid? (y/n): ").lower().strip()
        if tuition_status in ('y', 'n'):
            break
        print("⚠️ Please enter 'y' for yes or 'n' for no.")

    tuition_paid = tuition_status == 'y'
    student = None

    try:
        student = Student(name=name, tuition_paid=tuition_paid)

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
                student.register_course(course_input, sks, available_courses)

                if student.total_sks == student.max_sks:
                    print("🛑 Maximum credit limit reached.")
                    break

            except CourseRegistrationError as e:
                print(e)

    except CourseRegistrationError as e:
        print(e)
    finally:
        print("\n📌 Registration completed.")
        print(f"Student: {name}")
        print("Registered courses:")
        if student and student.registered_courses:
            for course in student.registered_courses:
                print(f"- {course.title()}")
        else:
            print("No courses registered.")
        if student:
            print(f"Total credits taken: {student.total_sks} / {student.max_sks}")

if __name__ == "__main__":
    main()
