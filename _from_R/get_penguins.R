if (!require("palmerpenguins")) install.packages("palmerpenguins")
penguins <- palmerpenguins::penguins

# Write CSV without row names (index column)
write.csv(penguins, "./csv/penguins.csv", row.names = FALSE, na = "")