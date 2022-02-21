import requests
import yaml
config = yaml.safe_load(open("./config.yml"))


def telegram_bot_sendtext(bot_message):

   bot_token = config.get('bot_token', '')
   bot_chatID = config.get('bot_chatID', '')
   print(bot_chatID)
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot: %s" % "ha ha ha")
print(test)