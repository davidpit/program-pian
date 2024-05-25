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


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

input_text = """           G      C     G 
1. Doamne vin și-ngenunchez,

       Em   D     C 
   Ție îți mărturisesc:

        G    C    G 
   Fără Tine aș cădea,

           Em    D      C 
   Doar Tu ești odihna mea.



             G   C  G  D 
R:    Eu de Tine am nevoie,

      Em   C    G  D 
      Am nevoie mare, 

         G/B      C  G/D    C 
      Tu ești neprihănirea mea

           G/D    D  G 
      Și-a mea apărare.
"""

print(input_text)

toneOfTheSong="G"     #CHANGE RIGHT HERE

toneToBeChanged="C"

output_text=input_text

for i in range(10):
    output_text=output_text.replace(numbers[i]," ")



input_text=output_text

for i in range(6):
        
    #print(i)
    # Check if "Bm" is present in the input text
    

    if game[toneOfTheSong][i] in input_text:
        # Replace "Bm" with "F#m"
        #print(game[toneOfTheSong][i], " ",game[toneToBeChanged][i] )

        output_text = input_text.replace(game[toneOfTheSong][i], numbers[i])
        input_text=output_text
        #print(output_text)



for i in range(6):

    output_text = output_text.replace(numbers[i], game[toneToBeChanged][i])
print("---------------------------------------")
print(output_text)


#SA DAM REMOVE LA NUMERE, NUMERELE LE FACEM STELUTE

