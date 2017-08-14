from date_parser import Date
from score_parser import Score


class Player:
    column_names = ('First Name', 'Last Name', 'Email Address', 'Mentor', 'Date of Last Game', 'High Score')

    def __init__(self, first_name, last_name, email, mentor, date, score):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mentor = mentor
        self.date = Date(date)
        self.score = Score(score)

    def get_score(self):
        return self.score.score

    def get_column_names(self):
        return self.column_names

    def output(self):
        return (self.first_name, self.last_name, self.email, self.mentor, self.date.output_string(),
                self.score.output_string())
