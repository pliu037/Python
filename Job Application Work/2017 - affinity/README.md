To run:
python main.py <path to input file> <path to output file>

Next steps:
- Finish writing test cases
- Finish TODOs
- Realized in the last few minutes one of the "Mentor" column could contain an email rather than a name; can handle this
  by creating an index mapping emails to players, and when an email is encountered, use the index to find the
  corresponding player's first and last name
- Determine a better way of mapping column names, column indices, and handlers (I worked on categorizer.py near the end
  of the 5 hr period, so was running out of time to think about optimal design; probably move more of the column parsing
  from categorize.py to player.py)
- Use metaclasses to auto-register new classes that extend ScoreParser and DateParser, removing the need to manually
  add instances of the new classes to SCORE_PARSERS and DATE_PARSERS, respectively

Current assumptions:
- Each file contains a complete column set (i.e.: some combination that allows us to determine first name, last name,
  email, mentor, date, and score
- There are no duplicate columns (e.g.: 2 "Email" columns, even if named differently)
- Unrecognized columns are ignored
- The "Name" column is mutually exclusive to the "First name" and "Last name" columns
- The "Player" columns is mutually exclusive to the "First name", "Last name", and "Email" columns
- Although different formats for dates and scores can occur in the "Date" and "Score" columns, respectively, an entry
  formatted in the form expected for "Name" or "Player" cannot occur in a "First name", "Last name", or "Email" column
