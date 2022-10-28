#Emily Rusch and Kaylen Nyhuis

lines = ["Haiku frogs in snow", "A limerick came from Nantucket", "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

def breakify(x):
    print("<br>".join(x))

string = "Hello World!"
output = []
index = 0
while index < len(sting):
    output.append(string[index])
    index += 1

print(output)

string = 'SPAM!HelloSPAM! WorldSPAM!!'
output = []
index = 0
while index < len(string):
    if string[index:index+5] == 'SPAM!':
        index += 5
    else:
        output.append(string[index])
        index += 1
