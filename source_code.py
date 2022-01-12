# @Date:   2022-01-04T21:36:22+03:00
# @Last modified time: 2022-01-12T11:11:17+03:00
import time,datetime
from time import sleep
import string

#----------------Kutuphane sinifi----------------
class Rastgele_Karakter:

    #-----------Epoch saniyelerini hesaplayan fonksiyon-----------
    def get_epochseconds(self):
        f = open("sonuc.txt", "a")

        time.sleep(0.001)
        v1 = time.time()
        v2 = int(time.time())
        v3 = (v1-v2)
        number = int(str(v3).replace('.', ''))
        return number


    #------Iki karakter arasinda random karakter ureten fonksiyon(n = uretmek istediginiz karakter sayisi)------
    def random_character_between(self, n, x, y):
        f = open("sonuc.txt", "a")
        f.write("Random %d character(s) between (%s,%s): "%(n, x, y))

        for q in range(n):
            number = self.get_epochseconds()
            start = ord(x)
            end = ord(y)
            number_between = min(start, end)+1
            number_between += ((number%100)%(max(start,end)-(min(start,end))))-1 # 54 / 4 = 2 - 1 = 1
            if(int((number_between%10) % 2) == 0):
                flag = True
            else:
                flag = False
            letter = chr(number_between)
            f.write(letter)
        f.write("\n")


    #-------Random karakter ureten fonksiyon(b = istediginiz karakter sayisi, default olarak 1 belirledim)-------
    def random_character(self, b = 1):
        f = open("sonuc.txt", "a")

        f.write("Random %d character(s): "%(b))
        for q in range(b):
            number = self.get_epochseconds() #12345

            if(int((number%10) % 2) == 0): #5
                flag = True #kucuk harf olcak
            else:
                flag = False #buyuk harf olcak

            if(flag == True):
                letter = chr(97 + ((number%100)%26)) #45 = 19 = 116

            else:
                letter = chr(65 + number%100%26) # 19 = 84

            f.write(letter)

        f.write("\n")

    #------Belirli karakterlerden random olarak karakter secen fonksiyon(n = istediginiz karakter sayisi)------
    def random_character_from(self, n, a, b, c, d, e, g):
        f = open("sonuc.txt", "a")
        f.write("Random %d character(s) from (%s, %s, %s, %s, %s, %s): "%(n, a, b, c, d, e, g))
        for q in range(n):
            number = self.get_epochseconds()
            number = number%6
            if(number == 0):
                letter = a
            elif(number == 1):
                letter = b
            elif(number == 2):
                letter = c
            elif(number == 3):
                letter = d
            elif(number == 4):
                letter = e
            else:
                letter = g
            f.write(letter)
        f.write("\n")


    #-------Random karakterlerden cumle ureten fonksiyon(n = istediginiz kelime sayisi, default olarak 1 belirledim)-------
    def random_words(self, n = 1):
        f = open("sonuc.txt", "a")
        f.write("%d Random Sentence(s): "%(n))
        for q in range(n):
            number = self.get_epochseconds()

            sentence_size = number%10
            for _ in range(sentence_size):
                number = self.get_epochseconds()

                if((int(number%10) % 2) == 0):
                    flag = True
                else:
                    flag = False

                if(flag == True):
                    letter = chr(((number%100)%26) + 97)
                else:
                    letter_number = 65 + number%100%26
                    letter = chr(65 + number%100%26)

                f.write(letter)
            f.write(" ")
        f.write("\n")

    #----------random small letter'lardan cumle olusturan fonksiyon----------
    def random_small_words(self, n = 1):
        f = open("sonuc.txt", "a")
        f.write("%d Random Sentence(s) with small letters: "%(n))
        for q in range(n):
            number = self.get_epochseconds()

            sentence_size = number%10
            for _ in range(sentence_size):
                number = self.get_epochseconds()

                letter = chr(((number%100)%26) + 97)

                f.write(letter)
            f.write(" ")
        f.write("\n")

    #----------random capital letter'lardan cumle olusturan fonksiyon(n = istediginiz kelime sayisi, default olarak 1 belirledim)----------
    def random_capital_words(self, n = 1):
        f = open("sonuc.txt", "a")
        f.write("%d Random Sentence(s) with capital letters: "%(n))
        for q in range(n):
            number = self.get_epochseconds()
            sentence_size = number%10
            for _ in range(sentence_size):
                number = self.get_epochseconds()
                letter = chr(((number%100)%26) + 65)
                f.write(letter)
            f.write(" ")
        f.write("\n")


#--------main---------
f = open("sonuc.txt", "a")
f.write("\n ----------------- \n")
random1 = Rastgele_Karakter()
random1.random_character_from(5,'a','b','c','d','g','e')
random1.random_character_between(4,'a','d')
random1.random_character(5)
random1.random_small_words(4)
random1.random_capital_words(5)
random1.random_words(4)
