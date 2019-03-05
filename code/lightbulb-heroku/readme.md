# Dialogflow demo using Heroku

This Dialogflow example connects to a web app running on the Heroku service. This demonstrates how to parse Dialogflow's webhook requests using Python (via the Flask library) and to act on those requests - in this case, by setting values in a Redis database.

To set up this example:

1. Import the zip file into Dialogflow
2. Deploy the python app to Heroku. See app.py for details. You will also need to attach a free Redis db to your Heroku instance.
3. In your Dialogflow project, set the fulfillment URL to YOUR_HEROKU_URL/dialog
