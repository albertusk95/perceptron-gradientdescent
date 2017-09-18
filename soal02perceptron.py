w0 = 0
w1 = 0
w2 = 0
w3 = 0
w4 = 0

x = []
x.append([])
x.append([])
x.append([])
x.append([])
x.append([])
x.append([])

x[0].append(1)
x[0].append(5.1)
x[0].append(3.5)
x[0].append(1.4)
x[0].append(0.2)
x[0].append(1)

x[1].append(1)
x[1].append(4.9)
x[1].append(3)
x[1].append(1.4)
x[1].append(0.2)
x[1].append(1)

x[2].append(1)
x[2].append(4.7)
x[2].append(3.2)
x[2].append(1.3)
x[2].append(0.2)
x[2].append(1)

x[3].append(1)
x[3].append(7)
x[3].append(3.2)
x[3].append(4.7)
x[3].append(1.4)
x[3].append(-1)

x[4].append(1)
x[4].append(6.4)
x[4].append(3.2)
x[4].append(4.5)
x[4].append(1.5)
x[4].append(-1)

x[5].append(1)
x[5].append(6.9)
x[5].append(3.1)
x[5].append(4.9)
x[5].append(1.5)
x[5].append(-1)


learningRate = 0.1
threshold = 0.01

squaredDiff = []		
squaredDiff.append([])
squaredDiff.append([])
squaredDiff.append([])
squaredDiff.append([])
squaredDiff.append([])
squaredDiff.append([])

# menghitung total perkalian bobot dengan nilai atribut
iteration = 0
while 1:

	print ('ITERATION: %d' % (iteration))
	print '\n'
	
	idxOfInstance = 0

	while idxOfInstance < 6:

		print ('Instance ke: %d' % (idxOfInstance))
		print '\n'

		print 'Bobot saat ini'
		print ('[%f, %f, %f, %f, %f]' % (w0, w1, w2, w3, w4))
		print '\n'

		# instance ke-n
		totalMultiplyOfWeightAndValue = (w0 * x[idxOfInstance][0]) + (w1 * x[idxOfInstance][1]) + (w2 * x[idxOfInstance][2]) + (w3 * x[idxOfInstance][3]) + (w4 * x[idxOfInstance][4])

		print 'Menghitung perkalian bobot dengan nilai atribut'
		print ('(%f * %f) + (%f * %f) + (%f * %f) + (%f * %f) + (%f * %f)' % (w0, x[idxOfInstance][0], w1, x[idxOfInstance][1], w2, x[idxOfInstance][2], w3, x[idxOfInstance][3], w4, x[idxOfInstance][4]))

		# output
		outputNetwork = 0
		if totalMultiplyOfWeightAndValue > 0:
			outputNetwork = 1
		elif totalMultiplyOfWeightAndValue == 0:
			outputNetwork = 0
		else:
			outputNetwork = -1


		print ('Hasil: %f' % (outputNetwork))
		print '\n'


		# perubahan nilai bobot
		if outputNetwork != x[idxOfInstance][5]:
			print 'Nilai output tidak sama dengan target'
			print 'Menghitung perubahan nilai bobot'
			print 'Rumus: Wi = Wi + learningRate * (target - output) * Xi'
			
			print ('w0 = %f + (%f * (%d - %f) * %f)' % (w0, learningRate, x[idxOfInstance][5], outputNetwork, x[idxOfInstance][0]))
			w0 = w0 + (learningRate * (x[idxOfInstance][5] - outputNetwork) * x[idxOfInstance][0])
			print ('w0 = %f' % (w0))

			print ('w1 = %f + (%f * (%d - %f) * %f)' % (w1, learningRate, x[idxOfInstance][5], outputNetwork, x[idxOfInstance][1]))
			w1 = w1 + (learningRate * (x[idxOfInstance][5] - outputNetwork) * x[idxOfInstance][1])
			print ('w1 = %f' % (w1))

			print ('w2 = %f + (%f * (%d - %f) * %f)' % (w2, learningRate, x[idxOfInstance][5], outputNetwork, x[idxOfInstance][2]))
			w2 = w2 + (learningRate * (x[idxOfInstance][5] - outputNetwork) * x[idxOfInstance][2])
			print ('w2 = %f' % (w2))

			print ('w3 = %f + (%f * (%d - %f) * %f)' % (w3, learningRate, x[idxOfInstance][5], outputNetwork, x[idxOfInstance][3]))
			w3 = w3 + (learningRate * (x[idxOfInstance][5] - outputNetwork) * x[idxOfInstance][3])
			print ('w3 = %f' % (w3))

			print ('w4 = %f + (%f * (%d - %f) * %f)' % (w4, learningRate, x[idxOfInstance][5], outputNetwork, x[idxOfInstance][4]))
			w4 = w4 + (learningRate * (x[idxOfInstance][5] - outputNetwork) * x[idxOfInstance][4])
			print ('w4 = %f' % (w4))

		else:
			print 'Nilai output sama dengan target'
			print 'Tidak perlu melakukan perubahan nilai bobot'

		print '\n'

		squaredDiff[idxOfInstance] = (x[idxOfInstance][5] - outputNetwork) * (x[idxOfInstance][5] - outputNetwork)
		
		print 'Menghitung kuadrat dari instance error'
		print 'Rumus: Error = (target - output) ^ 2'
		print ('Error = (%f - %f) * (%f - %f)' % (x[idxOfInstance][5], outputNetwork, x[idxOfInstance][5], outputNetwork))
		print ('Error = %f' % (squaredDiff[idxOfInstance]))
		print '\n'

		idxOfInstance = idxOfInstance + 1


	# kumulatif error
	cumError = 0.5 * (squaredDiff[0] + squaredDiff[1] + squaredDiff[2] + squaredDiff[3] + squaredDiff[4] + squaredDiff[5])

	print 'Menghitung error kumulatif'
	print ('Cumulative Error = 0.5 * (%f + %f + %f + %f + %f + %f)' % (squaredDiff[0], squaredDiff[1], squaredDiff[2], squaredDiff[3], squaredDiff[4], squaredDiff[5]))
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