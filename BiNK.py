#########################
#
# BiNK Python Developer Test
# Martin Franklin 2021
#
#########################

from datetime import datetime

import pprint


def read_data(filename):
    """
    Read the given csv file and reetunb a list object with the columns typed for use
    """
    fin = open(filename, "rt")
    ## skip header
    fin.readline()

    ## slurp it all in
    data_list = []
    for line in fin.readlines():
        ## split the line on comma 
        line = line.split(",")
        
        # convert Current Rent to float for sorting etc
        line[-1] = float(line[-1])
        
        ## convert Lease Years to int
        line[-2] = int(line[-2])
        
        ## convert Start Date to datetime object
        line[-3] = datetime.strptime(line[-3], '%d %b %Y')
        
        ## convert End Date to datetime object (02 Aug 2019 == 
        line[-4] = datetime.strptime(line[-4], '%d %b %Y')
        
        ## append this line into the data_list 
        data_list.append(line)
    return data_list



def req1(data_list):
    """
    Requirement 1
    Read in the attached file
        Produce a list sorted by Current Rent in ascending order
        Obtain the first 5 items from the resultant list and output to the console
    """
    ## sort it by Current Rent (the last column)
    index_number = -1
    sorted_data = sorted(data_list, key=lambda x:x[index_number]) 
    
    ## print the top 5
    for row in sorted_data[:5]:
        print(row)


def req2(data_list):
    """
    Requirement 2
    From the list of all mast data, create a new list of mast data with Lease Years = 25 years.
        Output the list to the console, including all data fields
        Output the total rent for all items in this list to the console
    """
    pass

def req3(data_list):
    """
    Requirement 3
    Create a dictionary containing tenant name and a count of masts for each tenant
        Output the dictionary to the console in a readable form
    """
    pass

## req 4
#~ List the data for rentals with Lease Start Date between 1st June 1999 and 31st August 2007
    #~ Output the data to the console with dates formatted as DD/MM/YYYY




if __name__=="__main__":
    ## N.B..Must haves & extras
    #~ Demonstrate usage of list comprehension for at least one of the tasks
    #~ Allow user input to run all of your script, or specific sections
    #~ multiple variations of Tenant Name - treat these as individual tenants.

    
    data_list = read_data("Python Developer Test Dataset.csv")
    
    ## call them all  
    req1(data_list)


    req2(data_list)




