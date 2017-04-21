# my_wechat_robot
itchat tuling robot wechat auto-google-translate 
I only try python2.7, I think it also can run on python3

hello, everyone. This is my little wechat robot using tuling123 robot[http://www.tuling123.com/] and itchat[https://pypi.python.org/pypi/itchat/1.3.5]. I add auto google-translate in my code. And you can add anything you want. By using python subprocess to run other program, or custom your own features.

some dependencies as follows:

requests -- use request to send message to robot API and receive the response

itchat -- python2

guess_language -- use to judge the message received is chinese or english for google translate(In my code, I only deal with the two languages, other languages are supported by robot)

mtranslate -- MIT python package for imitate browser to visit translate.google.com

You can install it easily by:

pip install [package-name]

for guess_language, "pip install guess_language" has some problems in my Ubuntu 16.04 server. The alternative choice is pip install from guess_language package source site.

In code, I deal with two language, it seems a little Redundant, but the text in py file can be deleted and modified.

Useful comments are contained in the py code. Hope your wechat more colorful!

Ultimate reminder: when you run the py code and it runs correctly, you will see a big QR graph for your phone wechat to scan to log in. If you don't use black background and white font color, the QR graph is strange and not useable.
