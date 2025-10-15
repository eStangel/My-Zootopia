import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')
print(animals_data)
for animal in animals_data:
    print(
        f"Name: {animal['name']}\n"
        f"Diet: {animal['characteristics']['diet']}\n"
        f"Location: {animal['locations'][0]}"
    )
    if animal['characteristics'].get('type', 0) != 0:
        print(f"Type: {animal['characteristics']['type']}\n")
    else:
        print()