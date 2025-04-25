# Create a tokenizer for your own language (mother tongue you speak). The tokenizer should
# tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,
# “3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
# this. [Hint: Use unicode blocks for your language, check wikipedia page

import re
class tokenizer_marathi:
    def __init__(self,text):
        self.t = text
    def punctuations(self):
        '''tokenize punctuations'''
        pattern = r'[|,;?!""-:^°=…]'
        res = re.split(pattern,self.t)
        return res
    def dates(self):
        '''dates from text'''
        pattern = r'[\d]+/[\d]+/[\d]+'
        return re.findall(pattern,self.t)
    def urls(self):
        '''returns url from text'''
        pattern = r'http[s]*://www.[\w]+.com'
        return re.findall(pattern,self.t)
    def emails(self):
        '''returns emails from text'''
        pattern = r'[\w]+@[\w]+.com'
        return re.findall(pattern,self.t)
    def numbers(self):
        '''returns various numbers from text'''
        pattern = r'[\d]+/[d]+|[\d]+[.]+[\d]+|\s[\d]+\s'
        return re.findall(pattern,self.t)
    def username(self):
        '''returns social media usernames handle names'''
        pattern = r'@[\w]+'
        return re.findall(pattern,self.t)
    def display(self):
        return self.t
    def whole(self):
        pattern = r'[|,;?!""-:^°=…]|[\d]+/[\d]+/[\d]+|http[s]*://www.[\w]+.com|[\w]+@[\w]+.com|[\d]+/[d]+|[\d]+[.]+[\d]+|\s[\d]+\s|@[\w]+|\w+'
        return re.findall(pattern,self.t)
    

tokken = '''तुमचा ईमेल / फोन नंबर / पत्ता काय आहे. हा माझा ईमेल / फोन नंबर / पत्ता आहे. तुम्ही Facebook किंवा Twitter वर आहात?'''

text = tokenizer_marathi(tokken)
print(text.display())
