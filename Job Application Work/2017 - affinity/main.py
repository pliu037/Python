import sys
from file_io import *
from categorizer import Categorizer


def convert_data_from_file(input_file_path, output_file_path):
    data = read_from_file(input_file_path)
    if data:
        categorizer = Categorizer(data[0])
        players = data[1:]
        processed_players = categorizer.parse_players(players)
        sorted_players = sorted(processed_players, reverse=True, key=lambda x: x.get_score())
        output = []
        output.append(sorted_players[0].get_column_names())
        for player in sorted_players:
            output.append(player.output())
        for out in output:
            print out
        write_to_file(output_file_path, output)


if __name__ == '__main__':
    if len(sys.argv[0]) >= 3:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        convert_data_from_file(sys.argv[1], sys.argv[2])
    else:
        raise RuntimeError('Please provide a file path')
