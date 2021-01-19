import numpy as np

y_actual = np.array ([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1])
y_predicted=np.array([1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0])

#Calculate Confusion Matrix
True_positive=0
False_positive=0
True_negative=0
False_negative=0

for i  in range (len(y_predicted)):
    if y_actual[i]==1 and y_predicted[i]==1:
        True_positive+=1
    elif y_actual[i]==0 and y_predicted[i]==0:
        True_negative+=1
    elif y_predicted[i]==1 and y_predicted[i]!=y_actual[i]:
        False_positive+=1
    elif y_predicted[i]==0 and y_predicted[i]!=y_actual[i]:
        False_negative+=1
print(True_positive, False_positive)
print(False_negative, True_negative)



    