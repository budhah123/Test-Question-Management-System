import random
import os

class AcademicAdminSystem:
    def __init__(self):
        self.admin_username = "admin@123"
        self.admin_password = "Admin456"
        self.attempts = 0
        self.lecturers = self.load_data('lecturer.txt')
        self.subjects = self.load_subjects('subject.txt')
        self.exam_personnel = self.load_data_personnel('personnel.txt')

    def load_data(self, filename):
        data = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    username, info = line.strip().split(':', 1)
                    data[username] = eval(info)
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"An error occurred while loading data from {filename}: {e}")
        return data

    def save_data(self, filename, data):
        try:
            with open(filename, 'w') as file:
                for username, info in data.items():
                    file.write(f"{username}:{info}\n")
        except Exception as e:
            print(f"An error occurred while saving data to {filename}: {e}")

    def save_data_personnel(self, filename, data):
        try:
            with open(filename, 'w') as file:
                for username, details in data.items():
                    password = details['Password']
                    email = details['Email']
                    file.write(f"{username}:{password}:{email}\n")
            print(f"Data saved successfully in {filename}.")
        except Exception as e:
            print(f"An error occurred while saving data to {filename}: {e}")

    def load_data_personnel(self, filename):
        data = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    username, rest = line.strip().split(':', 1)
                    password, email = rest.split(',')
                    data[username] = {
                        'Password':password,
                        'Email':email,
                    }
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"An error occurred while loading data from {filename}: {e}")
        return data

    def load_subjects(self, filename):
        subjects = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    subject, topics = line.strip().split(':', 1)
                    subjects[subject] = topics.split(',')
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"An error occurred while loading subjects from {filename}: {e}")
        return subjects

    def save_subjects(self, filename, subjects):
        try:
            with open(filename, 'w') as file:
                for subject, topics in subjects.items():
                    file.write(f"{subject}:{','.join(topics)}\n")
        except Exception as e:
            print(f"An error occurred while saving subjects to {filename}: {e}")

    def username_validate(self, username):
        if not any(char.isdigit() for char in username):
            return "Username must contain at least one number"
        elif "@" not in username:
            return "Username must contain @ symbol"
        else:
            return "valid"

    def password_validate(self, password):
        if len(password) < 8:
            return "Password must contain at least 8 characters"
        elif not any(char.isupper() for char in password):
            return "Password must contain at least one uppercase letter"
        elif not any(char.isdigit() for char in password):
            return "Password must contain at least one number"
        else:
            return "valid"

    def valid_date_of_birth(self, dob):
        try:
            month, day, year = map(int, dob.split('/'))
            if 1 <= month <= 12 and 1 <= day <= 31 and 1900 <= year <= 2024:
                return True
            else:
                return "Invalid date. Ensure the format is MM/DD/YYYY, the month is 1-12, the day is 1-31, and the year is not more than 2024."
        except ValueError:
            return "Invalid date format. Please use MM/DD/YYYY."

    def email_validate(self, email):
        if "@" in email and email.endswith("@gmail.com"):
            return "valid"
        return "Email must be a valid Gmail address"

    def admin_Login(self):
        while self.attempts < 3:
            print("*******Admin Login********")
            try:
                username_attempts = 0
                while username_attempts < 3:
                    username = input("Enter the Username: ")
                    username_validation = self.username_validate(username)
                    if username_validation != "valid":
                        print(username_validation)
                        username_attempts += 1
                        if username_attempts >= 3:
                            print("Too many attempts for username. Terminating the app.")
                            return False
                        continue
                    else:
                        break

                password_attempts = 0
                while password_attempts < 3:
                    password = input("Enter the password: ")
                    password_validation = self.password_validate(password)
                    if password_validation != "valid":
                        print(password_validation)
                        password_attempts += 1
                        if password_attempts >= 3:
                            print("Too many attempts for password. Terminating the app.")
                            return False
                        continue
                    else:
                        break

                if username == self.admin_username and password == self.admin_password:
                    print("Login successful")
                    self.attempts = 0  
                    self.admin_pannel()
                    break
                else:
                    self.attempts += 1
                    print(f"Incorrect credentials! Attempts Left: {3 - self.attempts}")

            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                if self.attempts >= 3:
                    print("Too many attempts. Terminating the app.")
                    return False

    def assign_new_lecturer(self):
        print("***Assign new lecturer***")
        while True:
            try:
                username = input("Enter the lecturer's username: ")
                username_validation = self.username_validate(username)
                if username_validation != "valid":
                    print(username_validation)
                    continue

                password = input("Enter the lecturer's password: ")
                password_validation = self.password_validate(password)
                if password_validation != "valid":
                    print(password_validation)
                    continue

                name = input("Enter the lecturer's name: ")
                address = input("Enter the lecturer's address: ")
                age = int(input("Enter the lecturer's age: "))

                while True:
                    country_code = '+977 '
                    contact_number = input(f"Enter the contact number: {country_code}")
                    if len(contact_number) == 10:
                        break
                    else:
                        print("Contact number must be 10 digits")
                        continue

                while True:
                    dob = input("Enter the lecturer's date of Birth (MM/DD/YYYY): ")
                    if self.valid_date_of_birth(dob) == True:
                        break
                    else:
                        print(self.valid_date_of_birth(dob))
                        continue

                while True:
                    email = input("Enter your Email address: ")
                    email_validation = self.email_validate(email)
                    if email_validation != 'valid':
                        print(email_validation)
                        continue
                    else:
                        break

                citizenship_Id = input("Enter Your Citizenship Id: ")

                self.lecturers[username] = {
                    "Password": password,
                    "profile": {
                        "Name": name,
                        "Address": address,
                        "Contact number": contact_number,
                        "Date of Birth": dob,
                        "Email Address": email,
                        "Age": age,
                        "Citizenship Id": citizenship_Id
                    }
                }
                self.save_data('lecturer.txt', self.lecturers)
                print(f"Lecturer assigned with username {username}")

                choice = input("Do you want to assign another new lecturer (Y/N): ")
                if choice.lower() == 'y':
                    continue
                break

            except Exception as e:
                print(f"An error occurred: {e}")

    def assign_personnel(self):
        print("*****Assign exam unit personnel*********")
        while True:
            try:
                username = input("Enter the personnel's username: ")
                password = input("Enter the personnel's password: ")
                username_validation = self.username_validate(username)
                if username_validation != "valid":
                    print(username_validation)
                    continue
                password_validation = self.password_validate(password)
                if password_validation != "valid":
                    print(password_validation)
                    continue

                while True:
                    email = input("Enter your Email address: ")
                    email_validation = self.email_validate(email)
                    if email_validation != 'valid':
                        print(email_validation)
                        continue
                    else:
                        break

                self.exam_personnel[username] = {
                    "Password": password,
                    "Email": email,
                }
                self.save_data_personnel('personnel.txt', self.exam_personnel)
                print(f"Exam unit personnel assigned with username {username}")
                break

            except Exception as e:
                print(f"An error occurred: {e}")

    def admin_pannel(self):
        while True:
            try:
                print("***************Welcome to the Admin Pannel*******")
                print("1. Assign a new lecturer")
                print("2. Assign a new exam unit personnel")
                print("3. Modify lecturer profile")
                print("4. Display the lecturer profile")
                print("5. Add topics and subjects")
                print("6. Delete the existing lecturer information")
                print("7. Delete the existing exam personnel")
                print("8. Exit")
                while True:
                    try:
                        ch = int(input("Enter your choice: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                if ch == 1:
                    self.assign_new_lecturer()
                elif ch == 2:
                    self.assign_personnel()
                elif ch == 3:
                    self.modify_lecturer_profile()
                elif ch == 4:
                    self.display_lecturer_profile()
                elif ch == 5:
                    self.add_subjects_and_topics()
                elif ch == 6:
                    self.delete_lecturer()
                elif ch == 7:
                    self.delete_exam_personnel()
                elif ch == 8:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

    # Placeholder methods for additional functionalities
    def modify_lecturer_profile(self):
        while True:
            print("********Modify lecturer Profile*******")
            try:
                username = input("Enter the lecturer's username to modify: ")
                if username in self.lecturers:
                    while True:
                        print("Which field do you want to modify?")
                        print("1. Name")
                        print("2. Address")
                        print("3. Contact number")
                        print("4. Date of birth")
                        print("5. Age")
                        print("6. Email address")
                        print("7. Citizenship ID")
                        print("8. Exit")
                        while True:
                            try:
                                choice = int(input("Enter your choice: "))
                                break
                            except ValueError:
                                print("Invalid input. Please enter a number.")

                        if choice == 1:
                            new_name = input("Enter your new name: ")
                            self.lecturers[username]["profile"]["Name"] = new_name
                            self.save_data('lecturer.txt', self.lecturers)
                            print("Name updated successfully")
                        elif choice == 2:
                            new_address = input("Enter the new address: ")
                            self.lecturers[username]["profile"]["Address"] = new_address
                            self.save_data('lecturer.txt', self.lecturers)
                            print("Address updated successfully")
                        elif choice == 3:
                            while True:
                                country_code = '+977 '
                                new_contact_number = input(f"Enter the new contact number: {country_code}")
                                if len(new_contact_number) == 10:
                                    self.lecturers[username]["profile"]["Contact number"] = new_contact_number
                                    self.save_data('lecturer.txt', self.lecturers)
                                    print("Contact number updated successfully")
                                    break
                                else:
                                    print("Contact number must be 10 digits")
                                    continue
                        elif choice == 4:
                            while True:
                                new_dob = input("Enter the lecturer's date of Birth (MM/DD/YYYY): ")
                                if self.valid_date_of_birth(new_dob) == True:
                                    self.lecturers[username]["profile"]["Date of Birth"] = new_dob
                                    self.save_data('lecturer.txt', self.lecturers)
                                    print("Date of birth updated successfully")
                                    break
                                else:
                                    print(self.valid_date_of_birth(new_dob))
                                    continue
                        elif choice == 5:
                            new_age = int(input("Enter the new lecturer's age: "))
                            self.lecturers[username]["profile"]["Age"] = new_age
                            self.save_data('lecturer.txt', self.lecturers)
                            print("Age updated successfully")
                        elif choice == 6:
                            while True:
                                new_email = input("Enter your new Email address: ")
                                email_validation = self.email_validate(new_email)
                                if email_validation != 'valid':
                                    print("Email format can't be matched! Please try again")
                                    continue
                                else:
                                    self.lecturers[username]["profile"]["Email Address"] = new_email
                                    self.save_data('lecturer.txt', self.lecturers)
                                    print("Email address updated successfully")
                                    break
                        elif choice == 7:
                            new_citizenship = input("Enter your new citizenship ID: ")
                            self.lecturers[username]["profile"]["Citizenship Id"] = new_citizenship
                            self.save_data('lecturer.txt', self.lecturers)
                            print("Citizenship ID updated successfully")
                        elif choice == 8:
                            self.admin_pannel()
                            print("Exiting modification.")
                            break
                        else:
                            print("Invalid choice! Please try again.")
                else:
                    print("Lecturer's username not found. Please try again.")
                
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def display_lecturer_profile(self):
        try:
            username = input("Enter the lecturer's username to display: ")
            if username in self.lecturers:
                print(f"Profile details of lecturer with username '{username}':")
                profile = self.lecturers[username]["profile"]
                for key, value in profile.items():
                    print(f"{key}: {value}")
            else:
                print(f"Lecturer with username '{username}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_subjects_and_topics(self):
        print("****** Add subjects and topics ******")
        while True:
            try:
                subject = input("Enter the subject name: ")
                if subject in self.subjects:
                    print("Subject already exists.")
                else:
                    topics = input("Enter the topics separated by commas: ").split(',')
                    self.subjects[subject] = topics
                    self.save_subjects('subject.txt', self.subjects)
                    print(f"Subject '{subject}' with topics added successfully.")
                choice = input("Do you want to add another subject and topics (Y/N)? ")
                if choice.lower() == 'n':
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

    def delete_lecturer(self):
        print("*** Delete Existing Lecturer ***")
        try:
            username = input("Enter the lecturer's username to delete: ")
            if username in self.lecturers:
                del self.lecturers[username]
                self.save_data('lecturer.txt', self.lecturers)
                print(f"Lecturer with username '{username}' deleted successfully.")
            else:
                print(f"Lecturer with username '{username}' not found.")

            print("***** All Lecturers *****")
            for username, info in self.lecturers.items():
                print(f"Username: {username}")
                for key, value in info["profile"].items():
                    print(f"{key}: {value}")
                print()
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_exam_personnel(self):
        print("*** Delete Existing Exam Personnel ***")
        try:
            username = input("Enter the personnel's username to delete: ")
            if username in self.exam_personnel:
                del self.exam_personnel[username]
                self.save_data('personnel.txt', self.exam_personnel)
                print(f"Exam personnel with username '{username}' deleted successfully.")
            else:
                print(f"Exam personnel with username '{username}' not found.")

            print("***** All Exam Personnel *****")
            for username, info in self.exam_personnel.items():
                print(f"Username: {username}")
                for key, value in info["profile"].items():
                    print(f"{key}: {value}")
                print()
        except Exception as e:
            print(f"An error occurred: {e}")

class RegisteredLecturer:
    def __init__(self):
        self.credentials = self.load_data('lecturer.txt')
        self.questions = self.load_questions('questions.txt')
        self.attempts = 0

    def load_data(self, filename):
        data = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    username, info = line.strip().split(':', 1)
                    data[username] = eval(info)
        except FileNotFoundError:
            print(f"{filename} not found.")
        except Exception as e:
            print(f"An error occurred while loading data from {filename}: {e}")
        return data

    def save_data(self, filename, data):
        try:
            with open(filename, 'w') as file:
                for username, info in data.items():
                    file.write(f"{username}:{info}\n")
        except Exception as e:
            print(f"An error occurred while saving data to {filename}: {e}")

    def load_questions(self, filename):
        questions = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    subject, topic, question, answer = line.strip().split(':', 3)
                    if subject not in questions:
                        questions[subject] = {}
                    if topic not in questions[subject]:
                        questions[subject][topic] = []
                    questions[subject][topic].append({"question": question, "answer": answer})
        except FileNotFoundError:
            print(f"{filename} not found.")
        except Exception as e:
            print(f"An error occurred while loading questions from {filename}: {e}")
        return questions

    def save_questions(self, filename, questions):
        try:
            with open(filename, 'w') as file:
                for subject, topics in questions.items():
                    for topic, qas in topics.items():
                        for qa in qas:
                            file.write(f"{subject}:{topic}:{qa['question']}:{qa['answer']}\n")
        except Exception as e:
            print(f"An error occurred while saving questions to {filename}: {e}")

    def login(self):
        while self.attempts < 3:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username in self.credentials and self.credentials[username]['Password'] == password:
                print("Login successful!")
                self.lecturer_panel(username)
                return True
            else:
                self.attempts += 1
                print(f"Invalid credentials. Attempts left: {3 - self.attempts}")

        

    def change_credentials(self, username):
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")

        self.credentials[new_username] = self.credentials.pop(username)
        self.credentials[new_username]['Password'] = new_password
        self.save_data('lecturer.txt', self.credentials)
        print("Username and password changed successfully!")

    def add_question(self):
        subject = input("Enter the subject: ")
        topic = input("Enter the topic: ")
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")

        if subject not in self.questions:
            self.questions[subject] = {}
        if topic not in self.questions[subject]:
            self.questions[subject][topic] = []

        self.questions[subject][topic].append({"question": question, "answer": answer})
        self.save_questions('questions.txt', self.questions)
        print("Question added successfully!")

    def modify_question(self):
        subject = input("Enter the subject: ")
        topic = input("Enter the topic: ")

        if subject in self.questions and topic in self.questions[subject]:
            for idx, qa in enumerate(self.questions[subject][topic]):
                print(f"{idx + 1}. {qa['question']} - {qa['answer']}")

            q_num = int(input("Enter the number of the question to modify: ")) - 1
            if 0 <= q_num < len(self.questions[subject][topic]):
                new_question = input("Enter the new question: ")
                new_answer = input("Enter the new answer: ")
                self.questions[subject][topic][q_num] = {"question": new_question, "answer": new_answer}
                self.save_questions('questions.txt', self.questions)
                print("Question modified successfully!")
            else:
                print("Invalid question number.")
        else:
            print("Subject or topic not found.")

    def view_questions(self):
        subject = input("Enter the subject: ")
        topic = input("Enter the topic: ")

        if subject in self.questions and topic in self.questions[subject]:
            for qa in self.questions[subject][topic]:
                print(f"Q: {qa['question']}\nA: {qa['answer']}\n")
        else:
            print("Subject or topic not found.")

    def lecturer_panel(self, username):
        while True:
            print("\n1. Change username and password")
            print("2. Add new questions and answers")
            print("3. Modify questions and answers")
            print("4. View questions and answers")
            print("5. Logout")

            while True:
                try:
                    choice = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if choice == 1:
                self.change_credentials(username)
            elif choice == 2:
                self.add_question()
            elif choice == 3:
                self.modify_question()
            elif choice == 4:
                self.view_questions()
            elif choice == 5:
                print("Logging out...")
                return 
            else:
                print("Invalid choice. Please try again.")



class ExamUnitPersonnel:
    def __init__(self):
        self.credentials = {}
        self.exam_papers = {"Set 1": {"Section A": [], "Section B": []}, "Set 2": {"Section A": [], "Section B": []}}

    def read_credentials(self, filename='personnel.txt'):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    parts = line.split(':')
                    if len(parts) == 2:
                        username, password = parts
                        self.credentials[username] = password
                    else:
                        print(f"Skipping invalid line in {filename}: {line}")
        except FileNotFoundError:
            print("Credentials file not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
        return self.credentials


    def personnel_panel(self):
        while True:
            try:
                print("***************Welcome to the exam unit personnel panel*******")
                print("\n1. Change username and password")
                print("2. Create exam papers")
                print("3. View exam papers")
                print("4. Modify exam papers")
                print("5. Exit")
                while True:
                    try:
                        ch = int(input("Enter your choice: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                if ch == 1:
                    self.change_credentials()
                elif ch == 2:
                    self.create_exam_papers()
                elif ch == 3:
                    self.view_exam_papers()
                elif ch == 4:
                    self.modify_exam_papers()
                elif ch == 5:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def login(self):
        attempts = 0
        while attempts < 3:
            self.credentials = self.read_credentials()

            input_username = input("Enter username: ")
            input_password = input("Enter password: ")

            if input_username in self.credentials:
                stored_password = self.credentials[input_username]

                if input_password == stored_password:
                    print("Login successful!")
                    self.personnel_panel()
                    return True
                else:
                    print("Invalid password.")
            else:
                print("Invalid username.")

            attempts += 1
            print(f"Incorrect credentials. You have {3 - attempts} attempts left.")

        print("Maximum attempts reached. Access denied.")
        return False

    def change_credentials(self):
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        self.credentials[new_username] = new_password
        with open('personnel.txt', 'w+') as file:
            for username, password in self.credentials.items():
                file.write(f"{username}:{password}\n")
        print("Username and password changed successfully!")

    def create_mcq(self):
        while True:
            question = input("Enter the question: ")
            options = []
            for i in range(4):
                option = input(f"Enter option {chr(97 + i)}: ")
                options.append(option)
            correct_option = input("Enter the correct option (a, b, c, d): ")
            ch = input("Do you want to add another question (y/n)?:")
            if ch.lower() == 'y':
                continue
            return {
                "question": question,
                "options": options,
                "correct_option": correct_option
            }

    def create_subjective(self):
        while True:
            print("Please enter the new subjective question:")
            question = input("Question: ")
            ch = input("Do you want to add another question (y/n)?:")
            if ch.lower() == 'y':
                continue
            return question

    def create_exam_papers(self):
        set1 = {"Section A": [], "Section B": []}
        set2 = {"Section A": [], "Section B": []}

        print("Create questions for Set 1, Section A (MCQs):")
        while True:
            mcq = self.create_mcq()
            set1["Section A"].append(mcq)
            ch = input("Do you want to add another question (y/n)?:")
            if ch.lower() == 'y':
                continue
            else:
                break

        print("Create questions for Set 1, Section B (Subjective):")
        while True:
            subjective = self.create_subjective()
            set1["Section B"].append(subjective)
            select = input("Do you want to add another question (y/n)?:")
            if select.lower() == 'y':
                continue
            else:
                break

        print("Create questions for Set 2, Section A (MCQs):")
        while True:
            mcq = self.create_mcq()
            set2["Section A"].append(mcq)
            select1 = input("Do you want to add another question (y/n)?:")
            if select1.lower() == 'y':
                continue
            else:
                break

        print("Create questions for Set 2, Section B (Subjective):")
        while True:
            subjective = self.create_subjective()
            set2["Section B"].append(subjective)
            choice = input("Do you want to add another question (y/n)?:")
            if choice.lower() == 'y':
                continue
            else:
                break

        self.exam_papers["Set 1"] = set1
        self.exam_papers["Set 2"] = set2

        self.save_exam_papers()
        print("Exam papers created and saved successfully!")

    def save_exam_papers(self):
        with open("papers.txt", "w") as file:
            for set_name, sections in self.exam_papers.items():
                for section_name, questions in sections.items():
                    file.write(f"{set_name} - {section_name}\n")
                    for q in questions:
                        if isinstance(q, dict):  # MCQ
                            file.write(f"Q: {q['question']}\n")
                            for i in range(len(q["options"])):
                                file.write(f"   {chr(97 + i)}) {q['options'][i]}\n")
                            file.write(f"Correct option: {q['correct_option']}\n\n")
                        else:  # Subjective
                            file.write(f"Q: {q}\n\n")

    def read_exam_papers(self):
        try:
            with open("papers.txt", "r") as file:
                current_set = None
                current_section = None
                for line in file:
                    line = line.strip()
                    if "Set" in line and "Section" in line:
                        parts = line.split(" - ")
                        current_set = parts[0]
                        current_section = parts[1]
                    elif line.startswith("Q:"):
                        question = line[3:]
                        if current_section == "Section A":
                            options = []
                            for _ in range(4):
                                option_line = file.readline().strip()
                                options.append(option_line[4:])
                            correct_option = file.readline().strip().split(": ")[1]
                            self.exam_papers[current_set][current_section].append({
                                "question": question,
                                "options": options,
                                "correct_option": correct_option
                            })
                        else:
                            self.exam_papers[current_set][current_section].append(question)
                    file.readline()  # Skip empty line
        except FileNotFoundError:
            print("Exam papers file not found.")

    def view_exam_papers(self):
        try:
            with open("papers.txt", "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("Exam papers file not found.")

    def modify_exam_papers(self):
        self.read_exam_papers()

        print("\nWhich set do you want to modify?")
        print("1. Set 1")
        print("2. Set 2")
        set_choice = input("Enter your choice: ")
        if set_choice == '1':
            current_set = self.exam_papers["Set 1"]
        elif set_choice == '2':
            current_set = self.exam_papers["Set 2"]
        else:
            print("Invalid choice.")
            return

        print("\nWhich section do you want to modify?")
        print("1. Section A (MCQs)")
        print("2. Section B (Subjective)")
        section_choice = input("Enter your choice: ")
        if section_choice == '1':
            section = "Section A"
        elif section_choice == '2':
            section = "Section B"
        else:
            print("Invalid choice.")
            return

        print(f"\nCurrent questions in {section}:")
        question_list = current_set[section]
        for i in range(len(question_list)):
            if section == "Section A":
                mcq = question_list[i]
                print(f"{i + 1}. {mcq['question']}")
                for j in range(len(mcq["options"])):
                    print(f"  {chr(97 + j)}) {mcq['options'][j]}")
                print(f"   Correct option: {mcq['correct_option']}")
            else:
                print(f"{i + 1}. {question_list[i]}")

        question_choice = int(input(f"\nEnter the number of the question you want to modify (1-{len(question_list)}): "))
        if 1 <= question_choice <= len(question_list):
            if section == "Section A":
                print("Enter the new MCQ details:")
                new_mcq = self.create_mcq()
                current_set[section][question_choice - 1] = new_mcq
            else:
                print("Enter the new subjective question:")
                new_question = self.create_subjective()
                current_set[section][question_choice - 1] = new_question
            print("Question modified successfully!")
            self.save_exam_papers()
        else:
            print("Invalid question number.")

# To run the program
if __name__ == "__main__":
    system = AcademicAdminSystem()
    system1 = ExamUnitPersonnel()
    lecturer_system = RegisteredLecturer()
    while True: 
        print("1. Academic admin Panel")
        print("2. Registered lecturer Panel")
        print("3. Exam unit personnel Panel")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("***Welcome to the Academic admin Panel***")
                system.admin_Login()
            elif choice == 2:
                lecturer_system.login()
            elif choice == 3:
                system1.login()
            else:
                print("Invalid choice! Exiting.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
