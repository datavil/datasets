import polars as pl
import os
from pathlib import Path


"""
Conditions to move a Rdataset to main csv folder:
1. Not a huge file (size < 5MB)
2. Should have an simple name
3. Should have a descriptive name
4. Should be a common dataset
5. Column names should be descriptive
"""

to_take = [
    "abortion",
    "absentee",
    "addmissions"
    "AirChrash",
    "Alligator",
    "anorexia",
    "Arrests",
    "arthritis",
    "auto",
    "avocado",
    "babies",
    "BackPack"
    "barley",
    "BeeStings",
    "BirdCalcium",
    "BirdNest",
    "birds",
    "Births",
    "BlueJays"
    "boston_marathon",
    "Caterpillars",
    "cherry",
    "Chicago",
    "Chile",
    "Cholera",
    "coffee_price",
    "College",
    "CollegeDistance",
    "comics",
    "commodity_prices",
    "concrete",
    "constants",
    "Contraceptives",
    "country_codes",
    "covid_testing",
    "cpu",
    "crabs",
    "Credit",
    "Diabetes",
    "diamonds",
    "earthquakes",
    "epilepsy",
    "films",
    "fishing",
    "Fitch",
    "Forbes2000",
    "FruitFlies",
    "Gasoline",
    "Gestation",
    "gpa",
    "HealthInsurance",
    "Journals",
    "Ketchup",
    "london_murders",
    "Mortgage",
    "Municipalities",
    "murders",
    "nba_finals",
    "nba_heights",
    "oils",
    "olive",
    "oscars",
    "population",
    "PorscheJaguar",
    "Pottery",
    "president",
    "Salaries",
    "species",
    "stars",
    "storms",
    "Train",
    "UN",
    "usa_migration",
    "usa_states",
    "Utilities",
    "water",
    "Wells",
    "wine",
    "Yogurt",
]
def main():
    RDS = pl.read_csv("Rdatasets.csv")
    RDS = RDS.filter(pl.col("Item").is_in(to_take))
    # constants
    SOURCE = "https://github.com/vincentarelbundock/Rdatasets/"
    LICENSE = "GPL-3.0"
    ORIGIN = "Rdatasets"

    # info dataframe
    info = pl.read_csv("datasets_info.csv")

    #name,source,license,origin,docs
    for row in RDS.select(["Item", "CSV", "Doc"]).iter_rows():
        name, csv, doc = row
        # Check if the name already exists in the `info` DataFrame
        if not info.filter(pl.col("name") == name).height > 0:
            adict = {
                "name": name,
                "source": SOURCE,
                "license": LICENSE,
                "origin": ORIGIN,
                "doc": doc
            }
            new_row = pl.DataFrame([adict])
            info.extend(new_row)

        # Check if the csv file exists
        fname = f"csv/{name}.csv"
        target_file = Path(fname)
        if target_file.exists():
            pass
        else:
            frame = pl.read_csv(csv, infer_schema_length=50_000, encoding="iso-8859-1")
            if "rownames" in frame.columns:
                frame = frame.drop("rownames")
                frame.columns = [x.replace(".","_") for x in frame.columns]

            if not target_file.exists():  # Only write if the file doesn't already exist
                frame.write_csv(fname)
        
    info.write_csv("datasets_info.csv")

    return

if __name__ == "__main__":
    main()