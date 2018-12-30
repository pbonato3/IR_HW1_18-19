import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# paths of the files containing the evaluations
eval_files_paths = []

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


#####################################################
# RETRIEVAL WITHOUT QUERY EXPANSION
#####################################################

eval_files_paths = ["./0/eval_0.txt", "./1/eval_1.txt", "./2/eval_2.txt", "./3/eval_3.txt"]

# load measures
load_eval(MAP = MAP, P_10 = P_10, RPrec = RPrec, files_path= eval_files_paths)
last_index = len(MAP[0]) - 1

# Print of the main statistics
print "MAP:   ", MAP[0][last_index], MAP[1][last_index], MAP[2][last_index], MAP[3][last_index]
print "P@10:  ", P_10[0][last_index], P_10[1][last_index], P_10[2][last_index], P_10[3][last_index]
print "RPrec: ", RPrec[0][last_index], RPrec[1][last_index], RPrec[2][last_index], RPrec[3][last_index]

# Print of the boxplots 
plt.boxplot([MAP[0][:last_index-1], MAP[1][:last_index-1], MAP[2][:last_index-1], MAP[3][:last_index-1]])
plt.title('Boxplot of Average Precision')
plt.ylabel('AP')
plt.xlabel('Run_#')
plt.show()

plt.boxplot([P_10[0][:last_index-1], P_10[1][:last_index-1], P_10[2][:last_index-1], P_10[3][:last_index-1]])
plt.title('Boxplot of P@10')
plt.ylabel('P_10')
plt.xlabel('Run_#')
plt.show()

plt.boxplot([RPrec[0][:last_index-1], RPrec[1][:last_index-1], RPrec[2][:last_index-1], RPrec[3][:last_index-1]])
plt.title('Boxplot of RPrec')
plt.ylabel('RPrec')
plt.xlabel('Run_#')
plt.show()

# Print of ANOVA statistics 
print "ANOVA 1-way, AP, all runs:" 
fvalue, pvalue = stats.f_oneway(MAP[0][:last_index-1], MAP[1][:last_index-1], MAP[2][:last_index-1], MAP[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, AP, BM25 runs:"  
fvalue, pvalue = stats.f_oneway(MAP[0][:last_index-1], MAP[2][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, AP, TF_IDF runs:"  
fvalue, pvalue = stats.f_oneway(MAP[1][:last_index-1], MAP[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print '\n'

print "ANOVA 1-way, P@10, all runs:" 
fvalue, pvalue = stats.f_oneway(P_10[0][:last_index-1], P_10[1][:last_index-1], P_10[2][:last_index-1], P_10[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, P@10, BM25 runs:"  
fvalue, pvalue = stats.f_oneway(P_10[0][:last_index-1], P_10[2][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, P@10, TF_IDF runs:"  
fvalue, pvalue = stats.f_oneway(P_10[1][:last_index-1], P_10[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue


print '\n'

print "ANOVA 1-way, RPrec, all runs:" 
fvalue, pvalue = stats.f_oneway(RPrec[0][:last_index-1], RPrec[1][:last_index-1], RPrec[2][:last_index-1], RPrec[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, RPrec, BM25 runs:"  
fvalue, pvalue = stats.f_oneway(RPrec[0][:last_index-1], RPrec[2][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, RPrec, TF_IDF runs:"  
fvalue, pvalue = stats.f_oneway(RPrec[1][:last_index-1], RPrec[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue





#####################################################
# RETRIEVAL WITH QUERY EXPANSION
#####################################################

print "\n RETRIEVAL WITH QUERY EXPANSION \n"

# paths of the files containing the evaluations
eval_files_paths = ["./0/eval_0_qe.txt", "./1/eval_1_qe.txt", "./2/eval_2_qe.txt", "./3/eval_3_qe.txt"]

# lists of lists:   [["eval_0_metrics"], ["eval_1_metrics"], ["eval_2_metrics"], ["eval_3_metrics"]]
MAP = []
P_10 = []
RPrec = []


# load measures
load_eval(MAP = MAP, P_10 = P_10, RPrec = RPrec, files_path= eval_files_paths)
last_index = len(MAP[0]) - 1


# Print of the main statistics
print "MAP:   ", MAP[0][last_index], MAP[1][last_index], MAP[2][last_index], MAP[3][last_index]
print "P@10:  ", P_10[0][last_index], P_10[1][last_index], P_10[2][last_index], P_10[3][last_index]
print "RPrec: ", RPrec[0][last_index], RPrec[1][last_index], RPrec[2][last_index], RPrec[3][last_index]

# Print of the boxplots 
plt.boxplot([MAP[0][:last_index-1], MAP[1][:last_index-1], MAP[2][:last_index-1], MAP[3][:last_index-1]])
plt.title('Boxplot of Average Precision')
plt.ylabel('AP')
plt.xlabel('Run_#')
plt.show()

plt.boxplot([P_10[0][:last_index-1], P_10[1][:last_index-1], P_10[2][:last_index-1], P_10[3][:last_index-1]])
plt.title('Boxplot of P@10')
plt.ylabel('P_10')
plt.xlabel('Run_#')
plt.show()

plt.boxplot([RPrec[0][:last_index-1], RPrec[1][:last_index-1], RPrec[2][:last_index-1], RPrec[3][:last_index-1]])
plt.title('Boxplot of RPrec')
plt.ylabel('RPrec')
plt.xlabel('Run_#')
plt.show()

# Print of ANOVA statistics 
print "ANOVA 1-way, AP, all runs:" 
fvalue, pvalue = stats.f_oneway(MAP[0][:last_index-1], MAP[1][:last_index-1], MAP[2][:last_index-1], MAP[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, AP, BM25 runs:"  
fvalue, pvalue = stats.f_oneway(MAP[0][:last_index-1], MAP[2][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, AP, TF_IDF runs:"  
fvalue, pvalue = stats.f_oneway(MAP[1][:last_index-1], MAP[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print '\n'

print "ANOVA 1-way, P@10, all runs:" 
fvalue, pvalue = stats.f_oneway(P_10[0][:last_index-1], P_10[1][:last_index-1], P_10[2][:last_index-1], P_10[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, P@10, BM25 runs:"  
fvalue, pvalue = stats.f_oneway(P_10[0][:last_index-1], P_10[2][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, P@10, TF_IDF runs:"  
fvalue, pvalue = stats.f_oneway(P_10[1][:last_index-1], P_10[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue


print '\n'

print "ANOVA 1-way, RPrec, all runs:" 
fvalue, pvalue = stats.f_oneway(RPrec[0][:last_index-1], RPrec[1][:last_index-1], RPrec[2][:last_index-1], RPrec[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, RPrec, BM25 runs:"  
fvalue, pvalue = stats.f_oneway(RPrec[0][:last_index-1], RPrec[2][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue

print "ANOVA 1-way, RPrec, TF_IDF runs:"  
fvalue, pvalue = stats.f_oneway(RPrec[1][:last_index-1], RPrec[3][:last_index-1])
print "F_value: " , fvalue , " P_value: ", pvalue
