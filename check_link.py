from pytube import YouTube
import os

prohibit_keyword = ["พี่โต", "พรี่โต", "พรี่คาซึยะ", "พี่คาซึยะ", "พี่ตู่", "พี่หลาม", "ใจเกเร", "Ricardo Milos",
                    "ricardo milos", "Ricardo milos", "Ricardo", "Milos", "milos", "ริคาร์โด้",
                    "ricardo", "milos", "เ ก ลี ย ด ค ว า ม ห วั่ น ไ ห ว", "เผาเมืองแปร", "ออกศึก", "pto",
                    "ใ จ เ ก เ ร", "danny", "lee", "danny lee", "Danny", "Lee", "Danny Lee", "Danny lee", "พรี่อู๋", "พรี่", "คุ ณ ภ า พ"]

daeng_word = ["กูบอกไปยังไอพวกชาตินรก","ไอสัสชิบหายมีควย", "มึงทำไปทำเหี้ยอะไร","ทำเพื่ออะไร", "อยากให้คนนู้นคนนี้เขาถูกใจไปหมดเลยไอ้เหี้ย",
              "มึงดียังไงไอเหี้ยสัสมึงดีตรงไหนหรอมึง", "เจ๋งหรอไอเหี้ย", "ส้นตีนไอสัส"]
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
    for i in daeng_word:
        if (i in text) or (text in i):
            return True
    return False

# def check_tenor(url):
