#! python3
# removecsvheader.py - remove the header from all CSV files in the current working directory

import csv, os
os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.

for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue	# Skip non csv files.

	print ('Removing header from ' + csvFilename + '...')

# Read the CSV file in (skipping first row).

csvRows = []
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
	if readerObj.line_num == 1:
		continue	# Skip first row.
	csvRows.append(row)
csvFileObj.close()

# Write out csv file.

csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
	newline = '')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
	csvWriter.writerow(row)
csvFileObj.close()
