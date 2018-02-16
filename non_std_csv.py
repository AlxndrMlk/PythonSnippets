# A quick auto-editor for non-standard structured csv file.

import csv
    
    for name in filenames:
        with open (name, 'rb') as f:
            reader = csv.reader(f)

            new_name = 'udated_' + name
            
            with open(new_name, 'wb') as f2:
                writer = csv.writer(f2)
                
                
                for row in reader:
                    
                    n_items = (len(row) - 3) / 5
                    
                    for i in range(n_items):
                        new_row = [row[0], row[1], row[2], row[3+5*i], row[4+5*i], row[5+5*i], row[6+5*i], row[7+5*i]]
                    
                        writer.writerow(new_row)
