

# calculate the total sales for each year
total_sales_2022 = sum_sales(load("data/book_sales_2022.csv"), 
                             load("data/game_sales_2022.csv"))
total_sales_2023 = sum_sales(load("data/book_sales_2023.csv"),
                              load("data/game_sales_2023.csv"))
total_sales_2024 = sum_sales(load("data/book_sales_2024.csv"),
                              load("data/game_sales_2024.csv"))

