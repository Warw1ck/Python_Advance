def students_credits(*args):
    course = []
    total_credits = 0
    for el in args:
        name, credits_num, max_points, person_points = el.split('-')
        procent = int(person_points)/int(max_points)
        credits_num = int(credits_num) * (procent)

        total_credits += round(credits_num, 1)
        course.append([name, round(credits_num, 1)])
    if total_credits >= 240:
        print(f"Diyan gets a diploma with {total_credits} credits.")
    else:
        print(f"Diyan needs {240 - total_credits} credits more for a diploma.")

    return '\n'.join([f'{a} - {round(b, 1)}' for a, b in sorted(course, key=lambda x: -x[1])])




print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

