'''Get Input'''
num_songs = raw_input()
num_songs = num_songs.split(" ")

n = int(num_songs[0])
m = int(num_songs[1])

songs = []
freqs = []

if n <= 0 or m <= 0:
	exit(0)

for i in range(0,n):
	'''Input'''
	song_details = raw_input()
	song_details = song_details.split(" ")

	'''True Frequency'''
	f = int(song_details[0])
	freqs.append(f)

	'''Title'''
	s = song_details[1]
	songs.append(s)


'''Compute Quality'''
quality = []

for i in range(0,n):
	'''Zipf Frequency'''
#	z = freqs[0]/(float)(i+1)

#	if freqs[0] <= 0:
#		q1 = float(0)
#	else:
#		q1 = (float)(freqs[i] * i/freqs[0])

	'''Quality'''
	q = (float)(freqs[i] * (i+1))
	quality.append(q)

'''Top m quality song indexes'''
sorted_quality = sorted(range(len(quality)), key=quality.__getitem__, reverse=True)[0:m]

#print quality
#print sorted_quality


'''Print Results'''
for i in range(0,m):
	print songs[sorted_quality[i]]
