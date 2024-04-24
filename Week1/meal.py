def main():
    meal = input("What time is it? ").strip()
    if 7.0 <= convert(meal) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(meal) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(meal) <= 19.0:
        print("dinner time")
    else:
        exit()


def convert(time):
    x, y = time.split(":")
    h = float(x)
    m = float(y)/60
    return h + m



if __name__ == "__main__":
    main()
