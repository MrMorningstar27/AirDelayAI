import joblib
import pandas as pd
import sklearn as sk
from pandas.tseries.holiday import USFederalHolidayCalendar
cal = USFederalHolidayCalendar()
from datetime import datetime
# load the model from disk
loaded_model = joblib.load("finalized_model_Air.joblib")
import argparse
parser = argparse.ArgumentParser()



parser.add_argument('date', type=lambda s: datetime.strptime(s, '%d-%m-%Y'),help="Date\nformat: '%d/%m/%Y'")
parser.add_argument('Hour', type=lambda s: datetime.strptime(s, '%H:%M'),help="Hour\nformat: '%H:%M'")
parser.add_argument('Airport', help="Add Airport with 3 letter identificator: LAX/JFK/IAD/MDW")

parser.parse_args()

def main():
    args = parser.parse_args()
    print("Estimated wait time is: {0} minutes".format(predict_delay(args.date,args.Hour,args.Airport)))


def predict_delay(departure_date, departure_time, origin):


    month = departure_date.month
    day = departure_date.day
    day_of_week = departure_date.isoweekday()
    hour = departure_time.hour

    origin = origin.upper()
    holidays = cal.holidays(start=departure_date, end=departure_date).to_pydatetime()
    input = [{
              'Hour': int(hour),
              'Month': int(month),
              'Day of month': int(day),
              'Day of week': int(day_of_week),
              'Airport_LAX': 1 if origin == 'LAX' else 0,
              'Airport_JFK': 1 if origin == 'JFK' else 0,
              'Airport_MDW': 1 if origin == 'MDW' else 0,
              'Airport_IAD': 1 if origin == 'IAD' else 0,
              'Holiday time': 1 if departure_date in holidays else 0}]
    input = pd.DataFrame(input) 
    input["Holiday time"] = input["Holiday time"].astype('category')
    input["Holiday time cat"] = input["Holiday time"]
    input["Hour"] = input["Hour"].astype('category')
    input["Hour cat"] = input["Hour"]
    input["Month"] = input["Month"].astype('category')
    input["Month cat"] = input["Month"]
    input["Day of week"] = input["Day of week"].astype('category')
    input["Day of week cat"] = input["Day of week"]
    input["Day of month"] = input["Day of month"].astype('category')
    input["Day of month cat"] = input["Day of month"]
    print(input)
    return loaded_model.predict(input)[0]















if __name__ == "__main__":
    main()