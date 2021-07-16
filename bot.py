import itchatmp
import ziproducer as zipd
itchatmp.config.SERVER_WAIT_TIME = 50
biaoqing_vocab = [v.strip() for v in open('emoji_vocab.txt')]
itchatmp.update_config(itchatmp.WechatConfig(
        token='ltplovelj1314',
            appId = 'wx3420ce9cefb2fb50',
                appSecret = '67e2fc84172d6545c0a59088e2b4571e'))

def delete_last():
        r=itchatmp.messages.batchget_material(itchatmp.content.IMAGE, offset=200, count=5)
        for v in r.get('item',[]):
                print(v)
                itchatmp.messages.delete_material(v['media_id'])
def upload_image(filename):
        delete_last()
        r = itchatmp.messages.upload(itchatmp.content.IMAGE, filename, permanent=True)
        return r['media_id']
def parse_biaoqing(msg):
        strings = msg['Content']
        unit_images =[]
        for i,emoji in enumerate(biaoqing_vocab): 
                if emoji in strings:
                        unit_images.append('images/{}.png'.format(i))
                        strings = strings.replace(emoji,'')
                        print(emoji,strings)
        return unit_images,strings
@itchatmp.msg_register(itchatmp.content.INCOME_MSG)
def reply(msg):
        if msg['MsgType'] == itchatmp.content.TEXT:
                if 1:
                        unit_images,strings = parse_biaoqing(msg)
                        print(unit_images,strings)
                        zipd.build_image(unit_images,strings,size=60)
                        mid = upload_image('images/final.png')
                        return '@img@{}'.format(mid)

                # except:
                #         return "请使用正确的输入，同时包含微信自带表情以及文字"

        
itchatmp.run()
