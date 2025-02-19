from django.shortcuts import render

def cv_view(request):
    cv_data = {
        "name": "Harsh Jalutharia",
        "email": "harshjalutharia@gmail.com",
        "phone": "+1 929-627-5059",
        "location": "Brooklyn, New York",
        "linkedin": "www.linkedin.com/in/harsh-jalutharia",
        "education": [
            {"degree": "MS in Computer Science", "institution": "New York University Tandon School of Engineering", "year": "2023-2025", "grade":"4.0 GPA"},
            {"degree": "B. Tech in Computer Engineering", "institution": "Delhi Technological University", "year": "2016-2020", "grade":"7.29 CGPA"},
            {"degree": "Grade 12 Science", "institution": "Delhi Public School Gandhinagar", "year": "2016", "grade":"92.8%"},
        ],
        "internships": [
            {"company": "Suzlon Energy Ltd", "time": "June 2019 - July 2019", 
             "point1": "Performed market research, created questionnaires, and communicated with 24 team leads across the country to determine 16 key factors influencing customer satisfaction.",
             "point2": "Carried out regression analysis on customer data to predict revenue and ensure timely payments."},
            {"company": "ONGC, Ahmedabad", "time": "June 2018 - July 2018",
             "point1": "Developed Well Locator App - View location and relevant data of 36 wells. Used Google Maps API.",
             "point2": "Developed Contacts App - Contact directory of ONGC employees capable of handling over 1000 records."},
        ],
        "research": [
            {"title": "College Major Project: Depression Detection using Facial Features", "time": "January 2020 - May 2020", 
             "point1": "Extracted facial features of subject and parsed them through an SVM classifier to estimate the depression level. Worked on classifier component and overall system integration.",
             "point2": "Research Paper presented in ICICCS 2020 and published in IEEE Xplore."},
            {"title": "Automatic Video Lecture Indexing", "time": "August 2019 - December 2019",
             "point1": "Created an application which can analyse a library of videos to create a searchable index.",
             "point2": "Designed the application GUI and performed text recognition using Python libraries."},
        ],
        "projects": [
            {"title": "Beta Dungeon - A top-down Roguelike with procedural generation", "time": "November 2021 - July 2022",
             "point1": "RPG with rogue elements where player must solve puzzles and take down enemies.",
             "point2": "Used procedural generation to design levels and developed using Unreal Engine 4 and C++."},
             {"title": "Clash Grounds - A multiplayer FPS game", "time": "January 2021 - September 2021",
             "point1": "First Person Shooter game where player must eliminate enemies or sneak by to proceed.",
             "point2": "Developed using Unreal Engine 4 and C++ and is Multiplayer."},
        ],
        "achievements": [
            {"entry": "Awarded Scholar Badge by the School for excellent performance in 12th standard in 2016."},
        ],
        "extraactivities": [
            {"entry": "Organized PUBG Tournament with 120 participants in IOSD DTU Festival in August 2019."},
            {"entry": "Food City Coordinator as part of the logistics team in the annual cultural festival Engifest 2019."},
            {"entry": "Creative team member in Engifest 2018."},
        ],
        "skills": [
            {"entry": "Proficient in C, C++ and Python"},
            {"entry": "Experience in Unreal Engine, Adobe Photoshop and Adobe Premiere Pro"},
            {"entry": "Certified in Python from University of Michigan (Coursera)"},
            {"entry": "Certified in Machine Learning from University of Washington (Coursera)"},
        ],
    }
    
    return render(request, "cv_template.html", {"cv": cv_data})