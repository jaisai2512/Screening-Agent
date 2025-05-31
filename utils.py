import re


#Tool used in saving user information
def extract_save_value(text):
    match = re.search(r"save:(.*)", text.strip())
    return match.group(1).strip() if match else ""
