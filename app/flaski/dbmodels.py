from sqlalchemy import Column, Integer, String, Boolean
from flaski.db import Base

class FishMaster(Base):
    __tablename__ = "fish_master"
    fish_name = Column(String, primary_key=True)
    poison = Column(Integer)
    poison_part = Column(String)
    wiki_url = Column(String)
    picture_path = Column(String)
    copyright_owner = Column(String)
    copyright_url = Column(String)
    
    def __init__(self, fish_name=None, poison=None, poison_part=None, wiki_url=None, picture_path=None, copyright_owner=None, copyright_url=None):
        self.fish_name = fish_name
        self.poison = poison
        self.poison_part = poison_part
        self.wiki_url = wiki_url
        self.picture_path = picture_path
        self.copyright_owner = copyright_owner
        self.copyright_url = copyright_url