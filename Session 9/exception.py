# Custom exception classes
class CourseRegistrationError(Exception):
    """Base exception for course registration errors"""
    pass

class CourseNotAvailableError(CourseRegistrationError):
    def __init__(self, course):
        message = f"⚠️ Mata kuliah '{course}' tidak tersedia dalam semester ini."
        super().__init__(message)

class MaxSKSExceededError(CourseRegistrationError):
    def __init__(self, message="⚠️ Jumlah SKS melebihi batas maksimal (24 SKS)."):
        super().__init__(message)

class UnpaidTuitionError(CourseRegistrationError):
    def __init__(self, message="❌ Mahasiswa belum membayar UKT. Silakan bayar UKT terlebih dahulu."):
        super().__init__(message)

class CourseAlreadyRegisteredError(CourseRegistrationError):
    def __init__(self, message="❗ Mata kuliah sudah pernah dipilih sebelumnya."):
        super().__init__(message)

# Simulasi sistem pendaftaran
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
        print(f"✅ Berhasil mendaftar mata kuliah {course.title()} ({sks} SKS). Total SKS: {self.total_sks}")

# Program utama
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

    print("=== SISTEM PENDAFTARAN MATA KULIAH TEKNIK INFORMATIKA ===")
    nama = input("Masukkan nama mahasiswa: ")

    # Validasi input y/n
    while True:
        status_ukt = input("Apakah UKT sudah dibayar? (y/n): ").lower().strip()
        if status_ukt in ('y', 'n'):
            break
        print("⚠️ Masukkan hanya 'y' untuk ya atau 'n' untuk tidak.")

    tuition_paid = status_ukt == 'y'
    mahasiswa = None

    try:
        mahasiswa = Student(name=nama, tuition_paid=tuition_paid)

        if not tuition_paid:
            raise UnpaidTuitionError()

        while True:
            print("\n📚 Daftar mata kuliah tersedia:")
            for course, sks in available_courses.items():
                print(f"- {course.title()} ({sks} SKS)")

            course_input = input("\nMasukkan nama mata kuliah (atau ketik 'selesai' untuk keluar): ").lower().strip()

            if course_input == "selesai":
                break

            try:
                if course_input not in available_courses:
                    raise CourseNotAvailableError(course_input)

                sks = available_courses[course_input]
                mahasiswa.register_course(course_input, sks, available_courses)

                if mahasiswa.total_sks == mahasiswa.max_sks:
                    print("🛑 Batas maksimal SKS telah tercapai.")
                    break

            except CourseRegistrationError as e:
                print(e)

    except CourseRegistrationError as e:
        print(e)
    finally:
        print("\n📌 Pendaftaran selesai.")
        print(f"Mahasiswa: {nama}")
        print("Mata kuliah yang terdaftar:")
        if mahasiswa and mahasiswa.registered_courses:
            for mk in mahasiswa.registered_courses:
                print(f"- {mk.title()}")
        else:
            print("Belum ada mata kuliah yang didaftarkan.")
        if mahasiswa:
            print(f"Total SKS yang diambil: {mahasiswa.total_sks} / {mahasiswa.max_sks}")

if __name__ == "__main__":
    main()
