import re

class DateTimeValidator:
    def __init__(self, dt_format):
        self.dt_format = dt_format
        self.pattern = re.compile(dt_format)

    def is_valid_datetime(self, dt_str):
        return self.pattern.match(dt_str) is not None


class DateTimeExtractor:
    def __init__(self, validator):
        self.validator = validator

    def extract_valid_datetimes(self, input_file, output_file):
        with open(input_file, 'r') as f:
            datetimes = f.readlines()

        valid_datetimes = []  # Use a list instead of a set
        for dt in datetimes:
            dt = dt.strip()
            if self.validator.is_valid_datetime(dt):
                valid_datetimes.append(dt)  # Append to list instead of adding to set

        with open(output_file, 'w') as f:
            for dt in valid_datetimes:
                f.write(dt + '\n')


if __name__ == "__main__":
    dt_format = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](Z|([+-]\d{2}:\d{2}))$'

    validator = DateTimeValidator(dt_format)
    extractor = DateTimeExtractor(validator)

    input_file = "../IOFiles/input.txt"  # Change this to your input file name
    output_file = "../IOFiles/output.txt"  # Change this to your output file name

    extractor.extract_valid_datetimes(input_file, output_file)
