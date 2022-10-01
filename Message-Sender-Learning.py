from requests import post

#Message Sender
r=post('https://textbelt.com/text',data={
	'phone': '+1(284)2420938',#The phone number
	'message': '@vv1ck',#the message
	'key' : 'textbelt'})
if '"success":true' in r.text:
	print('>> Done Send ')
elif '"success":false' in r.text:
	print('>> Error Send ')
else:
	print('>> Error')
print(r.text)
	
	
#OTP Generate
r=post('https://textbelt.com/otp/generate',data={
	'phone': '+1(284)2420938',#The phone Number
	'userid': 'vv1ck@TweakPY.edu',#any Email
	'key': 'example_otp_key'})
if '"success":true' in r.text:
	print('>> Done Send ')
	if '"otp"' in r.text:
		try:
			print(f'>> OTP : {r.json()["otp"]}')
		except Exception as i:
			print(f'Error >> {i}')
			exit()
	else:pass
elif '"success":false' in r.text:
	print('>> Error Send ')
else:
	print('>> Error')
print(r.text)
	
