from app_utils import get_data, StatusCodeException
from flask import Flask, request, render_template
import logging


app = Flask(__name__)
app.logger.setLevel(logging.INFO)  # Set log level to INFO
handler = logging.FileHandler('./logs/app.log')  # Log to a file
app.logger.addHandler(handler)


@app.route("/", methods=['GET', 'POST'])
def get_weather_data():
    if request.method == 'POST':
        city_name = request.form['location']
        app.logger.info(f"{city_name} was searched")
        try:
            weather_data = get_data(city_name)
        except StatusCodeException as e:
            app.logger.error('This is an error message')
            return render_template('weather_app_front.html', error=e)
        return render_template('weather_app_front.html', weather_data=weather_data)
    return render_template('weather_app_front.html')


@app.errorhandler(404)
def error_handler(e):
    return render_template('weather_app_front.html', error=e)


if __name__ == '__main__':
    app.run(debug=True)
