Import pandas as pd


Data = {
    “Student ID”: [
        “24/14212”,
        “24/15387”,
        “24/16742”,
        “24/12895”,
        “24/17463”,
        “24/13926”,
        “24/18531”,
        “24/15608”,
        “24/19274”,
        “24/16359”
    ],

    “Department”: [
        “Computer Science”,
        “Mass communication ”,
        “Nursing”,
        “Computer Science”,
        “Internationalrelations ”,
        “cybersecurity ”,
        “software engineering”,
        “Criminology”,
        “Politicalscience ”,
        “Biochemistry
    ],

    “Level”: [
        100, 200, 300, 400, 200,
        100, 300, 400, 100, 200
    ],

    “Attendance Percentage”: [
        85, 90, 78, 95, 82,
        88, 75, 92, 80, 89
    ],

    “Average Examination Score”: [
        76, 85, 68, 91, 73,
        80, 65, 88, 72, 84
    ]
}


Students = pd.DataFrame(data)


Print(students)
