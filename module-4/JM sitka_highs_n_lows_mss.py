import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

def plot_data(dates, temps, color, label, title):
    """Plots the given temperature data."""
    plt.plot(dates, temps, c=color, label=label)

def format_plot(title):
    """Formats the plot with title and labels."""
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.gcf().autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.legend()
    plt.show()

def get_data(filename, temp_type):
    """Retrieves dates and temperature data based on type."""
    dates, temps = [], []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            temp_index = -1
            if temp_type == 'highs':
                temp_index = header_row.index('TMAX')
            elif temp_type == 'lows':
                temp_index = header_row.index('TMIN')

            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    temp = int(row[temp_index])
                    dates.append(current_date)
                    temps.append(temp)
                except (ValueError, IndexError) as e:
                    print(f"Error processing row: {row} - {e}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: '{temp_type.upper()}' data not found in header.")
    return dates, temps


def main():

    while True:
        print("Weather Data Viewer Menu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dates, highs = get_data(filename, 'highs')
            if dates and highs:
                plt.figure(figsize=(10, 6))
                plot_data(dates, highs, 'red', 'Highs', "Daily High Temperatures - 2018")
                format_plot("Daily High Temperatures - 2018")
        elif choice == '2':
            dates, lows = get_data(filename, 'lows')
            if dates and lows:
                plt.figure(figsize=(10, 6))
                plot_data(dates, lows, 'blue', 'Lows', "Daily Low Temperatures - 2018")
                format_plot("Daily Low Temperatures - 2018")
        elif choice == '3':
            print("Exiting Weather Data Viewer. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

