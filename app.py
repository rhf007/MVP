from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to detect user's country
def detect_country(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country = data.get('country', 'Unknown')
        print(f"Detected IP: {ip_address}, Country: {country}")
        return country
    else:
        return 'Unknown'

# Function to get a random photo of the country from Unsplash
def get_random_photo(country):
    url = f"https://api.unsplash.com/photos/random?query={country}&orientation=landscape&client_id=d8eOgjcPTc98Sysa7xJfRXd_BaQZZ3jcF8gRLYTDQWg"
    data = requests.get(url).json()
    if 'urls' in data:
        photo_url = data["urls"]["regular"]
        return photo_url
    else:
        return None

@app.route('/', methods=['GET'])
def get_weather():
    
    return render_template('index.html')

@app.route('/index2', methods=['GET'])
def view_project():
    user_ip = request.remote_addr
    user_country = detect_country(user_ip)
    random_photo = get_random_photo(user_country)
    return render_template('index2.html', random_photo=random_photo)


if __name__ == '__main__':
    app.run(debug=True)