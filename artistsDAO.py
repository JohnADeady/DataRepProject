import mysql.connector 
import dbconfig as cfg


class ArtistsDAO:     
	db=""     
	def __init__(self):          
	    self.db = mysql.connector.connect(        
		host=cfg.mysql['host'],
		user=cfg.mysql['username'],
		password=cfg.mysql['password'],
		#auth_plugin='mysql_native_password',        
		database=cfg.mysql['database']
		)     
		
	def create(self, values):
		cursor = self.db.cursor()
		sql="insert into artists (name, genre, albums) values (%s,%s, %s)"
		cursor.execute(sql, values)
		self.db.commit()
		return cursor.lastrowid
		
	def createal(self, values):
		cursor = self.db.cursor()
		sql="insert into albums (title, artist, duration) values (%s,%s, %s)"
		cursor.execute(sql, values)
		self.db.commit()
		return cursor.lastrowid
		
	def getAll(self):
		cursor = self.db.cursor()
		sql="select * from artists"
		cursor.execute(sql)
		results = cursor.fetchall()
		
		returnArray = []
		print(results)
		for result in results:
			print(result)
			returnArray.append(self.convertToDictionary(result))
		
		return returnArray
		
	def getAllal(self):
		cursor = self.db.cursor()
		sql="select * from albums"
		cursor.execute(sql)
		results = cursor.fetchall()
		
		returnArray = []
		print(results)
		for result in results:
			print(result)
			returnArray.append(self.convertToDictionaryal(result))
		
		return returnArray
		
	def findByID(self, id):
		cursor = self.db.cursor()
		sql="select * from artists where id = %s"
		values = (id,)
		
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return self.convertToDictionary(result)
	
	def findByIDal(self, id):
		cursor = self.db.cursor()
		sql="select * from albums where id = %s"
		values = (id,)
		
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return self.convertToDictionary(result)
		
	def update(self, values):
		cursor = self.db.cursor()
		sql="update artists set name= %s, genre=%s, albums=%s  where id = %s"
		cursor.execute(sql, values)
		self.db.commit()
		
	def updateal(self, values):
		cursor = self.db.cursor()
		sql="update albums set title= %s, artist=%s, duration=%s  where id = %s"
		cursor.execute(sql, values)
		self.db.commit()
		
	def delete(self, id):
		cursor = self.db.cursor()
		sql="delete from artists where id = %s"
		values = (id,)
		cursor.execute(sql, values)
		self.db.commit()
		print("delete done")

	def deleteal(self, id):
		cursor = self.db.cursor()
		sql="delete from albums where id = %s"
		values = (id,)
		cursor.execute(sql, values)
		self.db.commit()
		print("delete done")
			
	def updateIDs(self, values):
		cursor = self.db.cursor()
		sql="update artists inner join albums on artists.name = albums.artist set artists.id = albums.id"
		cursor.execute(sql, values)
		self.db.commit()
		
	def convertToDictionary(self, result):
		colnames=['id','name','genre','albums']
		
		item = {}
		
		if result:
			for i, colName in enumerate(colnames):
				value = result[i]
				item[colName] = value
		
		return item
		
	def convertToDictionaryal(self, result):
		colnames=['id','title','artist','duration']
		
		item = {}
		
		if result:
			for i, colName in enumerate(colnames):
				value = result[i]
				item[colName] = value
		
		return item
		
 
artistsDAO = ArtistsDAO() 