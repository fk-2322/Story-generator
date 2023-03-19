import random
when = ['A few years ago','yestarday','last night','a long time ago','on 20th jan']
who = ['a rabbit',' an elephant','a mouse','a turtle','a cat']
name = ['ali','miriam','daniel','houk','starwalker']
residence = ['barcelona','patna','Panama','GOA','uk','Virgin Iland']
went = ['cinema','university','seminar','school','bank','pmo house']
happened = ['made a lot of friends','eats a burger','found a secret key','slolved a mistery','wrote a book']
print(random.choice(when) +', '+ random.choice(who)+' named '+ random.choice(name)+ ' that lived in '+random.choice(residence)+' went to the '+ random.choice(went)+' and '+random.choice(happened)+'.')