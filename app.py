from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Define a function to calculate the carbon footprint based on user inputs
def calculate_carbon_footprint(miles_driven, mpg, electricity_usage, gas_bill):
    # Calculate the carbon footprint from transportation
    carbon_footprint_transportation = (miles_driven / mpg) * 19.6
    # Calculate the carbon footprint from electricity usage
    carbon_footprint_electricity = electricity_usage * 1.37
    # Calculate the carbon footprint from natural gas usage
    carbon_footprint_gas = gas_bill * 12.2
    # Calculate the total carbon footprint
    total_carbon_footprint = carbon_footprint_transportation + carbon_footprint_electricity + carbon_footprint_gas
    return total_carbon_footprint

# Define a function to plot the user's carbon footprint over time
def plot_carbon_footprint(df):
    plt.plot(df['Date'], df['Carbon Footprint'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Carbon Footprint (metric tons)')
    plt.title('Carbon Footprint over Time')
    plt.show()

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for the results page
@app.route('/results', methods=['POST'])
def results():
    miles_driven = float(request.form['miles_driven'])
    mpg = float(request.form['mpg'])
    electricity_usage = float(request.form['electricity_usage'])
    gas_bill = float(request.form['gas_bill'])

    # Calculate the carbon footprint and print the result
    carbon_footprint = calculate_carbon_footprint(miles_driven, mpg, electricity_usage, gas_bill)
    print("Your carbon footprint for the past month is: {:.2f} metric tons".format(carbon_footprint))

    # Store the date and carbon footprint in a DataFrame
    df = pd.DataFrame({'Date': [pd.Timestamp.now().strftime('%Y-%m-%d')], 'Carbon Footprint': [carbon_footprint]})

    # Plot the user's carbon footprint over time
    plot_carbon_footprint(df)

    # Return
