from bs4 import BeautifulSoup as bs
import requests
from datetime import date
import os.path
import pandas as pd

Airports = ["GUM", "ATL", "AUS", "BWI", "BOS", "CLT", "MDW", "ORD", "CVG", "DFW", "DEN", "DTW", "FLL", "FAT", "HNL", "IAH", "SNA", "ONT", "STL", "LAX", "SGU", "LAS", "OAK", "MIA", "JFK", "MSP", "EWR", "SJC", "MCO", "SFB", "PBI", "PHL", "PHX", "PDX", "RDU", "SMF", "SPN", "SAT", "SLC", "SAN", "SAO", "SEA", "TPA", "IAD"]
def main():
    BaseParsingURL = "https://awt.cbp.gov"
    BaseString = "/Home/OpenExcel?port={0}&rptFrom={1}&rptTo={2}"
    DateFormat = "{0}/{1}/{2}"
    today = date.today()
    day = today.strftime("%d")
    month = today.strftime("%m")
    for year in range(2009,2020)[::-1]:
        for Airport in Airports:
            print(BaseParsingURL+BaseString.format(Airport,DateFormat.format(month,day,year),DateFormat.format(month,day,year+1)))
            html = requests.post(BaseParsingURL+BaseString.format(Airport,DateFormat.format(month,day,year),DateFormat.format(month,day,year+1)))
            ParseToCSV(html.text)
            print("parsed")
            
        
def ParseToCSV(html_string):
    
    df = pd.read_html(html_string, header=0)[0]
    #print(df)
    with open("Output.csv", 'a') as f:
        df.to_csv(f, header=f.tell()==0)





if __name__ == "__main__":
    main()