#########################
#
# BiNK Python Developer Test
# Martin Franklin 2021
#
#########################

import datetime

import csv

import pprint


## open the file and slurp it into a csv dict per row for use later.. or not
## this must run first for all requirements regardless, so keep it top level
with open('BiNK.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Property Name'])





## req 1
#~ Read in the attached file
#~      Produce a list sorted by “Current Rent” in ascending order
#~      Obtain the first 5 items from the resultant list and output to the console



## req 2
#~ From the list of all mast data, create a new list of mast data with “Lease Years” = 25 years.
    #~ Output the list to the console, including all data fields
    #~ Output the total rent for all items in this list to the console



## req 3
#~ Create a dictionary containing tenant name and a count of masts for each tenant
    #~ Output the dictionary to the console in a readable form


## req 4
#~ List the data for rentals with “Lease Start Date” between 1st June 1999 and 31st August 2007
    #~ Output the data to the console with dates formatted as DD/MM/YYYY



## N.B..Must haves & extras
#~ Demonstrate usage of list comprehension for at least one of the tasks
#~ Allow user input to run all of your script, or specific sections
#~ multiple variations of Tenant Name – treat these as individual tenants.