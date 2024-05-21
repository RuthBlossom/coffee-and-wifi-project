Coffee and Wifi

## Overview

Coffee and Wifi is a web application built with Flask that helps users find cafes equipped with essential amenities for remote work. Users can contribute by adding new cafes 
and view a comprehensive list of cafes with ratings for coffee quality, WiFi strength, and power socket availability. 
The application leverages Bootstrap for responsive design and WTForms for robust form handling.


## Features

- **Add New Cafes**: Users can add new cafes by providing details such as name, location, opening and closing times, coffee rating, WiFi strength, and power socket availability.
- **View Cafes List**: Displays a list of all cafes with the provided details, allowing users to easily find suitable locations for remote work.
- **Responsive Design**: Utilizes Bootstrap for a responsive and mobile-friendly interface.

## Technologies Used

- **Python**
- **Flask**
- **Flask-Bootstrap**
- **Flask-WTF**
- **WTForms**
- **CSV** for data storage

## Installation

Follow these steps to get a local copy of the project up and running:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RuthBlossom/coffee-and-wifi.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd coffee-and-wifi
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application**:
   ```bash
   python main.py
   ```

2. **Open your web browser and go to** `http://127.0.0.1:5002`.


## Acknowledgements

- **Bootstrap**: For providing the responsive design framework.
- **Flask-WTF** and **WTForms**: For form handling and validation.
- **Font Awesome**: For the coffee and wifi icons used in the project.


Thank you for checking out Coffee and Wifi! Enjoy finding and sharing the best cafes for remote work.
