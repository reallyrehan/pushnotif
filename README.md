# PushNotif

[![PyPI version](https://badge.fury.io/py/pushnotif.svg)](https://badge.fury.io/py/pushnotif)

Want to get notified on your phone when your code has executed? This is a simple tool to generate a Push Notification to your IFTTT app.

Now available to download through [PyPi](https://pypi.org/project/pushnotif/).

```
pip install pushnotif
```

## QuickStart

### Setting Up IFTTT Applet

1. Sign up for an [IFTTT account](https://ifttt.com/join).
2. Go to the **[Create](https://ifttt.com/create)** section.
3. Click on **Add** for **If This** and choose *"Webhooks".*
4. Choose the first option for **Receive a web request**.
5. Give this event any name, for example, *"Notifier"*, and click on **Create triger**.
6. Click on **Add** for **Then That** and choose *"Notifications"*.
7. Click on the first option for **Send a notification from the IFTTT app**.
8. Type a message that you want to accompany your notification. Here, you can also add an option for sending variables from runtime when you run code. Click on **Add ingredient** and choose any of the three **Value** variables. You can also use the **EventName** to add the name of the event in the notification and **OccurredAt** to get the time when the event occurred.

<img src = "tutorial/flow.gif">

For example,

#### Message Syntax
```
{{EventName}} : Your Code has executed with message {{Value1}} at {{OccurredAt}}
```
#### Message Output
```
Notifier : Your Code has executed with message "Model Finished Training" at September 9, 2021 at 07:51PM
```
9. Click on **Continue**. Write a Title for your Applet and click on **Finish**.
10. Go to the **[Webhook Documentations](https://ifttt.com/maker_webhooks)** to get your key. You will use this key to intialize your code.
<img src = "tutorial/key.png" style/>

11. Download the IFTTT app for **[Android](https://play.google.com/store/apps/details?id=com.ifttt.ifttt&hl=en_US&gl=US)** | **[iPhone](https://apps.apple.com/us/app/ifttt/id660944635)**

## Execution
```
pip install pushnotif
```

Run the following with your event name (*Step 5*) and key (*Step 10*) that you got when setting up IFTTT,
```
from pushnotif import PushNotif

handler = PushNotif(key = <your_key>, event = <your_event>)

...

model.fit(...)

...

handler.send("Model Trained")
```

You can put the `handler.send()` method at the end of any cell you want to be notified for after execution. 