# Dialogflow demo using IFTTT

This example uses IFTTT as an output from a Dialogflow bot.

In the simple case, using IFTTT is easy. You can create a webhook URL in IFTTT (https://www.ifttt.com/maker_webhooks) and connect that to your Dialogflow bot. However, this will only work if your bot activates only a single action. The reason for this is that each Dialogflow bot can only access a single webhook URL; it places specific details about the selected intent and parameters in the body of the request, but IFTTT cannot access them.

This example allows you to have a single bot that performs multiple IFTTT actions. It does this through a hack, by sending the webhook requests to a web app that I created (http://ifttt-bridge.herokuapp.com). This app references a spreadsheet (http://shaun.cat/ifttt-bridge), which looks at the intent name passed from your Dialogflow app and forwards the request to an IFTTT URL. Yes, this is very hacky.

To set up this example:

1. Import the zip file into Dialogflow
2. Sign up for an IFTTT account.
3. Get your IFTTT webhook URL by going to https://ifttt.com/maker_webhooks and clicking Documentation. Note that you can connect IFTTT to different actions by changing the URL on that page.
4. Create any IFTTT applets you want to use. Note that each should have its own webhook URL.
5. In Dialogflow, set your fulfillment URL to http://ifttt-bridge.herokuapp.com
6. In DialogFlow, give each of your intents a unique name (using the pattern yourname.action), and turn on webhook fulfillment.
7. Go to the spreadsheet at http://shaun.cat/ifttt-bridge. Log in with your CU ID.
8. For each intent in your Dialogflow app, add the intent name to the spreadsheet, along with the IFTTT webhook URL that is unique to your action. Note that your intent name must be unique to the spreadsheet.

Once this is set up, your dialogflow bot should function as normal. When an intent is activated, it will pass a request to the IFTTT bridge app. That app will parse the request for its intent name, look up the IFTTT URL from the spreadsheet, and send a request to that IFTTT URL.