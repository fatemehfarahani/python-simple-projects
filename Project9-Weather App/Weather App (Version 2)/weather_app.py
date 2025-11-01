from flask import Flask , render_template , request
import requests

app = Flask (__name__)

API_KEY = ''  # Enter your OpenWeatherMap API key here

@app.route('/' , methods=['GET' ,'POST'])

def home():
    
    weather= None

    if request.method =='POST':

        city = request.form['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'

        response = requests.get(url)
        data = response.json()


        if data['cod'] == 200:
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed']
            }
        else:
            weather = {'error': 'City not found!'}

    return render_template('index.html', weather=weather)
    



if __name__ == '__main__':
    app.run(debug=True)
