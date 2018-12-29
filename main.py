import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# paths of the files containing the evaluations
eval_files_paths = ["./0/run_0_eval.txt", "./1/run_1_eval.txt", "./2/run_2_eval.txt", "./3/run_3_eval.txt"]

# lists of lists:   [["eval_0_metrics"], ["eval_1_metrics"], ["eval_2_metrics"], ["eval_3_metrics"]]
MAP = []
P_10 = []
RPrec = []


# function to load evaluation metrics as:  [["eval_0_metrics"], ["eval_1_metrics"], ["eval_2_metrics"], ["eval_3_metrics"]]
# takes 3 arrays and list of paths
# for every file loads:
#	AP for every query (plus MAP as last) in MAP array
# 	P@10 for every query (plus mean P@10 as last) in P_10 array
#	Rprec for every query (plus mean Rprec as last) in RPrec array

def load_eval(MAP, P_10, RPrec, files_path):
	# for every file given
	for path in files_path :
		# open it
		file = open(path, 'r')

		# initialize three empty lists
		map_list = []
		p_10_list = []
		rprec_list = []

		# for every line of the file
		for line in file:
			# split the line into tokens
			tok = line.split()
			# if the first token of the line is map append the third to map_list
			if tok[0] == "map" :
				map_list.append(float(tok[2]))
			# if the first token of the line is P_10 append the third to p_10_list
			if tok[0] == "P_10" : 
				p_10_list.append(float(tok[2]))
			# if the first token of the line is Rprec append the third to rprec_list
			if tok[0] == "Rprec" :
				rprec_list.append(float(tok[2]))

		# append list to the corresponding array
		MAP.append(map_list)
		P_10.append(p_10_list)
		RPrec.append(rprec_list)
		# close file
		file.close()


# load measures
load_eval(MAP = MAP, P_10 = P_10, RPrec = RPrec, files_path= eval_files_paths)
last_index = len(MAP[0]) - 1

#plt.plot(['Run_0', 'Run_1', 'Run_2', 'Run_3'],[MAP[0][last_index], MAP[1][last_index], MAP[2][last_index], MAP[3][last_index]])
#plt.ylabel('MAP')
#plt.title("MAP values per run")
#plt.show()

#plt.plot(['Run_0', 'Run_1', 'Run_2', 'Run_3'],[P_10[0][last_index], P_10[1][last_index], P_10[2][last_index], P_10[3][last_index]])
#plt.ylabel('P@10')
#plt.title("P@10 values per run")
#plt.show()


#plt.plot(['Run_0', 'Run_1', 'Run_2', 'Run_3'],[RPrec[0][last_index], RPrec[1][last_index], RPrec[2][last_index], RPrec[3][last_index]])
#plt.ylabel('RPrec')
#plt.title("RPrec values per run")
#plt.show()

plt.boxplot([MAP[0][:last_index-1], MAP[1][:last_index-1], MAP[2][:last_index-1], MAP[3][:last_index-1]])
plt.ylabel('MAP')
plt.xlabel('Run_#')
plt.show()

fvalue, pvalue = stats.f_oneway(MAP[0][:last_index-1], MAP[1][:last_index-1], MAP[2][:last_index-1], MAP[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue



