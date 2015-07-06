import csvkit


def main():
    writer.writerow(["state", "property", "violence"])

    [reader.next() for i in range(0, 15)]

    for row in reader:
        area = ("".join([s for s in row[0].strip() if not s.isdigit()])
                  .replace(",", ""))

        if area != "":
            current_state = area

        if current_state not in regions and row[1].strip() == "Percent change":
            payload.append([current_state, row[4].strip(), row[16].strip()])

    writer.writerows(payload)


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
