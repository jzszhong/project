def getGainLoss(path1, path2):
    f1 = open(path1)
    f2 = open(path2)
    line1 = f1.readline()
    line2 = f2.readline()
    itvls = ["<-1", "-1~-0.75", "-0.75~-0.5", "-0.5~-0.25", "-0.25~0", "0~0.25", "0.25~0.5", "0.5~0.75", "0.75~1", ">1"]
    queries = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    while line1 and line2:
    	data1 = float((line1.split(" ")[-1]).split("\n")[0])
    	data2 = float((line2.split(" ")[-1]).split("\n")[0])
    	
    	# gain/loss for Q1 = (value_Q1_system_2 - value_Q1_system_1) / value_Q1_system_1
    	if (not data1 == 0):
    		cp = (data2 - data1) / data1
    		if (cp < -1):
    			queries[0] = queries[0] + 1
    		elif ((cp >= -1) and (cp < -0.75)):
    			queries[1] = queries[1] + 1
    		elif ((cp >= -0.75) and (cp < -0.5)):
    			queries[2] = queries[2] + 1
    		elif ((cp >= -0.5) and (cp < -0.25)):
    			queries[3] = queries[3] + 1
    		elif ((cp >= -0.25) and (cp < 0)):
    			queries[4] = queries[4] + 1
    		elif ((cp >= 0) and (cp < 0.25)):
    			queries[5] = queries[5] + 1
    		elif ((cp >= 0.25) and (cp < 0.5)):
    			queries[6] = queries[6] + 1
    		elif ((cp >= 0.5) and (cp < 0.75)):
    			queries[7] = queries[7] + 1
    		elif ((cp >= 0.75) and (cp < 1)):
    			queries[8] = queries[8] + 1
    		else:
    			queries[9] = queries[9] + 1
    	else:
    		cp = "infinity"
    		queries[9] = queries[9] + 1
    	
    	line1 = f1.readline()
    	line2 = f2.readline()
    	
    for i in range(10):
    	print(itvls[i] + "\t\t" + str(queries[i]))
    
    f1.close()
    f2.close()

# For task 2
getGainLoss("dataTFIDF.txt", "dataBM25.txt")

# For task 5
getGainLoss("dataTFIDF.txt", "dataTFIDFEmbedded.txt")