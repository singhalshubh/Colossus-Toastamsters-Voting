from django.shortcuts import render,redirect
from voting.models import users,votes,dashs,dashe,dasht,result
from django.http import HttpResponse
import hashlib,os
# Create your views here.

def user(request):
	if request and request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['password']
		phone = request.POST['phone']
		name = request.POST['name']
		password = hashlib.sha224(password1.encode('utf-8')).hexdigest()
		if(users.objects.filter(username = username).exists()):
			u = users.objects.get(username = username)
			if(not hashlib.sha224(password1.encode('utf-8')).hexdigest() == u.password ):
				return render(request , 'voting/intrude.html')
			elif(u.userflag == 1 and hashlib.sha224(password1.encode('utf-8')).hexdigest() == u.password):
				return render(request , 'voting/thank.html')
		else:
			users.objects.create(name = name , phone = phone , username = username , password = password)
			u = users.objects.get(username = username)
			u.userflag = 1
			u.save() 	
			return redirect( 'vote' , pk = u.id)

	else:
		return render(request , 'voting/index.html')


def vote(request,pk):
	if request and request.method == 'POST':
		votespeaker = request.POST['speaker']
		votetable = request.POST['table']
		voteevalu = request.POST['eval']
		votes.objects.create(votespeaker = votespeaker , voteevalu = voteevalu , votetable = votetable)
		#The id represents the meet number and thus the rsults should be stored somewhere as a backup if flushing the database
		results = result.objects.get(id = 1)
		if(votespeaker == '1'):
			results.speaker1 = results.speaker1 + 1
		elif(votespeaker == '2'):
			results.speaker2 = results.speaker2 + 1
		elif(votespeaker == '3'):
			results.speaker3 = results.speaker3 + 1
		else:
			results.speaker4 = results.speaker4 + 1

		if(voteevalu == '1'):
			results.evalu1 = results.evalu1 + 1
		elif(voteevalu == '2'):
			results.evalu2 = results.evalu2 + 1
		elif(voteevalu == '3'):
			results.evalu3 = results.evalu3 + 1
		else:
			results.evalu4 = results.evalu4 + 1

		if(votetable == '1'):
			results.table1 = results.table1 + 1
		elif(votetable == '2'):
			results.table2 = results.table2 + 1
		elif(votetable == '3'):
			results.table3 = results.table3+  1
		elif(votetable == '4'):
			results.table4 = results.table4 + 1
		elif(votetable == '5'):
			results.table5 = results.table5 + 1
		elif(votetable == '6'):
			results.table6 = results.table6 + 1
		else:
			results.table7 = results.table7 + 1
		results.save()
		return redirect('/')
	else:
		return render(request , 'voting/vote.html')

def dash(request):
	if request and request.method == 'POST':
		s1 = request.POST['s1']
		s2 = request.POST['s2']
		s3 = request.POST['s3']
		s4 = request.POST['s4']
		dashs.objects.create(s1 = s1 ,s2 = s2 , s3 = s3 , s4 = s4);
		return render(request,'voting/dash.html')
	else:
		return render(request , 'voting/dash.html')


def dashse(request):
	if request and request.method == 'POST':
		e1 = request.POST['e1']
		e2 = request.POST['e2']
		e3 = request.POST['e3']
		e4 = request.POST['e4']
		dashe.objects.create(e1 = e1 , e2 = e2 , e3 = e3 , e4 = e4);
		return render(request,'voting/dashe.html')
	else:
		return render(request , 'voting/dashe.html')


def dashst(request):
	if request and request.method == 'POST':
		t1 = request.POST['t1']
		t2 = request.POST['t2']
		t3 = request.POST['t3']
		t4 = request.POST['t4']
		t5 = request.POST['t5']
		t6 = request.POST['t6']
		t7 = request.POST['t7']
		dasht.objects.create(t1 = t1 , t2 = t2 , t3 = t3 , t4 = t4 , t5 = t5 , t6 = t6 , t7 = t7);
		return render(request,'voting/dasht.html')
	else:
		return render(request , 'voting/dasht.html')


