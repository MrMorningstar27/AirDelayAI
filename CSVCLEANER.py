from csv import *

with open('out.csv') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

    for x in range(len(list_of_rows)):
        for y in range(2,6):
            if list_of_rows[x][y] == "0":
                print(list_of_rows[x])
                #remove lines
                list_of_rows[x] = []
                pass
    #write lines with normal format
    with open("out.csv", "w", newline="") as f:
        writer = writer(f)
        for row in list_of_rows:
            if(row != []):
                writer.writerow(row)