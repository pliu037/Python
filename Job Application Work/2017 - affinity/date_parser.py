import re
import abc


class DateParser():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def parse(self, date_string):
        """
        :param date_string: The date string to parse
        :return: Returns a 4-tuple where the first element is a boolean indicating whether <date_string> matched the
                 internal regex followed by month, day, and year in int representation
        """
        pass


class StringMonthDateParser(DateParser):
    string_to_numeric_month = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7,
                               'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12, 'jan': 1,
                               'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9,
                               'oct': 10, 'nov': 11, 'dec': 12}
    compiled_regex = re.compile('^([^\W\d_]+) (\d+), (\d+)$')

    def parse(self, date_string):
        result = self.compiled_regex.match(date_string)
        if result:
            month = result.group(1).lower()
            day = result.group(2)
            year = result.group(3)
            if month in self.string_to_numeric_month:
                return True, self.string_to_numeric_month[month], int(day), int(year)
        return None, None, None, None


class NumericMonthDateParser(DateParser):
    compiled_regex = re.compile('^(\d+)/(\d+)/(\d+)$')

    def parse(self, date_string):
        result = self.compiled_regex.match(date_string)
        if result:
            month = result.group(1)
            day = result.group(2)
            year = result.group(3)
            return True, int(month), int(day), int(year)
        return None, None, None, None


DATE_PARSERS = [StringMonthDateParser(), NumericMonthDateParser()]


class Date:
    numeric_month_to_string_month = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
                                     9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    days_in_month = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, date_string):
        self.month = None
        self.day = None
        self.year = None
        for parser in DATE_PARSERS:
            found, month, day, year = parser.parse(date_string)
            if found:
                self.month = month
                self.day = day
                self.year = year
                break
        if not self.valid_date_information():
            raise RuntimeError('Incorrect date format for ' + date_string)

    def valid_date_information(self):
        if not self.day or not self.month or not self.year:
            return False
        if self.month < 1 or self.month > 12 or self.day < 1:
            return False
        # Ignores February because of leap years
        if self.month != 2:
            if self.day > self.days_in_month[self.month]:
                return False
        else:
            if (not self.is_leap_year() and self.day > 28) or self.day > 29:
                return False
        return True

    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                return False
            return True
        return False

    def output_string(self):
        return '{} {}, {}'.format(self.numeric_month_to_string_month[self.month], str(self.day), str(self.year))
