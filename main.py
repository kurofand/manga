#-*-coding:utf-8-*-

from mangaList import MangaList
from manga import Manga

mangaList=MangaList().fromJson("manga.json");
#for manga in mangaList.returnMangasByGenre(3):
#	manga.toScr();
for manga in mangaList.mangas:
	manga.toScr();
