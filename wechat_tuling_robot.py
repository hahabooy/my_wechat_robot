#coding=utf8
import requests
import itchat
from guess_language import guessLanguage
import os.path
from mtranslate import translate

today = 'reply_listDB' # use today as a file to store the list of friends who start the service of your robot.
if not os.path.exists(today): # if file not exist, create it.
    open(today, 'a').close()
with open(today) as f:
    content = f.readlines()
replylist = [x.strip() for x in content] # everytime restart read today file to restore the listof friends who start the service of your robot.
KEY = '0d816cc4b4b74cca837ed2318ad87198' # the API key of robot from [http://www.tuling123.com/]
def get_response(msg): # contact your robot through API
    apiUrl = 'http://www.tuling123.com/openapi/api' # the API address of robot from [http://www.tuling123.com/]
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    except:
        return

def write_replyDB(): # if friends open the service or close the service, rewrite today file
    with open(today, 'w'): pass
    with open(today, 'w') as f_today:
        for person in replylist:
            f_today.write("%s\n" % person)
        f_today.close()

def special_function(text): # special features you can add, here I add google-translate, by use '#' before the message send to me
    if len(text) <20: # if short than 20, then do feature identify, and give detailed query way.
        if u'google' in text or u'谷歌' in text:
            return u'Please put "#" and the language you want to transfer, "#en" or "#zh", before the text you want to translate, only support chinese and english. for example, \n you can also let me know which language you want by, for example, \n"#en 你还好么" will return "are you right?"\n"#zh are you right?" will return "你还好么"'
    # elif ... #other special uses
    # else:
    #     return 0
    if text[0] == u'#': # #means 'google translate'
        des_lang = 'en' if u'en' in text[1:4] else'zh-CN'
        # a = text[3:].encode('utf8')
        ans = '暂时无法连接translate.google, sorry about that.'
        try:
            ans = translate(text[3:].encode('utf8','ignore'), des_lang)
        except:
            pass
        return ans

@itchat.msg_register(itchat.content.TEXT)

def tuling_reply(msg): # the main function used for message processing
    #print(msg)
    #print(msg["User"].split(",")[0].split(":")[2])
    #(msg["FromUserName"]=="@d57c5b7f0fff1374fa5b38594ec49362")
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    # 如果图灵Key出现问题，那么reply将会是None
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    lang = guessLanguage(msg["Text"]) # guess the language type and give different response

    sender_alias = msg['User']['Alias'] # the unique id of senders(wechat users), attention: the FromUserId or something is not unique, which changes nexttime you log in.
    if lang == 'en': # is the message type is english
        first_greetings_EN = u"Hello, I'm xiaobo belonging to Zhenbo Xu, may I help you? If it's a emergency, please contact my owner by phone call or SMS. I can chat with you if you want, send <start> to begin and send <stop> to shut me down."
        defaultReply_EN = u'OMG, this question stumped me. Could you please wait for my master?'
        if msg["Text"] == "start": # start the service
            if sender_alias not in replylist:
                replylist.append(sender_alias) # add sender alias
                write_replyDB() #write to the file
            return u'xiaobo auto reply started' # notification send back to the sender
        elif msg["Text"] == "stop": # stop the service
            replylist.remove(sender_alias)
            write_replyDB()
            return u'xiaobo auto reply stopped'
        if sender_alias in replylist: # if the user in the list of who started the service, then process it 
            special_reply = special_function(msg["Text"]) # the features added
            if special_reply:
                return special_reply
            return get_response(msg['Text']) or defaultReply_EN  #if not satisfy self-defined features, send it to your robot by get_response(). And if no response from the robot, send the default reply.
        else:
            return first_greetings_EN # there is indeed a problem that everytime someone send you a message, he will receive the greeting from the robot. It can be sloved by add a flag to the today file, or another file to store the state.
    else:#默认为中文
        first_greetings_CN = u'嘿，我是徐振博家的小机器人小博，有什么可以帮助您的么.有急事请通过短信或者电话联系主人。我可以和您聊天，发送<开始>两个字就可以啦，发送<关闭>可以把烦人的我关掉。现在我会自动谷歌翻译,查天气,歇后语,查邮编查公交>等等。另外,如果有个功能您特别想要，可以联系我主人实现一下'
        defaultReply_CN = u'那个，这个机器人不会回答这个问题，不过他会谷歌翻译（回复<谷歌>查看详细信息）,输地名查天气,查单词,歇后语,查邮编查公交等等。另外,如果有个功能您特别想要，可以联系我，我有空实现一下'
        if msg["Text"] == u'开始':
            if sender_alias not in replylist:
                replylist.append(sender_alias)
                write_replyDB()
            return u'小博自动回复已开启'
        elif msg["Text"] == u'关闭':
            replylist.remove(sender_alias)
            write_replyDB()
            return u'小博自动回复已关闭'
        if sender_alias in replylist:
            special_reply = special_function(msg["Text"])
            if special_reply:
                return special_reply
            return get_response(msg['Text']) or defaultReply_CN  # .decode('unicode-escape')
        else:
            return first_greetings_CN

# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.run()
                                                                                                                                                                                                                            108,1         Bot
