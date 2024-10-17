import random
class ExamUnitPersonnel:
    def __init__(self):
        self.credentials = {}
        self.exam_papers = {"Set 1": {"Section A": [], "Section B": []}, "Set 2": {"Section A": [], "Section B": []}}
        self.mcq_bank = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "correct_option": "1"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "correct_option": "2"},
            {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "correct_option": "3"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Mark Twain", "William Shakespeare", "J.K. Rowling", "Charles Dickens"], "correct_option": "2"},
            {"question": "What is the boiling point of water?", "options": ["90°C", "100°C", "110°C", "120°C"], "correct_option": "2"}
        ]
        self.subjective_bank = [
            "Explain the theory of relativity.",
            "Describe the process of photosynthesis.",
            "What are the causes of World War II?",
            "Discuss the impact of technology on modern education.",
            "Analyze the themes in 'To Kill a Mockingbird'."
        ]

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
                print("***************Welcome to the exam unit personal panel*******")
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
        return random.choice(self.mcq_bank)

    def create_subjective(self):
        return random.choice(self.subjective_bank)

    def create_exam_papers(self):
        set1 = {"Section A": [], "Section B": []}
        set2 = {"Section A": [], "Section B": []}

        print("Create questions for Set 1, Section A (MCQs):")
        while len(set1["Section A"]) < 5:
            mcq = self.create_mcq()
            set1["Section A"].append(mcq)

        print("Create questions for Set 1, Section B (Subjective):")
        while len(set1["Section B"]) < 3:
            subjective = self.create_subjective()
            set1["Section B"].append(subjective)

        print("Create questions for Set 2, Section A (MCQs):")
        while len(set2["Section A"]) < 5:
            mcq = self.create_mcq()
            set2["Section A"].append(mcq)

        print("Create questions for Set 2, Section B (Subjective):")
        while len(set2["Section B"]) < 3:
            subjective = self.create_subjective()
            set2["Section B"].append(subjective)

        self.exam_papers["Set 1"] = set1
        self.exam_papers["Set 2"] = set2

        self.save_exam_papers()
        print("Exam papers created and saved successfully!")

    def create_mcq(self):
        question = input("Enter the question: ")
        options = []
        for i in range(4):
            option = input(f"Enter option {chr(97 + i)}: ")
            options.append(option)
        correct_option = input("Enter the correct option (a, b, c, d): ")
        return {
            "question": question,
            "options": options,
            "correct_option": correct_option
        }

    def create_subjective(self):
        return input("Enter the new subjective question: ")

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

if __name__ == "__main__":
    system1 = ExamUnitPersonnel()
    print("1. Academic admin Panel")
    print("2. Registered lecturer Panel")
    print("3. Exam unit personnel Panel")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("***Welcome to the Academic admin Panel***")
    elif choice == 2:
        pass
    elif choice == 3:
        system1.login()

    else:
        print("Invalid choice! Exiting.")
