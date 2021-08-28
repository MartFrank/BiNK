#########################
#
# BiNK Python Developer Test
# Martin Franklin 2021
#
#########################

from datetime import datetime

import pprint

DEBUG = 0


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
        current_rent = float(line[-1])
        if DEBUG: print("Current Rent : ", current_rent)
        line[-1] = current_rent
        
        ## convert Lease Years to int
        lease_years = int(line[-2])
        if DEBUG: print("Lease Years : ", lease_years)
        line[-2] = lease_years
        
        ## convert End Date to datetime object 
        end_date = datetime.strptime(line[-3], '%d %b %Y') 
        if DEBUG: print("End Date : ", end_date)
        line[-3] = end_date
        
        ## convert Start Date to datetime object
        start_date = datetime.strptime(line[-4], '%d %b %Y')
        if DEBUG: print("Start Date : ", start_date)
        line[-4] = start_date
                
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
    
    print("Lowest 5 current rents :")
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
    ## filter only the 25 year least row into a new list
    twenty_five = [x for x in data_list if x[-2] == 25]
    
    print("Lease Years = 25 :")
    total_rent = 0.0
    for row in twenty_five:
        total_rent = total_rent + row[-1]
        print(row)
    print("Total rent for 25 year lease : ", total_rent)

def req3(data_list):
    """
    Requirement 3
    
    Create a dictionary containing tenant name and a count of masts for each tenant
        Output the dictionary to the console in a readable form
    
    """
    tenant_masts = {}
    for row in data_list:
        tenant_name = row[-5]
        if tenant_name in tenant_masts:
            tenant_masts[tenant_name] = tenant_masts[tenant_name] + 1
        else:
            tenant_masts[tenant_name] = 1
    print("Tenant Name & Mast Count : ")
    pprint.pprint(tenant_masts)


def req4(data_list):
    """
    Requirement 4

    List the data for rentals with Lease Start Date between 1st June 1999 and 31st August 2007
        Output the data to the console with dates formatted as DD/MM/YYYY
        
    """
    early_date = datetime(1999, 6, 1)
    later_date = datetime(2007, 8, 31)
    
    
    ## filter only those with date inside the wanted  range
    wanted_date = [x for x in data_list if x[-4] > early_date and x[-4] < later_date ]
    
    for row in wanted_date:
        ## show the dates some formatting
        row[-4] = row[-4].strftime("%d/%m/%Y")
        row[-3] = row[-3].strftime("%d/%m/%Y")
        print(row)




if __name__=="__main__":
    ## N.B..Must haves & extras
    #~ Demonstrate usage of list comprehension for at least one of the tasks
    #~ Allow user input to run all of your script, or specific sections
    #~ multiple variations of Tenant Name - treat these as individual tenants.

    
    data_list = read_data("Python Developer Test Dataset.csv")
    
    ## call them all  
    #~ req1(data_list)
    #~ req2(data_list)
    #~ req3(data_list)
    req4(data_list)




