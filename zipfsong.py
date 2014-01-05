'''Get Input'''
num_songs = raw_input()
num_songs = num_songs.split(" ")

n = int(num_songs[0])
m = int(num_songs[1])

songs = []
freqs = []

if n is 0:
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
	z = freqs[0]/(float)(i+1)

	'''Quality'''
	if z > 0.0:
		q = ((float)(freqs[i]))/((float)(z))
	else:
		q = 0.0
	quality.append(q)

'''Top m quality song indexes'''
sorted_quality = sorted(range(len(quality)), key=quality.__getitem__, reverse=True)[0:m]


'''Print Results'''
for i in range(0,m):
	print songs[sorted_quality[i]]
