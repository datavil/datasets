install.packages("palmerpenguins")

# source https://github.com/allisonhorst/palmerpenguins
penguins <- palmerpenguins::penguins

write.csv(penguins, "./csv/penguins.csv")
