import csv

def importCsv():
    table = []
    #csv.reader(open('csv_files/sample.csv', 'rU'), delimiter=",", quotechar='|')
    with open('resultatVF.csv') as csvfile:  # ouverture du fichier csv
        lecture_fichier_csv = csv.reader(csvfile,delimiter=',')  # stockage dans la variable lecture_fichier_csv avec délimiteur "virgule"
        for ligne in lecture_fichier_csv:
            table.append(ligne)
    print(table)


importCsv()