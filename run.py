import platform,os
os.system('git pull')
print('\x1b[1;92mJOIN OUR FB GROUP')
os.system("xdg-open https://www.facebook.com/groups/737172040863921/?ref=share")
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("okk_enc").login()
elif 'aarch' in arc:
	__import__("x").login()
else:
	print('YOUR DEVICE ARCHITECTURE IS NOT SUPPORTING OUR SCRIPT')
