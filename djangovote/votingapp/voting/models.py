from django.db import models
# Create your models here.
class users(models.Model):
	username = models.CharField(max_length = 20) 
	password = models.CharField(max_length = 100)
	name = models.CharField(max_length = 30) 
	phone = models.IntegerField()
	userflag = models.IntegerField(default = 0)


class votes(models.Model):
	votespeaker = models.IntegerField()
	voteevalu = models.IntegerField()
	votetable = models.IntegerField()

class dashs(models.Model):
	s1 = models.CharField(max_length = 30)
	s2 = models.CharField(max_length = 30)
	s3 = models.CharField(max_length = 30)
	s4 = models.CharField(max_length = 30)

class dashe(models.Model):
	e1 = models.CharField(max_length = 30)
	e2 = models.CharField(max_length = 30)
	e3 = models.CharField(max_length = 30)
	e4 = models.CharField(max_length = 30)

class dasht(models.Model):
	t1 = models.CharField(max_length = 30)
	t2 = models.CharField(max_length = 30)
	t3 = models.CharField(max_length = 30)
	t4 = models.CharField(max_length = 30)
	t5 = models.CharField(max_length = 30)
	t6 = models.CharField(max_length = 30)
	t7 = models.CharField(max_length = 30)

class result(models.Model):
	speaker1 = models.IntegerField(default = 0)
	speaker2 = models.IntegerField(default = 0)
	speaker3 = models.IntegerField(default = 0)
	speaker4 = models.IntegerField(default = 0)
	evalu1 = models.IntegerField(default = 0)
	evalu2 = models.IntegerField(default = 0)
	evalu3 = models.IntegerField(default = 0)
	evalu4 = models.IntegerField(default = 0)
	table1 = models.IntegerField(default = 0)
	table2 = models.IntegerField(default = 0)
	table3 = models.IntegerField(default = 0)
	table4 = models.IntegerField(default = 0)
	table5 = models.IntegerField(default = 0)
	table6 = models.IntegerField(default = 0)
	table7 = models.IntegerField(default = 0)

def _str_(self):
	return self.username
