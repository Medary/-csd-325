import json

def print_student_list(student_list):
    for student in student_list:
        if 'last_name' in student and 'first_name' in student and 'id' in student and 'email' in student:
            print(f"{student['last_name']}, {student['first_name']} : ID = {student['id']}, Email = {student['email']}")
        else:
            print("Incomplete student data found.")
            print(student)


def main():
    filename = 'student.json'
    try:
        with open(filename, 'r') as f:
            student_list = json.load(f)
        print("Original Student List:")
        print_student_list(student_list)

        new_student = {
            'last_name': 'Medary',
            'first_name': 'Justin',
            'id': '12345',
            'email': 'jmedary@my365.bellevue.edu'
        }
        student_list.append(new_student)

        print("\nUpdated Student List:")
        print_student_list(student_list)

        with open(filename, 'w') as f:
            json.dump(student_list, f, indent=4)
        print(f"\nSuccessfully updated {filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.  Creating it with initial data.")
        student_list = [
            {'last_name': 'Ripley', 'first_name': 'Ellen', 'id': '45604', 'email': 'eripley@gmail.com'},
            {'last_name': 'Parker', 'first_name': 'John', 'id': '78923', 'email': 'jparker@gmail.com'},
            {'last_name': 'Brett', 'first_name': 'Samuel', 'id': '23487', 'email': 'sbrett@gmail.com'}
        ]
        with open(filename, 'w') as f:
            json.dump(student_list,f, indent=4)
        print(f"Created {filename} with default data.  Please run the program again.")

if __name__ == "__main__":
    main()







