import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {data["letter"][index]: data["code"][index] for (index, row) in data.iterrows()}


def generate_nato():
    word = str(input("Word to NATO: ")).upper()
    try:
        answer = [NATO_dict[word] for word in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato()

    else:
        print(answer)


generate_nato()
