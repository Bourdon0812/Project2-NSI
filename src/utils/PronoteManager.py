import csv

def importCsv():
    table = []
    #csv.reader(open('csv_files/sample.csv', 'rU'), delimiter=",", quotechar='|')
    with open('resultatVF.csv') as csvfile:  # ouverture du fichier csv
        lecture_fichier_csv = csv.reader(csvfile,delimiter=',')  # stockage dans la variable lecture_fichier_csv avec délimiteur "virgule"
        for ligne in lecture_fichier_csv:
            table.append(ligne)
    return(table)

table=importCsv()

def moyenneDevoirs(notes:dict) -> tuple:
    dict={}
    moyenneDS1=0
    moyenneDS2=0
    moyenneDS3=0
    moyenneDS4=0
    moyenneDS5=0
    for i in range(1,len(notes)):
        moyenneDS1+=int(notes[i][2])
        moyenneDS2+=int(notes[i][3])
        moyenneDS3+=int(notes[i][4])
        moyenneDS4+=int(notes[i][5])
        moyenneDS5+=int(notes[i][6])
    dict["DS1"]=round(moyenneDS1/len(notes),2)
    dict["DS2"]=round(moyenneDS2/len(notes),2)
    dict["DS3"]=round(moyenneDS3/len(notes),2)
    dict["DS4"]=round(moyenneDS4/len(notes),2)
    dict["DS5"]=round(moyenneDS5/len(notes),2)
    return(dict)

def moyenneEleves(notes:dict) -> dict:
    moyenneEleves=[]
    for i in range(1,len(notes)):
        temp_dict={}
        temp_dict["Nom"]=notes[i][0]
        temp_dict["Prénom"]=notes[i][1]
        temp_dict["Moyenne"]=(int(notes[i][2])+int(notes[i][3])+int(notes[i][4])+int(notes[i][5])+int(notes[i][6]))/5
        moyenneEleves.append(temp_dict)
    return(moyenneEleves)


def moyennesDecroissant(notes:dict) -> list:
    moyennes=moyenneEleves(notes)
    moyennesDecroissant=[]
    for i in range(len(moyennes)):
        moyennesDecroissant.append([moyennes[i]["Nom"],moyennes[i]["Moyenne"]])
    moyennesDecroissant=annexeTri(moyennesDecroissant)
    return(moyennesDecroissant)

def annexeTri(l:list) -> list:
    n=len(l)
    for i in range(0,n-1):
        indexminimum=i
        for j in range(i+1,n):
            if l[j]<l[indexminimum]:
                indexminimum=j
        if indexminimum != i:
            l[i], l[indexminimum] = l[indexminimum], l[i]
    return(l)