

colors = [	['green', 'green', 'green'],
			['green','red','red'],
			['green','green','green']]
measurement = ['red', 'red']
motions = [[0, 0], [0, 1]]
sensor_right = 1.0
p_move = 0.5

#initialisig

sensor_wrong = 1-sensor_right
size_h=len(colors[0])
size_v=len(colors)
#uniform p
p = [[1./(size_h*size_v) for column in range(size_h)] for row in range(size_v)]


def sense(p,Z):
	q=[[0 for column in range(size_h)] for row in range(size_v)]

	for i in range(size_v):
		for j in range(size_h):
			hit = colors[i][j] == Z;
			q[i][j] = (hit*sensor_right + sensor_wrong * (1-hit)) *p[i][j]
	s= sum(sum(i) for i in q)
	for i in range(size_v):
		for j in range(size_h):
			q[i][j] = q[i][j]/s
	return q

def move(p,U):
	q=[[0 for column in range(size_h)] for row in range(size_v)]

	for i in range(size_v):
		for j in range(size_h):
			s = p_move * p[(i-U[0]) % size_h ][(j-U[1]) % size_v]
			s = s + (1-p_move) * p[i][j]
			q[i][j] = s
	return q





results=p
for i in range(len(measurement)):
	results = sense(results,measurement[i])
	results = move(results,motions[i])
print(sense(results,measurement[0]))
