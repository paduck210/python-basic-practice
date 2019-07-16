
#앨범 테이블 만들기
CREATE TABLE "Album" (
"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
"artist_id" INTEGER,
"title" TEXT)

#앨범 테이블 데이터 추가
INSERT INTO Album (artist_id,title) VALUES (3, "MIC DROP") ;
INSERT INTO Album (artist_id,title) VALUES (1, "baby baby") ;


#아티스트 테이블 만들기
CREATE TABLE "Artist" (
"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
"name" TEXT)

#아티스트 테이블 테이터 추가
INSERT INTO Artist (name) VALUES ("Rock") ;
INSERT INTO Artist (name) VALUES ("R&B") ;
INSERT INTO Artist (name) VALUES ("KPOP") ;

#앨범 타이틀을 기준으로 // 아티스트 id 매칭하기
#select Album.title, Album.artist_id from Album join Artist on Album.artist_id = Artist.id ;
select Album.title, Album.artist_id, Artist.id, Artist.name from Album join Artist on Album.artist_id = Artist.id ;









#
#
# js = json.loads(data)
#
# first = js["response"]
# second = first["docs"]
#
# for each in second:
#     newid = each["id"]
#     newjl = each["journal"]
#     newen = each["eissn"]
#     newpu = each["publication_date"]
#     newar = each["article_type"]
#     newat = each["author_display"][0]
#     newab = each["abstract"][0]
#     newti = each["title_display"]
#     newsc = each["score"]
#
#
#     cur.execute('''INSERT INTO docs (id, journal, eissn, publication_date, article_type, author_display, abstract, title_display, score)
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (newid,newjl,newen,newpu,newar,newat, newab,newti,newsc))
#     conn.commit()
#
# cur.close()
