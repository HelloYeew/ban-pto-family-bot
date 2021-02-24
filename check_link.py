from pytube import YouTube
from function import *
import os

prohibit_keyword = ["พี่โต", "พรี่โต", "พรี่คาซึยะ", "พี่คาซึยะ", "พี่ตู่", "พี่หลาม", "ใจเกเร", "Ricardo Milos",
                    "ricardo milos", "Ricardo milos", "Ricardo", "Milos", "milos", "ริคาร์โด้",
                    "ricardo", "milos", "เ ก ลี ย ด ค ว า ม ห วั่ น ไ ห ว", "เผาเมืองแปร", "ออกศึก", "pto",
                    "ใ จ เ ก เ ร", "danny", "lee", "danny lee", "Danny", "Lee", "Danny Lee", "Danny lee",
                    "พรี่อู๋", "พรี่", "คุ ณ ภ า พ", "in-your-face", "cleaning-ass", "sex", "gachi", "ass",
                    "gachimuchi", "junkyard", "boyz", "Junkyard"]

daeng_word = ["กูบอกไปยังไอพวกชาตินรก", "ไอสัสชิบหายมีควย", "มึงทำไปทำเหี้ยอะไร", "ทำเพื่ออะไร",
              "อยากให้คนนู้นคนนี้เขาถูกใจไปหมดเลยไอ้เหี้ย",
              "มึงดียังไงไอเหี้ยสัสมึงดีตรงไหนหรอมึง", "เจ๋งหรอไอเหี้ย", "ส้นตีนไอสัส"]

mention_keyword = ["Kasumi", "kasumi", "คาซึมิ", "ตาสุมิ"]

revenge_keyword = read_file("revenge_keyword.txt")


# slicing word

def check_youtube(url):
    video = YouTube(url)
    name = video.title
    for word in prohibit_keyword:
        if word in name:
            return True
    return False


def check_only_keyword(text):
    for i in prohibit_keyword:
        if i in text:
            return True
    return False


def check_daeng_word(text):
    if text in daeng_word:
        return True
    return False


def check_revenge_keyword(text):
    for i in revenge_keyword:
        if i in text:
            return True
    return False

# def check_tenor(url):
