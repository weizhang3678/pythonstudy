'''
Created on Feb 12, 2020

@author: zhangwei
'''
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
file = urllib.request.urlopen('https://github.com/weizhang3678/javafx/blob/master/src/javafx/yf/ch01/FxDemo.java');
message = file.read()
print(message)