from werobot import WeRoBot
from werobot.replies import ImageReply
import ziproducer as zipd
robot = WeRoBot(token='ltplovelj1314')
robot.config["APP_ID"] = "wx3420ce9cefb2fb50"
robot.config["APP_SECRET"] = "67e2fc84172d6545c0a59088e2b4571e"
robot.config['HOST'] = '192.168.0.201'
robot.config['PORT'] = 80
biaoqing_vocab = [v.strip() for v in open('emoji_vocab.txt')]
client = robot.client
# client.create_menu({
#     "button":[{
#          "type": "click",
#          "name": "表情拼字",
#          "key": "pingzi"
#     }]
# })


def delete_last():
    r=client.get_media_list('image', offset=200, count=5)
    for v in r.get('item',[]):
        print(v)
        client.delete_permanent_media(v['media_id'])
def upload_image(filename):
    delete_last()
    r = client.upload_permanent_media('image', open(filename,'rb'))
    return r['media_id']
def parse_biaoqing(msg):
    strings = msg.content
    unit_images =[]
    for i,emoji in enumerate(biaoqing_vocab): 
        if emoji in strings:
            unit_images.append('images/{}.png'.format(i))
            strings = strings.replace(emoji,'')
    return unit_images,strings
@robot.text
def reply(msg):
    print(msg)    
    unit_images,strings = parse_biaoqing(msg)
    zipd.build_image(unit_images,strings,size=60)
    mid = upload_image('images/final.png')                        
    return  ImageReply(msg,media_id=mid)










# 让服务器监听在 0.0.0.0:80

robot.run()