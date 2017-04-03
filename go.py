import subprocess
import time
import pygame.mixer
pygame.mixer.init(frequency = 48000, size = -16, channels = 2, buffer = 1024)
#電源接続されてない際のアラート音
s = pygame.mixer.Sound("wore.wav")
#復帰時の音声
s2 = pygame.mixer.Sound("arigato.wav")
i=0
while i <100:
	check = subprocess.check_output("acpi")
	check = check.decode()
	if "Discharging" in check:
		s.play(-1)
		while i <100:
			check = subprocess.check_output("acpi")
			check = check.decode()
			if not "Discharging" in check:
				s.stop()
				s2.set_volume(0.5)
				s2.play()
				break
			time.sleep(1)
			print("check")
	print(check)
	time.sleep(1)
	
print(check)
