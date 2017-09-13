import csv
print("PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked")
with open("train.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    decks = []
    for row in reader:
        # print("Passanger name:", row["Name"])
        deck = row["Cabin"]
        deckletter = list(deck)
        Survived = row["Survived"]
        if(len(deck)):
            print(deckletter[0])
        if(True):
            decks.append(deck)
            # print(row["Name"],"cabin number:", deck,"Survived",Survived)
            print(deck,"Survived", Survived)

        # else:
            # print("cabin number:",0)
    # sortedDecks =sorted(decks)
    # print(sortedDecks)





