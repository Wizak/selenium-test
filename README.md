# Selenium-Test
Example, how selenium works with scraping website.
---
## Step 1
As example ChromeDriver that responds your browser and browser version.
Copy file to your work directory.
```
https://chromedriver.chromium.org/downloads
```
## Step 2
Install selenium lib with pip into your python venv.
```
python -m venv venv
venv\Scripts\Activate
pip install selenium
```
## Step 3
Run python script.
```
python main.py
```
## Step 4
Check result in chatbot_list.json.
```json
{
   "Telegram": "https://t.me/Diia_help_bot?start=X3VybD0lMkZsaW5rJmQ9Mg",
   "Viber": "viber://pa?chatURI=diia_help_bot&context=X3VybD0lMkZsaW5rJmQ9Mg==",
   "Messenger": "https://m.me/105597857511240?ref=X3VybD0lMkZsaW5rJmQ9Mg=="
}
```
