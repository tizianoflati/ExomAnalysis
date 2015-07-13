#!/usr/bin/python

# Path al file contenente il risultato del confronto tra due esomi.
# In futuro sara' passato in input
inputFileName = "../comparison/compare1-0.diff.sites_in_files"

# Numero varianti del primo esoma
variants1 = 0

# Numero varianti del secondo esoma
variants2 = 0

# Numero varianti in comune
commonVariants = 0

# Numero varianti in comune a livello di cromosomi
commonChromosomesWithVariants = dict()

# Contatore di linee lette; serve a saltare la prima riga
read = 0

# Ciclo di lettura del file riga-per-riga
with open(inputFileName, 'r') as filePointer:
    for line in filePointer:
        
        # Salta la prima prima
        if read == 0:
            read=read+1
            continue
        
        # Aggiorna il numero di linee lette
        read=read+1
        
        # Divido la linea in campi
        pieces = line.split("\t")
        chromosome = pieces[0]
        pos1 = pieces[1]
        pos2 = pieces[2]
        infile = pieces[3]
        ref1 = pieces[4]
        ref2 = pieces[5]
        alt1 = pieces[6]
        alt2 = pieces[7]
        
        # Variante comune
        if infile == "B":
            variants1 += 1
            variants2 += 1
            commonVariants += 1
            
            # Aggiornamento contatore dei cromosomi con varianti
            if chromosome in commonChromosomesWithVariants:
                commonChromosomesWithVariants[chromosome] += 1
            else:
                commonChromosomesWithVariants[chromosome] = 1
                
        # Variante solo nel primo file
        elif infile == "1":
            variants1 += 1
            
        # Variante solo nel secondo file
        elif infile == "2":
            variants2 += 1
        
print('Finished')
print('Total variants F1: ' + str(variants1))
print('Total variants F2: ' + str(variants2))
print('Common variants: ' + str(commonVariants))
print('Common chromosomes with variants: ' + str(len(commonChromosomesWithVariants)))
