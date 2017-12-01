import pickle
import copy
import sys

FIVE = 5
TEN = 10

'''
- Average acquisition score of all words that encountered
             at some time point before t
- Average acquisition score of words learned at some time 
            point before t
- Average acquisition score of all nouns encountered at some
            time point before t
- Average acquisition score of all verbs encountered at some 
            time point before t
'''
def main():
    if len(sys.argv) == 2:
            path = sys.argv[1]
    else:
        print 'not enough arguments'
        exit()
    #temp = path.split('/')[-2]
    
    if path[-1] != '/':
        path += '/'
    with open(path+ 'acq_score_timestamp.pkl') as infile:
        acq_timestamp = pickle.load(infile)
        updated_acq_timestamp = copy.deepcopy(acq_timestamp)

    five_qualified = []
    ten_qualified = []
    
    curr_t = 1
    time = 20000
    heard = set()
    num_heard = []
    five_num_heard = []
    ten_num_heard = []
    noun_num_heard = []
    verb_num_heard = []
    learned_list = []
    noun_acq = []
    verb_acq = []
    learned_acq = []
    all_acq = []
    five_heard = set()
    ten_heard = set()
    learned = set()
    
    while curr_t <= time:
            five_qualified_num = 0
            ten_qualified_num = 0
            five_tot_acq_sum = 0
            ten_tot_acq_sum = 0
            
            noun_num = 0
            verb_num = 0
            noun_tot_acq_sum = 0
            verb_tot_acq_sum = 0
            
            learned_num = 0
            learned_tot_acq_sum = 0
            
            all_tot_acq_sum = 0
            
            
            for key in acq_timestamp.keys():
                    #print(key)
                    
                    occurence = sorted(updated_acq_timestamp[key].keys())
                    
                    # find the largest time before time t that the word appears
                    sorted_timestamp = sorted(acq_timestamp[key].keys())
                   
                    total_occur_before = len([t for t in sorted_timestamp if t <= curr_t])
                    curr_acq = acq_timestamp[key][occurence[0]]
                     
                    if len(occurence) > 0 and occurence[0] <= curr_t:
                            heard.add(key)
                            all_tot_acq_sum += curr_acq
                            # noun 
                            if key.endswith('N'):
                                    noun_num += 1
                                    noun_tot_acq_sum += curr_acq
                            # verb
                            elif key.endswith('V'):
                                    verb_num += 1
                                    verb_tot_acq_sum += curr_acq
                            # learned
                            if curr_acq >= 0.7:
                                    learned.add(key)
                                    learned_tot_acq_sum += curr_acq
                            # if the acquisition score is no longer greater than 0.7
                            # remove it from learned words
                            elif key in learned:
                                    learned.remove(key)
                            
                            # frequency < 5
                            if total_occur_before < FIVE:
                                    five_heard.add(key)
                                    
                                    if curr_acq >= 0.7:
                                            # five_qualified -> low frequency learned words 
                                            five_qualified_num += 1
                                            five_tot_acq_sum += curr_acq
                            elif key in five_heard:
                                    five_heard.remove(key)
    
                            # frequnecy > 10
                            if total_occur_before > TEN:
                                    ten_heard.add(key)
                                    
                                    if curr_acq >= 0.7:
                                            # ten_qualified -> high frequency learned words
                                            ten_qualified_num += 1
                                            ten_tot_acq_sum += curr_acq
                                            
                            elif key in ten_heard:
                                    ten_heard.remove(key)
                        
                        # update the acquisition score according to the state
                    if len(occurence) > 1 and (occurence[1] == curr_t + 1):
                            updated_acq_timestamp[key].pop(occurence[0])
                    
    
            num_heard.append(len(heard))
            learned_list.append(len(learned))
            all_acq.append(all_tot_acq_sum)
            learned_acq.append(learned_tot_acq_sum)
            five_num_heard.append(len(five_heard))
            ten_num_heard.append(len(ten_heard))
            noun_acq.append(noun_tot_acq_sum)
            verb_acq.append(verb_tot_acq_sum)
            noun_num_heard.append(noun_num)
            verb_num_heard.append(verb_num)
            five_qualified.append(five_qualified_num)             
            ten_qualified.append(ten_qualified_num)               

            #vocab_growth_at_t.append((len(heard), ratio))
            print(path, curr_t)
            curr_t += 1
       
        
    
    with open(path+'plot_acq_score.pkl','wb') as outfile:
            pickle.dump(num_heard, outfile)
            pickle.dump(learned_list, outfile)
            pickle.dump(noun_acq, outfile)
            pickle.dump(verb_acq, outfile)
            pickle.dump(learned_acq, outfile)
            pickle.dump(all_acq, outfile)                
            pickle.dump(noun_num_heard, outfile)
            pickle.dump(verb_num_heard, outfile)
            pickle.dump(five_num_heard, outfile)
            pickle.dump(ten_num_heard, outfile)
            pickle.dump(five_qualified, outfile)
            pickle.dump(five_tot_acq_sum, outfile)
            pickle.dump(ten_qualified, outfile)
            pickle.dump(ten_tot_acq_sum, outfile)
        
        
if __name__ == "__main__":
        
        main()

