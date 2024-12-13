import polars as pl
import os


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