w0 = 0
w1 = 0
w2 = 0
w3 = 0

x = []
x.append([])
x.append([])
x.append([])

x[0].append(1)
x[0].append(1)
x[0].append(0)
x[0].append(1)
x[0].append(-1)

x[1].append(1)
x[1].append(0)
x[1].append(-1)
x[1].append(-1)
x[1].append(1)

x[2].append(1)
x[2].append(-1)
x[2].append(-0.5)
x[2].append(-1)
x[2].append(1)


learningRate = 0.1
threshold = 0.01

squaredDiff = []		
squaredDiff.append([])
squaredDiff.append([])
squaredDiff.append([])

deltaW = []
deltaW.append([])
deltaW.append([])
deltaW.append([])
deltaW.append([])

iteration = 0

while 1:

	print ('ITERATION: %d' % (iteration))
	print '\n'
	
	# initialize deltaW = 0
	deltaW[0] = 0
	deltaW[1] = 0
	deltaW[2] = 0
	deltaW[3] = 0

	idxOfInstance = 0

	while idxOfInstance < 3:

		print ('Instance ke: %d' % (idxOfInstance))
		
		print '\n'

		print 'Bobot saat ini'
		print ('[%f, %f, %f, %f]' % (w0, w1, w2, w3))

		print '\n'

		# instance ke-n
		totalMultiplyOfWeightAndValue = (w0 * x[idxOfInstance][0]) + (w1 * x[idxOfInstance][1]) + (w2 * x[idxOfInstance][2]) + (w3 * x[idxOfInstance][3])

		# total perkalian bobot dengan nilai atribut
		print 'Menghitung perkalian bobot dengan nilai atribut'

		print ('(%f * %f) + (%f * %f) + (%f * %f) + (%f * %f)' % (w0, x[idxOfInstance][0], w1, x[idxOfInstance][1], w2, x[idxOfInstance][2], w3, x[idxOfInstance][3]))

		# output
		outputNetwork = totalMultiplyOfWeightAndValue

		print ('Hasil: %f' % (outputNetwork))

		print '\n'

		# menghitung perubahan dari deltaW
		print 'Menghitung perubahan dari deltaW'
		print 'Rumus: deltaWi = deltaWi + learningRate * (target - output) * Xi'
	
		attrIdx = 0
	
		while attrIdx < 4:
			print ('deltaW[%d] = %f + (%f * (%f - %f) * %f)' % (attrIdx, deltaW[attrIdx], learningRate, x[idxOfInstance][4], outputNetwork, x[idxOfInstance][attrIdx])) 
			
			deltaW[attrIdx] = deltaW[attrIdx] + (learningRate * (x[idxOfInstance][4] - outputNetwork) * x[idxOfInstance][attrIdx]) 
			
			print ('deltaW[%d]: %f' % (attrIdx, deltaW[attrIdx]))

			attrIdx = attrIdx + 1


		print '\n'

		squaredDiff[idxOfInstance] = (x[idxOfInstance][4] - outputNetwork) * (x[idxOfInstance][4] - outputNetwork)
		
		print 'Menghitung kuadrat dari instance error'
		print 'Rumus: Error = (target - output) ^ 2'
		print ('Error = (%f - %f) * (%f - %f)' % (x[idxOfInstance][4], outputNetwork, x[idxOfInstance][4], outputNetwork))
		print ('Error = %f' % (squaredDiff[idxOfInstance]))

		print '\n'

		idxOfInstance = idxOfInstance + 1


	# menghitung perubahan W asli
	print 'Menghitung perubahan pada W'
	print 'Rumus: Wi = Wi + deltaWi'
	print ('W0 = %f + %f' % (w0, deltaW[0]))
	w0 = w0 + deltaW[0]
	print ('W0 = %f' % (w0))

	print ('W1 = %f + %f' % (w1, deltaW[1]))
	w1 = w1 + deltaW[1]
	print ('W1 = %f' % (w1))

	print ('W2 = %f + %f' % (w2, deltaW[2]))
	w2 = w2 + deltaW[2]
	print ('W2 = %f' % (w2))

	print ('W3 = %f + %f' % (w3, deltaW[3]))
	w3 = w3 + deltaW[3]
	print ('W3 = %f' % (w3))

	print '\n'

	# kumulatif error
	cumError = 0.5 * (squaredDiff[0] + squaredDiff[1] + squaredDiff[2])

	print 'Menghitung error kumulatif'
	print ('Cumulative Error = 0.5 * (%f + %f + %f)' % (squaredDiff[0], squaredDiff[1], squaredDiff[2]))
	print ('Cumulative Error = %f' % (cumError))

	print '\n'

	#n = raw_input()

	iteration = iteration + 1

	if cumError < threshold:
		print 'Kumulatif error < threshold'
		print 'Stop iterasi'
		print '\n'
		break
	else:
		print 'Kumulatif error > threshold'
		print 'Melanjutkan iterasi'
		print '\n'

	print '------------------------------------------------------------------------'

	print '\n'
