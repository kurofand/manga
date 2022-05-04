#-*-coding:utf-8-*-

from manga import Manga

#manga=Manga(u"Naruto", 709, 709, False, [u"сёнен", u"боевик", u"комедия"]);
#manga.toJson(u"manga.json");
manga=Manga();
manga.fromJson("manga.json");
manga.toScr();
