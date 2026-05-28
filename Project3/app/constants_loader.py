import json
with open(
    "app/constants/status_codes.json")as status_file:
    STATUS_CODES = json.load(status_file)
with open(
    "app/constants/error_messages.json")as error_file:
    ERROR_MESSAGES = json.load(error_file)
