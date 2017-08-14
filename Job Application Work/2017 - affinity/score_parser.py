import re
import abc
from utils import int_with_commas


class ScoreParser():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def parse(self, score_string):
        """
        :param score_string: The score string to parse
        :return: Returns a 2-tuple where the first element is a boolean indicating whether <score_string> matched the
                 internal regex followed by score in int representation
        """
        pass


class PlainScoreParser(ScoreParser):
    # TODO: Ensure that comma-separated integers are valid (i.e.: left-most group has at most 3 digits and all other
    #       groups have exactly 3 digits)
    compiled_regex = re.compile('^([\d+][\d+,*]*)$')

    def parse(self, score_string):
        result = self.compiled_regex.match(score_string)
        if result:
            score = re.sub(',', '', result.group(1))
            return True, int(score)
        return None, None


class UnitScorParser(ScoreParser):
    unit_to_factor = {'k': 1000, 'm': 1000000}
    compiled_regex = re.compile('^(\d+)([km]?)$')

    def parse(self, score_string):
        check = score_string.lower()
        result = self.compiled_regex.match(check)
        if result:
            score = int(result.group(1))
            unit = result.group(2)
            if unit in self.unit_to_factor:
                score *= self.unit_to_factor[unit]
            return True, score
        return None, None


SCORE_PARSERS = [PlainScoreParser(), UnitScorParser()]


class Score:
    def __init__(self, score_string):
        self.score = None
        for parser in SCORE_PARSERS:
            found, score = parser.parse(score_string)
            if found:
                self.score = score
                break
        if not self.score:
            raise RuntimeError('Incorrect date format for ' + score_string)

    def output_string(self):
        return '{}'.format(int_with_commas(self.score))
