# Importing Flask and other required modules
from flask import Flask, render_template, request, url_for
import requests


# Creating a Flask application instance
app = Flask(__name__)

# Define the route for the root URL
@app.route('/', methods=["GET", "POST"])
def index():
    # Render the homepage
    return render_template("index.html")

# Summarization endpoint
@app.route("/Summarization", methods=["GET", "POST"])
def Summarize():
    # API details
    if request.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": "Bearer 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"}

        # Data from user input
        data = request.form["data"]

        # Summary length (you can allow these to be input by the user in future)
        
        maxL = int(request.form["MaxL"])
        minL=maxL//4
        # Function to make API call
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        # Get the output from the API
        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},
        })[0]
        
        # Render the template with the result
        return render_template("index.html", result=output["summary_text"])

    # If GET request, render the form
    return render_template("index.html")

# Main driver function
if __name__ == '__main__':
    app.debug = True
    app.run()
