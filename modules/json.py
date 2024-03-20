import os
import json

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
setting_json_path = os.path.join(root_dir, "json", "Setting.json")
token_json_path = os.path.join(root_dir, "json", "Token.json")
DynamicVoice_json_path = os.path.join(root_dir, "json", "DynamicVoiceID.json")
words_json_path = os.path.join(root_dir, "json", "Words.json")

def open_setting_json():
    with open(setting_json_path,"r",encoding="utf8") as jfile:
        jdata = json.load(jfile)
    return jdata
    
def open_token_json():
    with open(token_json_path,"r",encoding="utf8") as tfile:
        TOKEN = json.load(tfile)
    return TOKEN

def open_DynamicVoice_json():
    with open(DynamicVoice_json_path,"r",encoding="utf8") as f:
        origin_channels = json.load(f)
    return origin_channels

def dump_setting():
    global jdata
    with open(setting_json_path,"w",encoding="utf8") as f:
        json.dump(jdata, f, ensure_ascii=False, indent=4)

def open_words_json():
    with open(words_json_path,"r",encoding="utf8") as f:
        words = json.load(f)
    return words

def dump_words(words):
    with open(words_json_path,"w",encoding="utf8") as f:
        json.dump(words, f)