import re

def extract_registration_numbers(file_path):
    with open(file_path, 'r') as file:
        data = file.load()
    return re.findall(r'[A-Z][a-z]+[0-9]+', data)


def load_expected_output(file_path):
    expected_results = {}
    with open(file_path, 'r') as file:
        for line in file:
            reg, value = line.strip.split(",")
            expected_results[reg] = value
    return expected_results