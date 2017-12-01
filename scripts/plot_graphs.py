import sys,os
import pickle
import matplotlib.pyplot as plt
import numpy as np
core_path = os.path.abspath('../new_model/')
sys.path.append(core_path)
#from core.plot import *
import seaborn as sns


# set the colors and styles of the plots
sns.set_context("paper", rc={"lines.linewidth": "2.5"})
sns.set(font_scale=2.5)
colors = ["windows blue", "pale red","amber","purple",  ]
sns.set_palette(sns.xkcd_palette(colors))
_lines = ['-', '--', '-',':']

def plot_vocab_growth(path):
    y_axis = "Proportion of words learned"
    x_axis = "Word types received"
    for i in range(4):
        plt.plot(num_heard[i], np.true_divide(learned_list[i], num_heard[i]), label = labels[i], linestyle= _lines[i])  
        
    plt.legend(loc="lower right")
    plt.ylim((0.0,1.0))
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title("Vocabulary Growth") 
    plt.savefig(path+"_vgrowth_curve")   
    plt.close()
        

def plot_learning_curve(path,t):
    plt.figure(figsize=(8,10))
    y_axis = "proportion of learned"
    x_axis = "Time"   
    time = np.arange(t)
    for i in range(4):
        plt.plot(time, np.true_divide(learned_list[i], num_heard[i])[:t], label = labels[i], linestyle= _lines[i])
    
    plt.legend(loc="lower right")
    plt.ylim((0.0,1.0))
    plt.xlim((0.0,t))
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    #plt.title("Learning Curve") 
    plt.savefig(path+"_learning_curve") 
    
    plt.close()
        
def plot_avg_acq_score(path,cat, t):
    '''
    Plot average acquisition score in time range t of a given category cat.
    category can be "nouns", "verbs", "learned", or "all" words
    '''
       
    plt.figure(figsize=(8,10))
    y_axis = "Average Acq Score of all the " + cat
    x_axis = "Time"   
    time = np.arange(t)
    print (t)
    for i in range(4):
            if cat == "nouns":
                    plt.plot(time, np.true_divide(noun_acq[i], noun_num_heard[i])[:t], label = labels[i], linestyle= _lines[i])
            elif cat == "verbs":
                    plt.plot(time, np.true_divide(verb_acq[i], verb_num_heard[i])[:t], label = labels[i], linestyle= _lines[i])
            elif cat == "learned":
                    plt.plot(time, np.true_divide(learned_acq[i], learned_list[i])[:t], label = labels[i], linestyle= _lines[i])
            else:
                    plt.plot(time, np.true_divide(all_acq[i], num_heard[i])[:t], label = labels[i], linestyle= _lines[i])
    
    plt.legend(loc="lower right")
    plt.ylim((0.0,1.0))
    plt.xlim((0.0,t))
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.savefig(path+"_"+str(t)+"_acg_acq_"+cat) 
    plt.close()


if len(sys.argv) != 3:
    print "not enough input arguments"
    exit(2)
else:
    try:
        alignment_model_path = sys.argv[1]
        time = int(sys.argv[2])
    except:
        print "Variable time is not a valid integer!"
        exit(2)

if alignment_model_path[-1] != '/':
    alignment_model_path += '/'

labels = ['word-comp','FAS', 'no-comp','ref-comp']
time_props_list = [ alignment_model_path + folder_name + '/plot_acq_score.pkl' for folder_name in labels]

num_heard = []
learned_list = []
noun_acq = []
verb_acq = []
learned_acq = []
all_acq = []
noun_num_heard = []
verb_num_heard = []
five_num_heard = []
ten_num_heard = []
five_qualified = []
five_tot_acq_sum = []
ten_qualified = []
ten_tot_acq_sum = []

# load all the numbers from the pickle file and 
for i in range(4):
    with open(time_props_list[i]) as outfile:
        print(time_props_list[i])
        num_heard.append(pickle.load(outfile))
        learned_list.append(pickle.load(outfile))
        noun_acq.append(pickle.load(outfile))
        verb_acq.append(pickle.load(outfile))
        learned_acq.append(pickle.load(outfile))
        all_acq.append(pickle.load(outfile))                   
        noun_num_heard.append(pickle.load(outfile))
        verb_num_heard.append(pickle.load(outfile))
        five_num_heard.append(pickle.load(outfile))
        ten_num_heard.append(pickle.load(outfile))
        five_qualified.append(pickle.load(outfile))
        five_tot_acq_sum.append(pickle.load(outfile))
        ten_qualified.append(pickle.load(outfile))
        ten_tot_acq_sum.append(pickle.load(outfile))
        
j = 0

abspath = os.path.abspath(alignment_model_path)
plot_path = abspath+'/plot/'
print plot_path
if not os.path.exists(plot_path):
    os.makedirs(plot_path)


#plot_vocab_growth('curr_plot/'+name)
plot_learning_curve(plot_path, time)    
#plot_avg_acq_score('plot/'+name, 'nouns',time)
#plot_avg_acq_score('plot/'+name, 'verbs', time)
#plot_avg_acq_score('plot/'+name, 'learned', time)
plot_avg_acq_score(plot_path, 'all',time)

