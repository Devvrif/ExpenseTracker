from pathlib import Path
import json 

expenses_file = Path("data/expenses.json")

def load_expenses():
    expenses_file.parent.mkdir(parents = True, exist_ok = True)
    
    if expenses_file.exists():
        try:
            data = json.loads(expenses_file.read_text())
            return data

        except json.JSONDecodeError:
            return []


def save_expenses(expenses_list):
    json_string=json.dumps(expenses_list, indent = 4)
    expenses_file.write_text(json_string)
