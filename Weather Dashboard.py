from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests

API_KEY = "194b8b9782611e3759986b504d05bdc6"

class WeatherHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/weather':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            city = data.get('city', '')

            # Fetch weather data from OpenWeatherMap API
            try:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
                response = requests.get(url)
                weather_data = response.json()

                if response.status_code == 200:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        "City": city,
                        "Temperature": weather_data['main']['temp'],
                        "Description": weather_data['weather'][0]['description'],
                        "Humidity": weather_data['main']['humidity']
                    }).encode())
                  
                else:
                    self.send_error(400, message=weather_data.get('message', 'Invalid city'))

            except Exception as e:
                self.send_error(500, message=str(e))

        else:
            self.send_error(404)

if __name__ == '__main__':
    port = 8080
    server_address = ('0.0.0.0', port)
    server = HTTPServer(server_address, WeatherHandler)
    print(f"Server running on http://localhost:{port}")
    server.serve_forever()
