Entrance = "hello world and practice makes perfect and hello world again"
if not type(Entrance) == str :
    print("The argument Is Not str:")
elif str == int :
    print("The argument Not is int")
Words = Entrance.split(" ")
print(Words)
Counter = 0
WordsIndexOne = []
WordsMajorityOne = []
for Word in Words:
    print(f"***{Word}***")
    for Validator in Words :
        if Word == Validator:
            Counter +=1
            print(f"-----{Word}---->{Counter}")
    if Counter == 1: 
        WordsIndexOne.append(Word)
    if Counter > 1 and not Word in WordsMajorityOne :
        WordsMajorityOne.append(Word)
    Counter = 0
TextWithOutDuplicates = WordsIndexOne + WordsMajorityOne
FilledText = " ".join(TextWithOutDuplicates)
print(Words)
print(WordsIndexOne)
print(WordsMajorityOne)
print(TextWithOutDuplicates)
print(FilledText)


