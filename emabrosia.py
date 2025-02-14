# echo "# eAmbrosia" >> README.md
#git init
#git add README.md
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/victorsole/eAmbrosia.git
#git push -u origin main

# Install necessary libraries
# pip install requests flask

from flask import Flask, jsonify, request
import requests

app = Flask("Bo")

# Define the route to fetch data from the eAmbrosia API
@app.route('/api/geographical-indications', methods=['GET'])
def get_geographical_indications():
    # Define the eAmbrosia API endpoint
    eambrosia_url = 'https://webgate.ec.europa.eu/eambrosia-api/api/v1/geographical-indications'

    # Extract query parameters from the incoming request
    modified_on_from = request.args.get('modifiedOnFrom', '2020-01-01T00:00:00.000Z')
    modified_on_to = request.args.get('modifiedOnTo', '2022-03-30T23:59:59.000Z')

    # Add parameters to the eAmbrosia API call
    params = {
        'modifiedOnFrom': modified_on_from,
        'modifiedOnTo': modified_on_to
    }

    # Send a GET request to the eAmbrosia API
    try:
        response = requests.get(eambrosia_url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        json_data = response.json()
        return jsonify(json_data)  # Send the JSON response to the frontend
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

