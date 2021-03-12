import csv

#arquivo csv salvo no meu pc
with open('names.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter = '\t')
    # for line in csv_reader:
    #     print(line)

    #dicionario
    # csv_reader = csv.DictReader(csv_file)
    # for line in csv_reader:
    #         print(line)


    # with open('new_nomes.cvs','w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')
    #
    #     for line in csv_reader:
    #         csv_writer.writerow(line)

    csv_reader = csv.DictReader(csv_file)
    with open('new_nomes.csv', 'w') as new_file:
            fieldnames = ['Nome', 'Sobrenome']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='-')

            csv_writer.writeheader()
            for line in csv_reader:
                del line['email']
                csv_writer.writerow(line)