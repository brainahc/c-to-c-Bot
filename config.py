import os

class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1717678870:AAHhSGt4VITjuDnRGQxn_YZj7r_0kicyot8")
      API_ID = int(os.environ.get("APP_ID", 174376))
      API_HASH = os.environ.get("API_HASH","1add6707c2c1790deefd09eff3ebaa54")
      CHANNEL = set(x for x in os.environ.get("-1001431924155", "1001202193311").replace("\n", " ").split(' '))
