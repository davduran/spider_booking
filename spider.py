#!/usr/bin/python
#-*- coding utf-8 -*-
import os
import sys
import re
import time
import string
import random
import MySQLdb
import mechanize
from BeautifulSoup import BeautifulSoup  as bs
 
#reload(sys)
 
#sys.setdefaultencoding("utf-8")
 
os.system("clear")
 
br = mechanize.Browser()
 
br.set_handle_robots(False)
 
#----------------------- Total hoteles disponibles por comunidad --------------------------------------
comunidades = [725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 761, 765, 768, 769, 1522, 1523]
 
for i in range(0, 16):
 
 useragent = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/2010020que Ubuntu/9.04 (Alegre) Namoroka/3.6.2pre ',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.en-US-Urv rv:1.9.0.6)',
            'Microsoft Internet Explorer/4.0b1 (Windows 95)',
            'Opera/8.00 (Windows queT 5.1; U; en)',
        'Amaya/9.51 libwww/5.4.0',
        'Mozilla/4.0 (compatible; MSIE 5.0; AOL Windowsndows 95; c_athome)',
        'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (como Gecko) (Kubuntu)',
        'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
                'Mozilla/4.8 [en] (Windows NT 6.0; U)',
                'Opera/9.25 (Windows NT 6.0; U; en)',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                'Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)',
                'Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0',
                'Opera/7.51 (Windows NT 5.1; U) [en]',
                'Opera/7.50 (Windows XP; U)',
                'Opera/7.50 (Windows ME; U) [en]',
                'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a',
                'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
                'Googlebot/2.1 (+http://www.googlebot.com/bot.html)',
                'msnbot/1.0 (+http://search.msn.com/msnbot.htm)',
                'msnbot/0.11 (+http://search.msn.com/msnbot.htm)',
                'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8',
                'Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)',
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/85.8',
                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.15',
                'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
                'Konqueror/3.0-rc4; (Konqueror/3.0-rc4; i686 Linux;;datecode)',
                'Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.8-gentoo-r3; X11;',
                'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
                'BlackBerry8310',
                'Sprint MP6900SP',
                'Mozilla/5.0(SymbianOS/9.2; U; Series60/3.1 NokiaN82/10.0.035; Profile/MIDP-2.0',
                'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)',
                'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                'Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
                'Mozilla/5.0 (Linux; U; Android 1.6; en-gb; Dell Streak Build/Donut AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/ 525.20.1',
                'Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
                'HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1',
                'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                'Mozilla/5.0 (Linux; U; Android 2.0.1; en-us; Droid Build/ESD56) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17']
 
 br.addheaders = [('User-agent', random.choice(useragent))]
 
 time.sleep(random.uniform(1,3))
 
 try:
     respuesta = br.open("http://www.booking.com/searchresults.es.html?checkin_monthday=30;checkin_year_month=2012-7;checkout_monthday=31;checkout_year_month=2012-7;;region="+str(comunidades[i])+";offset=0;rows=50")
 
 except HTTPError, e:
     sys.exit("%d: %s" % (e.code, e.msg))
 
 html = respuesta.read()
 soup = bs(html)
 
 textDisponibles = soup.find('span',{'class':'availability_nr'})
 
 if textDisponibles > 0:
   totalDisponibles = string.replace(textDisponibles.text, ' disponibles.','')
 else:
   totalDisponibles = 0
#------------------------------------------------------------------------------------------------------
 
#-------------------------- Consultamos la disponibilidad por comunidad y por pagina ------------------
 try:
     respuesta = br.open("http://www.booking.com/searchresults.es.html?  checkin_monthday=30;checkin_year_month=2012-7;checkout_monthday=31;checkout_year_month=2012-7;;region="+str(comunidades[i])+";offset=0;rows=50")
 
 except HTTPError, e:
     sys.exit("%d: %s" % (e.code, e.msg))
 
 html2 = respuesta.read()
 soup2 = bs(html)
 
 region = str(comunidades[i])
 
 #nombre hotel
 nombre_hotel = soup2.find('a',{'class':'hotel_name_link url '})
 nombre_hotel = nombre_hotel.get('title')
 nombre_hotel = string.replace(nombre_hotel, u'\u2018', "@")
 nombre_hotel = string.replace(nombre_hotel, u'\u2019', "#")
 
 print nombre_hotel
 
 #checkin
# checkin = unicode("2012-07-30")
# print checkin
 
 #adress
 adress = string.replace(soup2.find('div',{'class':'address'}).text, '&bull;Mostrar mapa','')
 adress = string.replace(adress, u'\u2018', "@")
 adress = string.replace(adress, u'\u2019', "#")
 
 #coordenadas
 coordenadas = soup2.find('a',{'class':'show_map '})
 coordenadas = coordenadas.get('data-coords')
 
 #descripcion
 descripcion = soup2.find('p',{'class':'hotel_desc twocolumns'}).text
 descripcion = string.replace(descripcion, 'usersOnPage.incend usersOnPage.inc', '')
 descripcion = string.replace(descripcion, u'\u2018', "@")
 descripcion = string.replace(descripcion, u'\u2019', "#")
 
 #imagen
 imagen = soup2.find('img',{'class':'hotel round8'})
 imagen = imagen.get('src')
 
 #puntuacion
 puntuacion = soup2.find('span',{'class':'average'}).text
#------------------------------------------------------------------------------------------------------
 
 
#-------------------------------------- Guardamos en la BBDD ------------------------------------------
 db=MySQLdb.connect(host="localhost", user="root", passwd="8945", db="spiderjuice")
 
 cursor=db.cursor()
 
 sql="INSERT INTO hotels (name, adress, descripcion, image, region) VALUES ('"+unicode(nombre_hotel)+"', '"+unicode(adress)+"', '"+unicode(descripcion)+"', '"+unicode(imagen)+"', '"+unicode(region)+"')"
 
 cursor.execute(sql)
