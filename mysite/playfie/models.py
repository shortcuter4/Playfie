from django.db import models

# Create your models here.

#User(id,password,email,name,surname,username,balance)
class User(models.Model):
	id = models.IntegerField(primary_key=True)
	id = models.AutoField(primary_key=True)
	password = models.CharField(max_length=16, null=False)
	email = models.CharField(max_length=32, null=False, unique=True)
	username =  models.CharField(max_length=16, null=False, unique=True)
	name = models.CharField(max_length=32)
	surname = models.CharField(max_length=32)
	balance = models.IntegerField()

	@property
	def full_name(self):
		"Returns the person's full name."
		return '%s %s' % (self.name, self.surname)

	def __str__(self):
        return self.id
	


#Artist(artist_id, no_of_albums, bio)
class Artist(models.Model):
	artist_id = models.ForeignKey(User, on_delete=models.CASCADE)
	no_of_albums = models.IntegerField()
	bio - models.TextField()

	def __str__(self):
		return self.artist_id


#RegularUser(user_id,no_of_friends,no_of_playlists)
class RegularUser(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	no_of_friends = models.IntegerField()
	no_of_playlists = models.IntegerField()

	def __str__(self):
		return self.user_id


# Podcaster(podcaster_id,profession)
class Podcaster(models.Model):
	podcaster_id = models.ForeignKey(User, on_delete=models.CASCADE)
	profession = models.CharField(max_length=32)

	def __str__(self):
        return self.podcaster_id

# MusicProduct(product-id, price,name,releasedate)
class MusicProduct(models.Model):
	product_id = models.AutoField(primary_key=True)
	price = models.IntegerField()
	name = models.CharField(max_length=32)
	release_date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
        return self.product_id

# Album(album_id,no_of_songs,total-time)
class Album(models.Model):
	album_id = models.ForeignKey(MusicProduct, on_delete=models.CASCADE)
	no_of_songs = models.IntegerField()
	total_time = models.IntegerField()

	def __str__(self):
        return self.album_id

# Song(song_id,songtime)
class Song(models.Model):
	song_id = models.ForeignKey(MusicProduct, on_delete=models.CASCADE)
	song_time = models.IntegerField()

	def __str__(self):
        return self.song_id

# Podcast(p-id,topic,name,price)
class Podcast(models.Model):
	p_id = models.AutoField(primary_key=True)
	topic = models.TextField()
	name = models.CharField(max_length=32)
	price = models.IntegerField()

	def __str__(self):
        return self.p_id

# Playlist(pl-id,playlist-name,total-time,no-of-songs)
class Playlist(models.Model):
	pl_id = models.AutoField(primary_key=True)
	pl_name = models.CharField(max_length=32)
	total_time = models.IntegerField()
	no_of_songs = models.IntegerField()

	def __str__(self):
        return self.pl_id

# Comment(c-id,textBody,date)
class Comment(models.Model):
	c_id = models.AutoField(primary_key=True)
	textBody = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
        return self.c_id

# Genre(genre-id,genre-name)
class Genre(models.Model):
	genre_id = models.AutoField(primary_key=True)
	genre_name = models.CharField(max_length=32)

	def __str__(self):
        return self.genre_id

# Schedule(s-id,p-id,schedule_description,date)
class Schedule(models.Model):
	s_id = models.ForeignKey(Podcast, on_delete=models.CASCADE)
	p_id = models.IntegerField(primary_key=True)
	description = models.TextField()
	date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
        return self.s_id