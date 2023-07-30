# Iteration 2: Basic GUI

import PySimpleGUI as sg

# Define a dictionary of courses and their minimum GPA requirements
courses = {
    "Computer Science": {"GPA": 85, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/computer-science.html"},
    "Engineering": {"GPA": 75, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-engineering-honours-behons.html"},
    "Business": {"GPA": 60, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-commerce-bcom.html"},
    "Arts": {"GPA": 50, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-arts-ba.html"},
    "Education": {"GPA": 40, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-education-teaching-bedtchg.html"}
}

def get_recommendations(name, gpa):
    if gpa >= 85:
        message = f"Hello {name}, you have an excellent GPA. You can apply for any course you want."
    elif gpa >= 75:
        message = f"Hello {name}, you have a good GPA. You can apply for most courses except Computer Science."
    elif gpa >= 60:
        message = f"Hello {name}, you have a decent GPA. You can apply for Business, Arts, or Education courses."
    elif gpa >= 50:
        message = f"Hello {name}, you have a low GPA. You can only apply for Arts or Education courses."
    else:
        message = f"Hello {name}, you have a very low GPA. You may not be eligible for any university courses."

    # Print the list of recommended courses based on the GPA
    message += "\nHere are some recommended courses for you:"
    for course, info in courses.items():
        if gpa >= info["GPA"]:
            message += f"\n- {course}"

    return message

# Create the layout for the window
layout = [
    [sg.Text('Enter Your Name:  '), sg.InputText(key='-NAME-')],
    [sg.Text('Enter Your Highschool GPA:'), sg.InputText(key='-GPA-')],
    [sg.Button('Ok'), sg.Button('Cancel')],
    [sg.Output(size=(70, 10))]  # Display course recommendations here
]

def main():
    window = sg.Window('Course Recommendation System', layout)

    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):
            break

        name = values['-NAME-']
        gpa = float(values['-GPA-'])

        if gpa < 0 or gpa > 100:
            sg.popup("Invalid GPA. Please enter a number between 0 and 4.")
        else:
            recommendations = get_recommendations(name, gpa)
            print(recommendations)

    window.close()

if __name__ == "__main__":
    main()
