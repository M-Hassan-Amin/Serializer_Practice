#####################  Normal ###########################

CDmodel = tf.keras.models.load_model('ecg(Normal(2lablesspliting)).h5')

#####################  MI ###########################

labellist = ['SA', 'SNR']
labelonehot = {"SA":[0],"SNR":[1]}



trainobj = {"SA":[],"SNR":[]}
answerobj = {"SA":[],"SNR":[]}
    
for k in labellist:
    
    finaldisease = []
    finaldiseaselabels = []
    newdata = an[an["subglass"]==k]
    for sub,filename in zip(newdata['subglass'],
    newdata['filename']):
        files = eval(filename)
        print(sub)
        print(len(files))
        
        
        ##read signal one by one
        nopick = 0
        for sig in files:
            path = f"allfolders/{sub}/{sig.split('.')[0]}"
            #print(path)
            data = wfdb.rdsamp(path)[0]
            
            #print(data.shape,type(data))
            
            if data.shape[0] == 5000:
                finaldisease.append(data)
                finaldiseaselabels.append(labelonehot[k])
                #print("pick")
                
            else:
                #print("no pick")
                nopick+=1
                
        print("no of notpicking",nopick)
        print('------------------------------------')
    
    
    trainobj[k] = finaldisease
    answerobj[k] = finaldiseaselabels






combinedata = np.array(trainobj["SA"] + trainobj["SNR"] )
combinelabels = np.array(answerobj["SA"] + answerobj["SNR"] )





import numpy
from sklearn.model_selection import train_test_split
Normal_X_train, Normal_X_test, Normal_y_train, Normal_y_test = train_test_split(combinedata, combinelabels, test_size=0.33, random_state=42)




len(Normal_X_test), len(Normal_y_test)

##single prediction
correct = []
wrong = []


for i in range(len(Normal_X_test)):
    inp = np.array([Normal_X_test[i]])
    Pr = CDmodel.predict(inp)
    result = np.argmax(Pr)
    if result == 0 and Normal_y_test[i][0] == 0:
        correct.append(result)
        print("--------------- Correct Prediction ---------------")
        print("Prediction is SA : ", result, "        Actual is SA : ", Normal_y_test[i][0])
        
        
    elif result == 0 and Normal_y_test[i][0] == 1:
        wrong.append(result)
        print("--------------- Wrong Prediction ---------------")
        print("Prediction is SA : ", result, "        Actual is SNR : ", Normal_y_test[i][0])
        
    elif result == 1 and Normal_y_test[i][0] == 0:
        wrong.append(result)
        print("--------------- Wrong Prediction ---------------")
        print("Prediction is SNR : ", result, "        Actual is SA : ", Normal_y_test[i][0])
    
    elif result == 1 and Normal_y_test[i][0] == 1:
        correct.append(result)
        print("--------------- Correct Prediction ---------------")
        print("Prediction is SNR : ", result, "        Actual is SNR : ", Normal_y_test[i][0])


print("correct",len(correct)/len(Normal_X_test))
print("wrong",len(wrong)/len(Normal_X_test))
        
