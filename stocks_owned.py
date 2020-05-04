
#https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/

from csv import writer
 
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

row_contents = [32,'Shaun','Java','Tokyo','Morning']

append_list_as_row('students.csv', row_contents)
