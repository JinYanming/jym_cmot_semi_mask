import numpy as np
from Common.list2array import lists2array
def mot_tracklet_confidence_update(tracklet=None,param=None,lambda_=None,*args,**kwargs):

    
    if lambda_ == None:
        lambda_=1.2
    
    ## Tracklet confidence update
    
    hyp_score= np.array((tracklet.hyp.score))
    L_T=0
    ass_idx=[]
    hyp_score_length = len(hyp_score)
    for ii in range(0,len(hyp_score)):
        ii = hyp_score_length - ii -1#reverse the range list
        if hyp_score[ii] == 0:
            break
        L_T=L_T + 1
        ass_idx.append(ii)
    ass_idx = np.array(ass_idx).astype(np.int)
    L_T_backwards = lambda x:1/x if x !=0 else np.Inf
    Conf_prob=np.dot(np.dot(L_T_backwards(L_T),np.sum(hyp_score[ass_idx])),(1 - np.exp(np.dot(- lambda_,np.sqrt(L_T)))))
    tracklet.Conf_prob = Conf_prob
    tracklet.Cont_Asso = L_T
    
    return tracklet
    
if __name__ == '__main__':
    pass
