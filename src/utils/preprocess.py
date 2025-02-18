import pandas as pd

filepaths = ["../../data/Books.csv", "../../data/Ratings.csv"]

def remove_invalid_records(filename):
    # Remove records w/o proper ISBN length or nondigits.
    df = pd.read_csv(filename)
    df["ISBN"] = df["ISBN"].astype(str).str.strip()
    df = df[df['ISBN'].apply(lambda x: (len(x) == 10 or len(x) == 13) and x.isdigit())]
    df.to_csv(filename, index=False)

def compute_check_digit(isbn):
    # Computes the check digit for conversion from ISBN-10 to ISBN-13
    if len(str(isbn)) not in (10, 13):
        raise ValueError(f"Invalid length of ISBN-10: {isbn, len(str(isbn))}")
    isbn = "978" + str(isbn)[:9]
    sum_of_digits = 0
    for i in range(len(isbn)):
        factor = 1 + ((i % 2) * 2)
        if isbn[i].lower() == "x":
            sum_of_digits += 10 * factor
        else:
            try:
                sum_of_digits += int(isbn[i]) * factor
            except ValueError as e:
                print(f"ERROR: Invalid digit in ISBN-10: {isbn[i], i}")
                return
    check_digit = (10 - (sum_of_digits % 10)) % 10
    return isbn + str(check_digit)

def convert_isbn(filename):
    # Takes CSV file and checks for ISBN columns.
    # If they exist, convert each field value into ISBN-13 new column.
    df = pd.read_csv(filename)
    fields = df.columns.tolist()
    if "ISBN" in fields:
        # Calculate final digit in ISBN-13 sequence
        df["ISBN-13"] = df["ISBN"].apply(compute_check_digit)
        df.to_csv(filename, index=False)
        return True
    return False

for fp in filepaths:
    remove_invalid_records(fp)
    convert_isbn(fp)
    print(fp, "DONE PROCESSING")