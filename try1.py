import random

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
                    username = parts[0]
                    password = parts[1]
                    self.credentials[username] = password
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
                ch = int(input("Enter your choice: "))
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
        with open('personnel.txt', 'w') as file:
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
    system1 = ExamUnitPersonnel()
    print("1. Academic admin Panel")
    print("2. Registered lecturer Panel")
    print("3. Exam unit personnel Panel")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("***Welcome to the Academic admin Panel***")
        # system.admin_Login()  # Implement this if needed
    elif choice == 2:
        pass
    elif choice == 3:
        system1.login()
    else:
        print("Invalid choice! Exiting.")
