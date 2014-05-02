# calculates frechet distance between two curves defined by a list
# of coordinates in R^2 
from analyze import compression_factor

bucket_size = 200 / compression_factor

def frechet(song, hum, starts, octave=0):


	# calculates euclidean distance in R^2
	def euclid(p1,p2):
		return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)

	# octave displacement
	def octave_displace(tick, octave):
		if tick[1] == 0:
			return tick
		return (tick[0],tick[1] + (octave * 12))

	frechet_list = []
	# iterate over the hum list and calculate euclidean distance between
	# hum and every point in the song
	# frechet distance is the sum of the infs of these values
	# iterate over every start in the song
	for start in starts:
		# if the hum is longer than the length of the song from the start to
		# to the end, then we cannot compare
		song_clip = song[start:]
		# print len(song_clip)
		if len(hum) > len(song_clip):
			continue
		# store a list of minimum euclidean distances between each point in
		# the hum and every point in the song; the sum of the min_list will 
		# therefore be the frechet distance	
		min_list = []
		# for tick_h in hum:
		for x in xrange(0,len(hum)):
			if octave != 0:
				hum[x] = octave_displace(hum[x],octave)
			# this initial min_val uses the index in the distance	
			# min_val = (euclid((x,hum[x][1]),(x,song_clip[x][1])),song_clip[x][0],x)
			# this initial min_val normalizes the timestamps
			min_val = (euclid((hum[x][0] - hum[0][0],hum[x][1]),((song_clip[x][0]-song_clip[0][0]),song_clip[x][1])),song_clip[x][0],x)
			# iterate over song list to calculate minimum euclidean distance
			""" for y in xrange(max((x-bucket_size),0),min(x+bucket_size,len(song_clip))):
				new_dist = (euclid((x,hum[x][1]),(y,song_clip[y][1])),song_clip[y][0],y)
				if new_dist[0] < min_val[0]:
					min_val = new_dist """
			for y in xrange(max((x-bucket_size),0),min(x+bucket_size,len(song_clip))):
				new_dist = (euclid((hum[x][0]-hum[0][0],hum[x][1]),(song_clip[y][0]-song_clip[0][0],song_clip[y][1])),song_clip[y][0],y)
				if new_dist[0] < min_val[0]:
					min_val = new_dist
			min_list.append(min_val)
			# print "Distance at times (" + str(hum[x][0]) + "," + str(min_val[1]) + ") at indices (" + str(x) + "," + str(min_val[2]) + ") is " + str(min_val[0])

		# frechet_list.append(sum(min_list))
		frechet_list.append(sum(pair[0] for pair in min_list))
	# return the minimum frechet value for a hum matched to each section
	# of a song
	print frechet_list
	return min(frechet_list)

def frechet_plain(song,hum):
	def euclid(p1,p2):
		return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)
	min_list = []		
	for tick_h in hum:
		min_val = euclid(tick_h,song[0])
		for tick_s in song:
			new_dist = euclid(tick_h,tick_s)
			if new_dist < min_val:
				min_val = new_dist
		min_list.append(min_val)
	return sum(min_list) 

#tests
l1 = [(0,0),(1,1),(2,2)]
l2 = [(0,0),(1,.5),(2,1),(3,1.5),(4,2)]
l3 = [(1,.5),(2,1),(3,1.5),(4,2)]
starts = [0,1]

frechet_plain(l2,l1)
frechet_plain(l3,l1)
frechet(l2,l1,starts)



		

