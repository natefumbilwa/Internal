import PySimpleGUI as sg

# Define a dictionary of courses and their minimum GPA requirements
courses = {
    "Computer Science": {"GPA": 85, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/computer-science.html"},
    "Engineering": {"GPA": 75, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-engineering-honours-behons.html"},
    "Business": {"GPA": 60, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-commerce-bcom.html"},
    "Arts": {"GPA": 50, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-arts-ba.html"},
    "Education": {"GPA": 40, "Link": "https://www.auckland.ac.nz/en/study/study-options/find-a-study-option/bachelor-of-education-teaching-bedtchg.html"}
}

# Define a dictionary of course descriptions
descriptions = {
    "Computer Science": "Computer science is the study of computation and information. It involves the design, analysis, implementation, and application of algorithms, data structures, programming languages, software systems, and hardware devices.",
    "Engineering": "Engineering is the application of science, mathematics, and technology to create solutions for various problems in society. It involves the design, construction, testing, and maintenance of structures, machines, systems, and processes.",
    "Business": "Business is the activity of making money by producing or buying and selling goods or services. It involves the management, organization, operation, and strategy of various enterprises in different sectors and markets.",
    "Arts": "Arts is the expression of human creativity and imagination in various forms such as literature, music, painting, sculpture, theater, film, and dance. It involves the creation, interpretation, appreciation, and criticism of various works of art.",
    "Education": "Education is the process of facilitating learning and acquiring knowledge, skills, values, and attitudes. It involves the teaching, training, guidance, and assessment of students in various settings such as schools, colleges, universities, and workplaces."
}

# Define the layout of the first window
layout1 = [[sg.Text('Enter Your Name:  '), sg.InputText(key='-NAME-')],
           [sg.Text('Enter Your NCEA GPA:'), sg.InputText(key='-GPA-')],
           [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel')]]

# Create the first window object
window1 = sg.Window('Student Data Collection', layout1)

# Loop to handle the events and values of the first window
while True:
    event1, values1 = window1.read()
    if event1 in (None, 'Cancel'):
        break
    name = values1['-NAME-']
    gpa = float(values1['-GPA-'])
    
    # Check if the GPA is valid
    if gpa < 0 or gpa > 100:
        sg.popup("Invalid GPA. Please enter a number between 0 and 100.")
    else:
        # Print a message based on the GPA
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
        layout2 = [[sg.Text(message)]]
        for course, info in courses.items():
            if gpa >= info["GPA"]:
                layout2.append([sg.Button(course)])

        # Create the second window object
        window2 = sg.Window('Course Recommendations', layout2)

        # Loop to handle the events and values of the second window
        while True:
            event2, values2 = window2.read()
            if event2 in (None, 'Cancel'):
                break
            # Check if the event is one of the course buttons
            if event2 in courses.keys():
                course_info = f"{event2}: {descriptions[event2]}\n\nApply at: {courses[event2]['Link']}"
                sg.popup(course_info)

        # Close the second window
        window2.close()

# Close the first window
window1.close()
