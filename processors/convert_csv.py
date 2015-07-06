import csvkit
import json


def main():
    state_hash = get_stateface()

    writer.writerow(["state", "property", "violence", "sf"])

    [reader.next() for i in range(0, 15)]

    for row in reader:
        area = ("".join([s for s in row[0].strip() if not s.isdigit()])
                  .replace(",", ""))

        if area != "":
            current_state = area

        if current_state == "Puerto Rico":
            continue

        if current_state not in regions and row[1].strip() == "Percent change":
            payload.append([current_state, row[4].strip(), row[16].strip(),
                            state_hash[current_state.title()]])

    writer.writerows(payload)


def get_stateface():
    with open("data/state_hash.json") as f:
        state_hash = json.load(f)
    with open("data/stateface.json") as f:
        data = json.load(f)
        data.pop("US")
        return dict([[state_hash[k], v] for k, v in data.items()])


if __name__ == "__main__":
    reader = csvkit.CSVKitReader(open("data/raw.csv"))
    writer = csvkit.CSVKitWriter(open("data/data.csv", "wb"))

    regions = ["Middle Atlantic", "Midwest", "East North Central",
               "West North Central", "South", "South Atlantic",
               "East South Central", "West South Central", "West",
               "Mountain.", "Pacific"]
    current_state = None
    payload = []

    main()
