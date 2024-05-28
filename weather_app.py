from app_utils import get_data, StatusCodeException
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def get_weather_data():
    if request.method == 'POST':
        city_name = request.form['location']
        try:
            weather_data = get_data(city_name)
        except StatusCodeException as e:
            return render_template('weather_app_front.html', error=e)
        return render_template('weather_app_front.html', weather_data=weather_data)
    return render_template('weather_app_front.html')


@app.errorhandler(404)
def error_handler(e):
    return render_template('weather_app_front.html', error=e)


if __name__ == '__main__':
    app.run(debug=True)
