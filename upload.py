import itchatmp

itchatmp.update_config(itchatmp.WechatConfig(
        token='ltplovelj1314',
            appId = 'wx3420ce9cefb2fb50',
                appSecret = '67e2fc84172d6545c0a59088e2b4571e'))
# with open('emoji_media_id.txt','w') as f:
#     for i in range(109):
#         r = itchatmp.messages.upload(itchatmp.content.IMAGE, 'images/{}.png'.format(i), permanent=True)
#         f.write(r['media_id']+'\n')
#         f.flush()
r = itchatmp.messages.get_material_count()
print(r)
r = itchatmp.messages.batchget_material(itchatmp.content.IMAGE, offset=100, count=r['image_count'])
print(len(r['item']))