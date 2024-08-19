def season_name_from_month_no(month_no: int) -> str:
    seasons = ("winter", "spring", "summer", "fall")
    # very nice formula because the month numbering starts from 1
    i = (month_no % 12) // 3
    return seasons[i]


if __name__ == '__main__':
    for i in range(1, 12 + 1):
        print(season_name_from_month_no(i))
