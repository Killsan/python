import vk_api
import random
import time
token = ''
vk = vk_api.VKApi(token = token)
vk._auth_token()
while True:
    try:
        messages = vk.method('messages.getConcersation', {'offset':0, 'count':20, 'filter':'unanswered'})
        if messages['count'] >= 1:
            id = messages['items'][0]['last_messages']['from_id']
            body = messages['items'][0]['last_messages']['text']
            if body.lower() == 'hi':
                vk.method('messages.send', {'peer_id' : id, 'messages' : 'hello', 'random_id' : random.randint(1,2121212121212)})
            elif body.lower() == 'как дела?':
                vk.method('messages.send', {'peer_id' : id, 'messages' : "it's ok", 'random_id' : random.randint(1,2121212121212)})    
            else:
                vk.method('messages.send', {'peer_id' : id, 'messages' : '...', 'random_id' : random.randint(1,2121212121212)})    
    except Exception as E:
        tine.sleep(1)            