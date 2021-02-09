from pytube import YouTube
import os

prohibit_keyword = ["พี่โต", "พรี่โต", "พรี่คาซึยะ", "พี่คาซึยะ", "พี่ตู่", "พี่หลาม", "ใจเกเร", "Ricardo Milos",
                    "ricardo milos", "Ricardo milos", "Ricardo", "Milos", "milos",
                    "ricardo", "milos", "เ ก ลี ย ด ค ว า ม ห วั่ น ไ ห ว", "เผาเมืองแปร", "ออกศึก", "pto",
                    "ใ จ เ ก เ ร", "danny", "lee", "danny lee", "Danny", "Lee", "Danny Lee", "Danny lee"]


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

# def check_tenor(url):
