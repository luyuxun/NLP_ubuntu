h_file = open('100_3','r')
#dummy one
dict = {'LU YuXun':-0.123}
for lines in h_file:
	l_str = lines.split(' ')
	#get the key
	dict_key = l_str[0]
	#preprocess the vector
	del l_str[0] #the first one, A.K.A the key
	del l_str[ len(l_str) - 1 ] #the '\n'
	vec = map(float, l_str) #get the vector
	dict[dict_key] = vec#build the dictionary
#	print 'the vec is:',dict[dict_key]
#	print 'the vect is',dict[dict_key]
#	print 'the key is',dict_key
	#dict.get('key','deafult') is another solution
#	print dict.has_key(dict_key)#judge if the dict has the key
#	raw_input('Press any key to continue')
h_file.close()
#After building the vector-dictionary

