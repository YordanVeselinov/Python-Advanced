def gather_credits(needed_credits, *args):
    collected_credits = 0
    coursed_take = []
    result = ""

    for course, current_credits in args:

        if course not in coursed_take:
            coursed_take.append(course)
            collected_credits += current_credits

        if collected_credits >= needed_credits:
            break

    if collected_credits >= needed_credits:
        result += f"Enrollment finished! Maximum credits: {collected_credits}.\n"
        result += f"Courses: {', '.join(sorted(coursed_take, key=lambda x: x))}"
    else:
        result += f"You need to enroll in more courses! You have to gather {abs(needed_credits - collected_credits)} credits more."

    return result


from unittest import TestCase, main


class Test(TestCase):
    def test_students_credits(self):
        result = gather_credits(
            80,
            ("Advanced", 30),
            ("Basics", 27),
            ("Fundamentals", 27),

        )

        self.assertEqual(
            result.strip(),
            """Enrollment finished! Maximum credits: 84.
Courses: Advanced, Basics, Fundamentals""")


if __name__ == '__main__':
    main()