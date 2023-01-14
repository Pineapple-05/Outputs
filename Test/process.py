import tui

lists = [["1", "2"], ["3", "4"], ["5", "6"], ["3", "4"]]


def hotel_name(reviews):
    hotel_n = tui.hotel_name()
    for n in range(1, len(reviews)):
        if hotel_n == reviews[n][1]:
            print(reviews[n])


def hotel_dates(reviews):
    hotel_d = tui.review_dates()
    for n in range(1, len(reviews)):
        for i in range(0, len(hotel_d)):
            if hotel_d[i] == reviews[n][0]:
                print(f"{hotel_d[i]}:{reviews[n]}")


def all_reviews(reviews):
    summary = {}
    for n in range(1, len(reviews)):
        summary.append(reviews[n][0])
        print(summary)

all_reviews(lists)
