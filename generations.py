def which_generation_am_I(year):
    generations = [
    (1901, "Greatest Generation"),
    (1928, "Silent Generation"),
    (1946, "Baby Boomers (Boomers)"),
    (1966, "Generation X"),
    (1981, "Generation Y (Millennials)"),
    (1997, "Generation Z (Zoomers)"),
    (2013, "Generation Alpha"),
    ]

    current_generation = "This year is out of range for defined generations."


    for start_year, generation_name in generations:

        if year < start_year:
            break

        current_generation = generation_name

    return current_generation