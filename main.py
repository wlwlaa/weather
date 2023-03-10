import requests


def main():
    START_URL = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=c308c34844dc547a013d1f330c5a58c7'
    CITY = input('Введите город: ')
    url = START_URL + '&q=' + CITY

    response = requests.get(url).json()

    current_inf = response['list'][0]['main']
    temp = round(current_inf['temp'] - 273)
    temp_feels_like = round(current_inf['feels_like'] - 273)
    pressure = round(current_inf['pressure'] // 10 * 7.537)
    humidity = current_inf['humidity']

    print(f"Температура: {temp} С, ощущается как {temp_feels_like} С")
    print(f"Давление: {pressure} мм. рт. ст.")
    print(f"Влажность: {humidity}%")

    weather_inf = response['list'][0]['weather'][0]['description']
    weather_state = {
        'clear sky': 'ясно', 
        'fog': 'туман', 
        'scattered clouds': 'переменная облачность', 
        'light rain': 'легкий дождь', 
        'few clouds': 'облачно', 
        'moderate rain': 'дождь', 
        'heavy intensity rain': 'сильный дождь', 
        'rain and snow': 'дождь со снегом', 
        'snow': 'снег', 
        'light snow': 'легкий снег', 
        'overcast clouds': 'пасмурно', 
        'broken clouds': 'малооблачно'
    }
    
    if weather_inf in weather_state:
        print(f"Состояние неба: {weather_state[weather_inf]}")
    else:
        print(f"Состояние неба: {weather_inf}")

    print('\n')

    print("Прогноз на следующие часы:")
    current_inf = response['list'][4]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][4]['weather'][0]['description']
    print(f"Прогноз на {response['list'][4]['dt_txt']}: температура: {temp} С, {weather_state[weather_inf]}")

    current_inf = response['list'][6]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][6]['weather'][0]['description']
    print(f"Прогноз на {response['list'][6]['dt_txt']}: температура: {temp} С, {weather_state[weather_inf]}")

    current_inf = response['list'][8]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][8]['weather'][0]['description']
    print(f"Прогноз на {response['list'][8]['dt_txt']}: температура: {temp} С, {weather_state[weather_inf]}")

    current_inf = response['list'][10]['main']
    temp = round(current_inf['temp'] - 273)
    weather_inf = response['list'][10]['weather'][0]['description']
    print(f"Прогноз на {response['list'][10]['dt_txt']}: температура: {temp} С, {weather_state[weather_inf]}")
    

if __name__ == '__main__':
    main()
