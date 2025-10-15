import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
output = ""
for animal in animals_data:
    output += (
        f"Name: {animal['name']}\n"
        f"Diet: {animal['characteristics']['diet']}\n"
        f"Location: {animal['locations'][0]}\n"
    )
    if animal['characteristics'].get('type', 0) != 0:
        output += f"Type: {animal['characteristics']['type']}\n\n"
    else:
        output += "\n"

with open("animals_template.html", "r") as f:
    data = f.read()

data = data.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as f:
    f.write(data)