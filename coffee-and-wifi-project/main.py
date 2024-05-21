from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

# Create a new Flask web application instance
app = Flask(__name__)

# Set the secret key for secure session management. This is necessary for Flask-WTF to handle CSRF tokens.
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Initialize Bootstrap5 with the Flask app to use Bootstrap in the templates
Bootstrap5(app)

# Define a WTForms form class for the Cafe form
class CafeForm(FlaskForm):
    # StringField for cafe name with a DataRequired validator
    cafe = StringField('Cafe name', validators=[DataRequired()])
    # StringField for location with DataRequired and URL validators
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    # StringField for opening time with a DataRequired validator
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    # StringField for closing time with a DataRequired validator
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    # SelectField for coffee rating with predefined choices and a DataRequired validator
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    # SelectField for wifi rating with predefined choices and a DataRequired validator
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    # SelectField for power socket availability with predefined choices and a DataRequired validator
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    # Submit button for the form
    submit = SubmitField('Submit')

# Define the route for the homepage
@app.route("/")
def home():
    # Render the index.html template for the homepage
    return render_template("index.html")

# Define the route for adding a new cafe
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    # Create an instance of CafeForm
    form = CafeForm()
    # Check if the form is submitted and validated
    if form.validate_on_submit():
        # Open the CSV file in append mode to add a new cafe
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            # Write the form data to the CSV file
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        # Redirect to the cafes route after form submission
        return redirect(url_for('cafes'))
    # Render the add.html template with the form
    return render_template('add.html', form=form)

# Define the route for displaying the list of cafes
@app.route('/cafes')
def cafes():
    # Open the CSV file in read mode
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        # Read the CSV file data
        csv_data = csv.reader(csv_file, delimiter=',')
        # Create a list to hold all the rows from the CSV file
        list_of_rows = []
        # Append each row from the CSV file to the list
        for row in csv_data:
            list_of_rows.append(row)
    # Render the cafes.html template with the list of cafes
    return render_template('cafes.html', cafes=list_of_rows)

# Check if the script is run directly (and not imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode on port 5002
    app.run(debug=True, port=5002)

