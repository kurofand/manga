#-*-coding:utf-8-*-
import json

class Manga:
	name=u"";
	chapterCount=0;
	chapterReaded=0;
	ongoing=False;
	genre=[];
	parent=None;

	def __init__(self):
		self.name=u"";
		self.chapterCount=0;
		self.chapterReaded=0;
		self.ongoing=False;
		self.genre=[];
		self.parent=None;

	def fromDict(self, dict, parent=None):
		self.name=dict["name"];
		self.chapterCount=dict["chapterCount"];
		self.chapterReaded=dict["chapterReaded"];
		self.ongoing=dict["ongoing"];
		self.genre=dict["genre"];
		if(not(parent is None)):
			self.parent=parent;
		return self;

	def toDict(self):
		res={};
		res["name"]=self.name;
		res["chapterCount"]=self.chapterCount;
		res["chapterReaded"]=self.chapterReaded;
		res["ongoing"]=self.ongoing;
		res["genre"]=self.genre;
		return res;

	def toJson(self):
		s=u"{";
		dict=self.toDict();
		for key in dict.keys():
			s=s+u"\"%s\":"%key;
			if((isinstance(dict[key], unicode))or(isinstance(dict[key], str))):
				s=s+u"\"%s\""%dict[key];
			elif(isinstance(dict[key], bool)):
				s=s+u"%s"%unicode(dict[key]).replace(u"F", u"f").replace(u"T", u"t");
			elif(isinstance(dict[key], list)):
#				s=s+u"[%d]"%u",".join(dict[key]);
				s=s+u"[";
				for e in dict[key]:
					s=s+u"%s,"%unicode(e);
				s=s[:-1]+u"]";
			else:
				s=s+unicode(dict[key]);
			s=s+u",";
		s=s[:-1]+u"}";
		return s;

	def toScr(self):
		genres=u"";
		if(not(self.parent is None)):
			genres=self.parent.returnGenres(self.genre);
		print(u"Название:%s\nКоличество глав:%s\nГлав прочитано:%s\nОнгоинг:%s\nЖанры:%s"%(self.name, self.chapterCount, self.chapterReaded, u"да" if(self.ongoing) else u"нет", genres));
