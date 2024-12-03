import datetime
import nselib
from nselib import capital_market

def get_weekdays(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.datetime.strptime(end_date, '%d-%m-%Y')

    weekdays = []
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() not in [5, 6]:  # Exclude Saturday and Sunday
            weekdays.append(current_date.strftime('%d-%m-%Y'))
        current_date += datetime.timedelta(days=1)

    return weekdays


def save_bhav_copy_to_csv(date):
  bhav_data = capital_market.bhav_copy_with_delivery(date)
  import pandas as pd
  df = pd.DataFrame(bhav_data)

  # Save the DataFrame to a CSV file
  filename = f"bhavcopy_{date}.csv"
  df.to_csv(filename, index=False)

start_date = '01-01-2024'
end_date = '21-11-2024'
weekday_dates = get_weekdays(start_date, end_date)
# Example usage:
for date in weekday_dates:
  save_bhav_copy_to_csv(date)
