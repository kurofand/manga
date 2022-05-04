#-*-coding:utf-8-*-
import json

class Manga:
	name=u"";
	chapterCount=0;
	chapterReaded=0;
	ongoing=False;
	genre=[];

	def __init__(self, name=u"", chapterCount=0, chapterReaded=0, ongoing=False, genre=[]):
		self.name=name;
		self.chapterCount=chapterCount;
		self.chapterReaded=chapterReaded;
		self.ongoing=ongoing;
		self.genre=genre;

	def fromJson(self, fName):
		f=open(fName, "r");
		jStr=json.load(f);
		f.close();
		self.name=jStr["name"];
		self.chapterCount=jStr["chapterCount"];
		self.chapterReaded=jStr["chapterReaded"];
		self.ongoing=jStr["ongoing"];
		self.genre=jStr["genre"];

	def toDict(self):
		res={};
		res["name"]=self.name;
		res["chapterCount"]=self.chapterCount;
		res["chapterReaded"]=self.chapterReaded;
		res["ongoing"]=self.ongoing;
		res["genre"]=self.genre;
		return res;

	def toJson(self, fName):
		f=open(fName, "w");
		s=u"{";
		dict=self.toDict();
		for key in dict.keys():
			s=s+u"\"%s\":"%key;
			if((isinstance(dict[key], unicode))or(isinstance(dict[key], str))):
				s=s+u"\"%s\""%dict[key];
			elif(isinstance(dict[key], bool)):
				s=s+u"%s"%unicode(dict[key]).replace(u"F", u"f").replace(u"T", u"t");
			elif(isinstance(dict[key], list)):
				s=s+u"[\"%s\"]"%u"\",\"".join(dict[key]);
			else:
				s=s+unicode(dict[key]);
#			if(key==u"name"):
#				s=s+u"\"%s\","%(key, dict[key]);
#			elif(key=="ongoing"):
#				s=s+u"\"%s\"
#			elif(key!="genre"):
#				s=s+u"\"%s\":%s,"%(key, dict[key]);
#			else:
#				s=s+u"\"%s\":[\"%s\"],"%(key, u"\",\"".join(dict[key]));
			s=s+u",";
		s=s[:-1]+u"}";
		f.write(s.encode("utf-8"));
		f.close();

	def toScr(self):
		print(u"Название:%s\nКоличество глав:%s\nГлав прочитано:%s\nОнгоинг:%s\nЖанры:%s"%(self.name, self.chapterCount, self.chapterReaded, u"да" if(self.ongoing) else u"нет", u",".join(self.genre)));
