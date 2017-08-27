from player import Player


class Categorizer:
    first_name_fields = {'first name', 'first'}
    last_name_fields = {'last name', 'last'}
    email_fields = {'email address', 'email'}
    mentor_fields = {'mentor'}
    date_fields = {'date of last game', 'last game date', 'most recent game date'}
    score_fields = {'high score', 'highest score', 'max score'}
    name_fields = {'name'}
    player_fields = {'player'}

    def __init__(self, columns):
        self.first_name_index = None
        self.last_name_index = None
        self.email_index = None
        self.mentor_index = None
        self.date_index = None
        self.score_index = None
        self.name_index = None
        self.player_index = None
        self.num_columns = 0
        for index, column in enumerate(columns):
            check = column.lower()
            if check in self.first_name_fields:
                if self.first_name_index is not None or self.name_index is not None or self.player_index is not None:
                    raise RuntimeError('Duplicate first name field: ' + columns)
                self.first_name_index = index
                self.num_columns += 1

            elif check in self.last_name_fields:
                if self.last_name_index is not None or self.name_index is not None or self.player_index is not None:
                    raise RuntimeError('Duplicate last name field: ' + columns)
                self.last_name_index = index
                self.num_columns += 1

            elif check in self.email_fields:
                if self.email_index is not None or self.player_index is not None:
                    raise RuntimeError('Duplicate email field: ' + columns)
                self.email_index = index
                self.num_columns += 1

            elif check in self.mentor_fields:
                if self.mentor_index is not None:
                    raise RuntimeError('Duplicate mentor field: ' + columns)
                self.mentor_index = index
                self.num_columns += 1

            elif check in self.date_fields:
                if self.date_index is not None:
                    raise RuntimeError('Duplicate date field: ' + columns)
                self.date_index = index
                self.num_columns += 1

            elif check in self.score_fields:
                if self.score_index is not None:
                    raise RuntimeError('Duplicate score field: ' + columns)
                self.score_index = index
                self.num_columns += 1

            elif check in self.name_fields:
                if self.name_index is not None or self.first_name_index is not None or self.last_name_index is not None:
                    raise RuntimeError('Duplicate name field: ' + columns)
                self.name_index = index
                self.num_columns += 1

            elif check in self.player_fields:
                if self.player_index is not None or self.first_name_index is not None or self.last_name_index is not \
                        None or self.email_index is not None:
                    raise RuntimeError('Duplicate player field: ' + columns)
                self.player_index = index
                self.num_columns += 1
        if not self.valid_column_set():
            raise RuntimeError('Not a valid column set: ' + str(self.__dict__))

    def valid_column_set(self):
        if self.score_index is None or self.date_index is None or self.mentor_index is None:
            return False
        valid = False
        if self.player_index is not None and self.email_index is None and self.first_name_index is None and \
                self.last_name_index is None:
            valid = True
        elif self.name_index is not None and self.first_name_index is None and self.last_name_index is None and \
                self.email_index is not None:
            valid = True
        elif self.email_index is not None and self.first_name_index is not None and self.last_name_index is not None:
            valid = True
        return valid

    def parse_players(self, players_tokens):
        processed_players = []
        for player_line in players_tokens:
            processed_players.append(self.parse_player(player_line))
        return processed_players

    def parse_player(self, player_tokens):
        if len(player_tokens) != self.num_columns:
            raise RuntimeError('Expected {} columns but got {}'.format(self.num_columns, player_tokens))
        if self.first_name_index is not None:
            first_name = player_tokens[self.first_name_index]
            last_name = player_tokens[self.last_name_index]
            email = player_tokens[self.email_index]
        if self.name_index is not None:
            email = player_tokens[self.email_index]
            name = player_tokens[self.name_index]
            name_tokens = name.split(',')
            first_name = name_tokens[1].strip()
            last_name = name_tokens[0].strip()
        if self.player_index is not None:
            player = player_tokens[self.player_index]
            tokens = player.split()
            first_name = ' '.join(tokens[:-2])
            last_name = tokens[-2]
            raw_email = tokens[-1]
            email = raw_email.strip('<>')
        mentor = player_tokens[self.mentor_index]
        date = player_tokens[self.date_index]
        score = player_tokens[self.score_index]
        return Player(first_name.title(), last_name.title(), email, mentor, date, score)
