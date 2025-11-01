import requests

API_KEY = ''  # Enter your OpenWeatherMap API key here

def get_weather(city):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    
    response =requests.get(url)
    data = response.json()

    return data



def show_weather(data , city):
    
    print(data)

    if data['cod'] =='404':
        print (f'City not found!')

    else :

        print(f"\nWeather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind: {data['wind']['speed']} Km/h")


def main():

    city = input('Enter city name:')
    data = get_weather(city)
    show_weather(data,  city)


if __name__ == '__main__':
    main()