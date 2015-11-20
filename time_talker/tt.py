#! /usr/bin/env python
import subprocess
import sys
import datetime
from jinja2 import Environment, PackageLoader
jinja_env = Environment(loader=PackageLoader('tt',
                                             'template'))

def speak(text, speed=200):
    speed = str(speed)
    cmd = ['espeak',
           '-v', 'mb-en1',
           '-s', speed,
           '-m',
           '--stdout']
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(input=text)
    p2 = subprocess.Popen(('paplay'), stdin=subprocess.PIPE)
    p2.communicate(input=output[0])

def check_arg():
    switch = 0
    try:
        option = sys.argv[1]
        if option == '-f':
            switch = 1
    except IndexError:
        pass
    return switch

class myDateTime():
    def __init__(self):
        """
        """
        self.now = datetime.datetime.now()

    def split_num(self,n):
        n = str(n).upper()
        result = ' '.join(n)
        return result

    def getT(self,p):
        """
        """
        result = {}
        time_part = self.now.strftime(p)
        result['whole'] = time_part
        result['split'] = self.split_num(time_part)
        result['suffix'] = self.ordinal(time_part)
        return result

    def output(self):
        """
        """
        emph = {'rate':0.2,
                'pitch':'-20%'}
        num = {'volume':"100",
               'rate':'.9',
               'rate_2':'1.5'}
        line = {'hour':d.getT('%H'),
                'minute':d.getT('%M'),
                'month':d.getT('%B'),
                'month_abr':d.getT('%b'),
                'day':d.getT('%d'),
                'switch':check_arg(),
                'emph':emph,
                'num':num}
        return line

    def ordinal(self,n):
        try:
            n = int(n)
        except ValueError:
            return None
        if 10 <= n % 100 < 20:
            return 'th'
        else:
            return  {1 : 'st',
                     2 : 'nd',
                     3 : 'rd'}.get(n % 10, "th")

if __name__ == '__main__':
    template = jinja_env.get_template('time.ssml')
    d = myDateTime()
    message = template.render(d.output())
    print(message)
    speak(message.replace("\n",""))
    
