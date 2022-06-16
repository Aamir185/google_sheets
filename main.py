import  SheetsAPI as gs

if __name__ == '__main__':
    sheet_id = '1BmU3UDGNPEjtw-mGOBmc2vJDBnX0SL4kjVBPB5nP_Ho'
    range = 'Commercial_Mart!A1:G72'  # Commercial Mart

    df = gs.get_sheet_data(sheet_id, range)

    print(df)

    exit(1)