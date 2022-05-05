#-*-coding:utf-8-*-

import json

from manga import Manga

class MangaList:
	mangas=[];
	genres=[];

	def __init__(self):
		self.mangas=[];

	def fromJson(self, fName):
		f=open(fName, "r");
		jStr=json.load(f);
		f.close();
		for manga in jStr["mangas"]:
			self.mangas.append(Manga().fromDict(manga, self));
		self.genres=jStr["genres"];
		return self;

	def toJson(self, fName):
		f=open(fName, "w");
		s=u"{";
		s=s+u"\"mangas\":["
		for manga in self.mangas:
			s=s+manga.toJson()+u",";
		s=s[:-1]+u"],";
		s=s+u"\"genres\":[";
		for genre in self.genres:
			s=s+u"{"
			for key in genre.keys():
				s=s+u"\"%s\":"%key+(u"\"%s\","%genre[key] if((isinstance(genre[key], str)or(isinstance(genre[key], unicode)))) else u"%s,"%unicode(genre[key]));
			s=s[:-1]+u"},";
		s=s[:-1]+u"]";
		s=s+u"}";
		f.write(s.encode("utf-8"));
		f.close();

	def returnGenreNameById(self, id):
		res=u"";
		for genre in self.genres:
			if(genre["id"]==id):
				res=genre["name"];
				break;
		return res;

	def returnGenres(self, ids):
		res=u"";
		for id in ids:
			res=res+u"%s,"%self.returnGenreNameById(id);
		return res[:-1];

	def returnMangaById(self, id):
		for manga in self.mangas:
			if(manga.id==id):
				return manga;

	def returnMangaByName(self, name):
		for manga in self.mangas:
			if(manga.name==name):
				return manga;

	def returnMangasByGenre(self, id):
		mangas=[];
		for manga in self.mangas:
			if(id in manga.genre):
				mangas.append(manga);
		return mangas;

	def updateManga(self, id, name=u"", chapterCount=0, chapterReaded=0, ongoing=False, genre=[]):
		manga=self.returnMangaById(id);
		manga.name=name;
		manga.chapterCount=chapterCount;
		manga.chapterReaded=chapterReaded;
		manga.ongoing=ongoing;
		manga.genre=genre;
