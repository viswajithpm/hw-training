from lxml.html import fromstring,tostring

form_page = fromstring('''<html><body><form>Your Name: <input type="text" name="name"><br>Your Phone: <input type="text" name="phone"><br>Your Favorite:Dogs <input type="checkbox" name="interest" value="dog">Cats <input type="checkbox" name="interest" value="cat">Birds <input type="checkbox" name="interest" value="bird"><input type="submit"></form></body></html>''')
form = form_page.forms[0]
form_fields = dict(
		name='john smith',
		phone='2434076',
		interest=set(['cat','dog'])

		)
print(tostring(form))