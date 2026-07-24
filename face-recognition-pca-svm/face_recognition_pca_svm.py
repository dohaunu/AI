import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_lfw_people
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix,ConfusionMatrixDisplay
import seaborn as sns
faces= fetch_lfw_people(min_faces_per_person=70,resize=0.4)
X =faces.data  
Y = faces.target 
images=faces.images
target_names=faces.target_names #list of persoon names 
h, w = images.shape[1:3] #height and width of the image 


#split data  into testing and training

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3, random_state=442)
#pca decomposition
pca=PCA(n_components=150,whiten=True,random_state=442).fit(X_train)
 #150 PCA Reduced features (principal components)
X_train_pca=pca.transform(X_train)
X_test_pca=pca.transform(X_test)
# Inverse transform to get reconstructed faces
X_test_reconstructed = pca.inverse_transform(X_test_pca)

#train SVM (support vector machine)on compressed images 
clf=SVC(kernel='rbf',class_weight='balanced')
clf.fit(X_train_pca, Y_train)  # Train SVM on PCA-reduced features
#clf.fit to train the svm(clf on the data)

#do the predictions and evaluate
Y_pred_pca=clf.predict(X_test_pca)
conf_mat=confusion_matrix(Y_test,Y_pred_pca,labels=range(len(target_names)))#y_pred are the estimated targets
#labels is a list of labels to index the matrix
display=ConfusionMatrixDisplay(confusion_matrix=conf_mat,display_labels=target_names)
display.plot(cmap='Greens',colorbar=False,xticks_rotation="vertical")
plt.title("confusion matrix")
print("\nClassification Results:")
print(f"Accuracy: {accuracy_score(Y_test, Y_pred_pca):.2%}")
print("\nDetailed Report:")
print(classification_report(Y_test, Y_pred_pca,target_names=target_names))
#visualization 
 
def plot_faces(images, titles, h, w, n_row=3, n_col=5, title_sup=None):
    plt.figure(figsize=(1.8*n_col,2.4*n_row))
    for i in range(n_row*n_col):
        if i >= len(images):
            break
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=10)
        plt.xticks(())
        plt.yticks(())
    if title_sup:
        plt.suptitle(title_sup, fontsize=16)
    plt.tight_layout()
    plt.show()

# Show original faces
plot_faces(X_test, [target_names[Y] for Y in Y_test], h, w, title_sup="Original Faces")
#show data after compression 
plot_faces(X_test_reconstructed,[target_names[Y] for Y in Y_test],h,w,title_sup="Reconstructed Faces(PCA Compression)")
# Show predicted results
titles_pred = [f"True: {target_names[true]}\nPred: {target_names[pred]}" for true, pred in zip(Y_test, Y_pred_pca)]
plot_faces(X_test, titles_pred, h, w, title_sup="Classification Results (True vs Predicted)")
