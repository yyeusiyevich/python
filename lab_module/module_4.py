class Trainee:
    passing_grade = 8
    """
    Trainee class represents a trainee in the company.
    It has the following attributes:
    name: a string representing the trainee's name.
    surname: a string representing the trainee's surname.
    visited_lectures: an integer representing the number of lectures the trainee has visited.
    done_home_tasks: an integer representing the number of home tasks the trainee has done.
    missed_lectures: an integer representing the number of lectures the trainee has missed.
    missed_home_tasks: an integer representing the number of home tasks the trainee has missed.
    mark: an integer representing the trainee's mark.
    It has the following methods:
    visit_lecture: adds 1 point to the trainee's mark.
    do_homework: adds 2 points to the trainee's mark.
    miss_lecture: subtracts 1 point from the trainee's mark.
    miss_homework: subtracts 2 points from the trainee's mark.
    _add_points: adds points to the trainee's mark, taking into account the maximum mark (10).
    _ subtract_points: subtracts points from the trainee's mark, taking into account the minimum mark (0).
    is_passed: checks if the trainee has passed the course.
    If the mark is greater than or equal to 8, the trainee has passed.
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.visited_lectures = 0
        self.done_home_tasks = 0
        self.missed_lectures = 0
        self.missed_home_tasks = 0
        self.mark = 0

    def visit_lecture(self):
        self.visited_lectures += 1
        self._add_points(1)

    def do_homework(self):
        self.done_home_tasks += 2
        self._add_points(2)

    def miss_lecture(self):
        self.missed_lectures -= 1
        self._subtract_points(1)

    def miss_homework(self):
        self.missed_home_tasks -= 2
        self._subtract_points(2)

    def _add_points(self, points: int):
        if self.mark + points > 10:
            self.mark = 10
        else:
            self.mark += points

    def _subtract_points(self, points):
        if self.mark - points < 0:
            self.mark = 0
        else:
            self.mark -= points

    def is_passed(self):
        if self.mark >= Trainee.passing_grade:
            print("Good job!")
        else:
            missing_points = Trainee.passing_grade - self.mark
            print(f"You need to {missing_points} points. Try to do your best!")

    def __str__(self):
        status = f"Trainee {self.name.title()} {self.surname.title()}:\n" \
                 f"done homework {self.done_home_tasks} points;\n" \
                 f"missed homework {self.missed_home_tasks} points;\n" \
                 f"visited lectures {self.visited_lectures} points;\n" \
                 f"missed lectures {self.missed_lectures} points;\n" \
                 f"current mark {self.mark};\n" \

        return status