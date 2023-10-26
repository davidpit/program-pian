def spatiu():
    for i in range(3):
        print("")
    
game = {
    'C': ['C', 'Dm', 'Em', 'F', 'G', 'Am'],
    'C#': ['C#', 'D#m', 'Fm', 'F#', 'G#', 'A#m'],
    'D': ['D', 'Em', 'F#m', 'G', 'A', 'Bm'],
    'D#': ['D#', 'Fm', 'Gm', 'G#', 'A#', 'Cm'],
    'E': ['E', 'F#m', 'G#m', 'A', 'B', 'C#m'],
    'F': ['F', 'Gm', 'Am', 'A#', 'C', 'Dm'],
    'F#': ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m'],
    'G': ['G', 'Am', 'Bm', 'C', 'D', 'Em'],
    'G#': ['G#', 'A#m', 'Cm', 'C#', 'D#', 'Fm'],
    'A': ['A', 'Bm', 'C#m', 'D', 'E', 'F#m'],
    'A#': ['A#', 'Cm', 'Dm', 'D#', 'F', 'Gm'],
    'B': ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m']
}




song="""   D     G         D   A           Bm 
R: Cântă suflet al meu pentru Dumnezeu,
       G  D  Asus  A 
Cel binecuvântat
"""


for char in song:
    print(char, end="")


#gama=input("In ce gama e piesa? ")
gama_initiala="D" #AICI TREBUIE SCHIMBAT, IN CE GAMA ESTE PIESA

print()

gama_finala="G" #IN CE GAMA VREI SA FIE TRASPUSA


resulting_song = ""

    
print()

print("------------------------")



for i in range(len(song)):

    if song[i] == " ":
        resulting_song+=' '
    
    if i > 0 and i < len(song) - 1 and song[i - 1] == " " and song[i + 1] == " ":
        for j in range(6):
            #print( game[gama_initiala][j])
            if song[i] == game[gama_initiala][j]:
               a=game[gama_finala][j]
               resulting_song+=a
               
    elif song[i - 1] == " " and song[i + 1] == "m" and song[i+2] == " ":
        for j in range(6):
            #print( game[gama_initiala][j])
            if song[i] == game[gama_initiala][j][0]:
                a=game[gama_finala][j][0]
                resulting_song+=a

    elif song[i - 1] == " " and song[i + 1] == "s" and song[i+2] == "u":
        for j in range(6):
            #print( game[gama_initiala][j])
            if song[i] == game[gama_initiala][j][0]:
               a=game[gama_finala][j][0]
               resulting_song+=a
    elif song[i] != " ": 
        resulting_song+=song[i]
    

print(resulting_song)




        












spatiu()