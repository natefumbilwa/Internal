import PySimpleGUI as sg
import csv

# Define a class for the Course Recommendation App
class CourseRecommendationApp:
    def __init__(self):

        # Dictionary containing course information with GPA requirements and links
        self.courses = {
            "Computer Science": {"GPA": 85, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/computer-science.html"},
            "Engineering": {"GPA": 75, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-engineering-honours-behons.html"},
            "Business": {"GPA": 60, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-commerce-bcom.html"},
            "Arts": {"GPA": 50, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-arts-ba.html"},
            "Education": {"GPA": 40, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-education-teaching-bedtchg.html"},
            "Science": {"GPA": 70, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-science-bsc.html"},
            "Health Sciences": {"GPA": 65, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-health-sciences-bhsc.html"},
            "Law": {"GPA": 80, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-laws-llb.html"}
        }
        
        # Dictionary containing course descriptions
        self.descriptions = {
            "Computer Science": "Computer science is the study of computation and information. It involves the design, analysis, implementation, and application of algorithms, data structures, programming languages, software systems, and hardware devices.",
            "Engineering": "Engineering is the application of science, mathematics, and technology to create solutions for various problems in society. It involves the design, construction, testing, and maintenance of structures, machines, systems, and processes.",
            "Business": "Business is the activity of making money by producing or buying and selling goods or services. It involves the management, organization, operation, and strategy of various enterprises in different sectors and markets.",
            "Arts": "Arts is the expression of human creativity and imagination in various forms such as literature, music, painting, sculpture, theater, film, and dance. It involves the creation, interpretation, appreciation, and criticism of various works of art.",
            "Education": "Education is the process of facilitating learning and acquiring knowledge, skills, values, and attitudes. It involves the teaching, training, guidance, and assessment of students in various settings such as schools, colleges, universities, and workplaces.",
            "Science": "Science is the systematic study of the natural world through observation and experimentation. It involves various disciplines such as biology, chemistry, physics, and environmental science.",
            "Health Sciences": "Health Sciences encompass a range of medical and health-related fields focused on understanding, maintaining, and improving human health. It includes disciplines like medicine, nursing, public health, and biomedical science.",
            "Law": "Law is the system of rules and regulations that govern society and protect individual rights. It involves the interpretation, application, and enforcement of legal principles and statutes.",
}

        # List of broad interests available for selection
        self.interests = ["Computer Science", "Engineering", "Business", "Arts", "Education", "Science", "Health Sciences", "Law"]
        
        # File name for storing user data
        self.csv_file = 'user_data.csv'

    # Saves the user data to a CSV file
    def save_user_data(self, name, gpa, selected_interests):
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, gpa, ', '.join(selected_interests)])

    # Checks if the entered name is valid
    def is_valid_name(self, name):
        return name.strip() != ""

    # Checks if the entered GPA is a valid float between 0 and 100
    def is_valid_gpa(self, gpa):
        try:
            gpa = float(gpa)
            return 0 <= gpa <= 100
        except ValueError:
            return False

    # Filters courses based on the entered GPA and selected interests
    def get_filtered_courses(self, gpa, selected_interests):
        if not selected_interests:
            return {course: info for course, info in self.courses.items() if gpa >= info["GPA"]}
        else:
            return {course: info for course, info in self.courses.items() if course in selected_interests and gpa >= info["GPA"]}

    # Starts the application by creating the first window
    def run(self):
        self.create_first_window()

    # Creates the initial window for data collection
    def create_first_window(self):
        layout = [
            [sg.Text('Enter Your Name:  '), sg.InputText(key='-NAME-')],
            [sg.Text('Enter Your NCEA GPA:'), sg.InputText(key='-GPA-')],
            [sg.Text('Select Your Broad Interests:')],
            [sg.Checkbox(interest, key=f'-INTEREST-{index}', default=False) for index, interest in enumerate(self.interests)],
            [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel')]
        ]
        window = sg.Window('Student Data Collection', layout)

        while True:
            event, values = window.read()
            if event in (None, 'Cancel'):
                break

            name = values['-NAME-']
            gpa = values['-GPA-']

            if not self.is_valid_name(name):
                sg.popup("Please enter a valid name.")
                continue

            if not self.is_valid_gpa(gpa):
                sg.popup("Please enter a valid GPA (a number between 0 and 100).")
                continue

            gpa = float(gpa)
            selected_interests = [self.interests[index] for index in range(len(self.interests)) if values[f'-INTEREST-{index}']]

            if gpa < 0 or gpa > 100:
                sg.popup("Invalid GPA. Please enter a number between 0 and 100.")
            else:
                # Proceed to display the course recommendations
                self.display_course_recommendations(name, gpa, selected_interests)

            # Save the user data
            self.save_user_data(name, gpa, selected_interests)

        window.close()

    # Displays course recommendations based on the user's GPA and interests
    def display_course_recommendations(self, name, gpa, selected_interests):
        filtered_courses = self.get_filtered_courses(gpa, selected_interests)
        message = ""

        # Generate a recommendation message based on GPA
        if gpa >= 85:
            message = f"Hello {name}, you have an excellent GPA. You can apply for any course you want."
        elif gpa >= 75:
            message = f"Hello {name}, you have a good GPA. You can apply for most courses except Computer Science."
        elif gpa >= 60:
            message = f"Hello {name}, you have a decent GPA. You can apply for Business, Arts, Education, Science, or Health Sciences courses."
        elif gpa >= 40:
            message = f"Hello {name}, you have a low GPA. You can only apply for Arts, Education, Science, or Health Sciences courses."
        else:
            message = f"Hello {name}, you have a very low GPA. You may not be eligible for any university courses."

        # Generate buttons or text for each eligible course
        layout = [[sg.Text(message)]]
        for course, info in self.courses.items():
            if gpa >= info["GPA"]:
                if course in filtered_courses:
                    layout.append([sg.Button(course)])
                else:
                    layout.append([sg.Text(f"{course} (Not an interest, but GPA is high enough)")])

        window = sg.Window('Course Recommendations', layout)

        while True:
            event, values = window.read()
            if event in (None, 'Cancel'):
                break

            # Show a popup with course information when a course button is clicked
            if event in filtered_courses:
                course_info = f"{event}: {self.descriptions[event]}\n\nApply at: {filtered_courses[event]['Link']}"
                sg.popup(course_info)

        window.close()

# Entry point of the application
if __name__ == "__main__":
    app = CourseRecommendationApp()
    app.run()
