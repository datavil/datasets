if (!require("nycflights13")) install.packages("nycflights13")

#https://github.com/tidyverse/nycflights13
"
?flights: all flights that departed from NYC in 2013
?weather: hourly meterological data for each airport
?planes: construction information about each plane
?airports: airport names and locations
?airlines: translation between two letter carrier codes and names
"
#extract datasets from the nycflights13 package
flights <- nycflights13::flights
weather <- nycflights13::weather
planes <- nycflights13::planes
airports <- nycflights13::airports
airlines <- nycflights13::airlines

#export to csv folder
write.csv(flights, "./csv/flights.csv", row.names = FALSE, na = "")
write.csv(weather, "./csv/weather.csv", row.names = FALSE, na = "")
write.csv(planes, "./csv/planes.csv", row.names = FALSE, na = "")
write.csv(airports, "./csv/airports.csv", row.names = FALSE, na = "")
write.csv(airlines, "./csv/airlines.csv", row.names = FALSE, na = "")
