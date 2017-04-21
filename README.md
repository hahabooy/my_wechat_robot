# my_wechat_robot
**Key word: itchat tuling robot wechat auto-google-translate **

I only try *python2.7*, but those packages all avaliable on python3


hello, everyone. This is my little wechat robot using tuling123 robot[http://www.tuling123.com/] and itchat[https://pypi.python.org/pypi/itchat/1.3.5]. I add auto google-translate in my code. And you can add anything you want. By using python subprocess to run other program, or custom your own features.

###some dependencies as follows:

1.requests -- use request to send message to robot API and receive the response

2.itchat -- python2/3 depends on your enviorment.

3.guess_language -- use to judge the message received is chinese or english for google translate(In my code, I only deal with the two languages, other languages are supported by robot)

4.mtranslate -- MIT python package for imitate browser to visit translate.google.com

### You can install it easily by:

> pip install [package-name]

for guess_language, "pip install guess_language" has some problems in my Ubuntu 16.04 server. The alternative choice is pip install from guess_language package source site.


In code, I deal with two language and more with chinese due to country of my friends, it seems a little Redundant, but the text in py file can be deleted and modified by you after you figure it out.


Useful comments for your understanding are included in the py code. Hope, with the wechat robot, your wechat more colorful!


### Ultimate reminder:

1.when you run the py code and it runs correctly, you will see a big QR graph for your phone wechat to scan to log in. If you don't use black background and white font color, the QR graph is strange and not useable.

2.When you apply the tuling123 robot, the robot you use for match this code is self-defined robot, rather than wechat robot which is used for wechat public account（微信公众号）.
