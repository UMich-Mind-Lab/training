# Getting data from Google Sheets

This assumes that you already have the API key created and in
place in `~/gsheet_api/gsheet_client.json`.  That directory and
file should only be readable by you; that is, you should

```
$ chmod -R go-rwx ~/gsheet_api
```

We always start by importing needed libraries.

```python
import os
# for google sheets API
import gspread
# the following for authenticating google sheet id
from oauth2client.service_account import ServiceAccountCredentials
```

Uses gspread and oauth to get a client connection to a Google
spreadsheet (Excel workbook), which may contain multiple
worksheets (Excel spreadsheet)

```python
def get_wb(wb_name):
    # get credentials from file
    tokenDir = os.path.join(os.path.expanduser('~'),
                            'gsheet_api','gsheet_client.json')
    print("tokenDir is: ", tokenDir)
    #set up API to talk to google
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(tokenDir,scope)
    # Read the credentials to use for authorization
    client = gspread.authorize(creds)
    # Open the workbook connection
    wb = client.open(wb_name)
    return wb

# End of function
print("end function def")
```

We will look at the 'MTwiNS fMRI Report' Google Sheets workbook.
```python
wb = get_wb('MTwiNS fMRI Report')
```

Within the workbook, we want the spreadsheet for Wave 3

```python
ws = wb.worksheet('Wave3')
```


Start by getting the worksheet as a list of lists

```python
list_data = ws.get_all_values()
```

To get specific columns, you use indexes, i.e., the numeric position
First three rows.  This is a 'list slice'.

```python
print(list_data[:3])
```

Print the values of just twinID, fmri_complete, and mriFolder for only the
first three rows.

```python
for twin in list_data[:3]:
    print(twin[1], twin[16], twin[31])
```

Can also get the worksheet as a list of dictionaries
```python
dict_data = ws.get_all_records()
```

Print the key values for the first record; keys are column names, and
in this structure are repeated for each participant.  This selects
first item from the list dict_data, then from that, it uses .keys()
to get the list of keys.

```python
print(dict_data[0].keys())
```

Print the first three full records

```python
printdict_data[:3])
```

Print the values of just twinID, fmri_complete, and mriFolder for only the
first three rows.

```python
for twin in dict_data[:3]:
    print(twin['twinID'], twin['fmri_complete'], twin['mriFolder'])
```
