
# Option: 6) Serving with REST APIs( Python Flask ) 

# Devlopment of AI application and classification:

AI algorithms will be used in an increasing number of commonplace applications in the future. For instance, you might want to incorporate an image classifier into a mobile application. As part of the broader application design, you would employ a deep learning model that had been trained on hundreds of thousands of photos to accomplish this.The use of these kinds of models as standard components of applications will make up a sizable portion of software development in the future. You will train an image classifier in this project to identify several flower species.

### COLAB NOTEBOOK: 
https://colab.research.google.com/drive/1WVUu3SfG6LjkPxjWs8QWBHlGsUsWU5sH#scrollTo=s2FFmHRz2zpR

### Modele training and AI Application classification steps are as :
https://github.com/shubhadapaithankar/255-Bonous-Work/blob/main/Flower_classifier-Notebook.ipynb


# Building and training the classifier 

To build and train the classifier.Used one of the pretrained models from torchvision.models to get the image features. Build and train a new feed-forward classifier using those features.

1. Load a pre-trained network 
2. Define a new, untrained feed-forward network as a classifier, using ReLU activations and dropout
3. Train the classifier layers using backpropagation using the pre-trained network to get the features
4. Track the loss and accuracy on the validation set to determine the best hyperparameters

Click the like for more Detail Information about model prediction : <a href="https://colab.research.google.com/drive/1WVUu3SfG6LjkPxjWs8QWBHlGsUsWU5sH#scrollTo=s2FFmHRz2zpR/" target="_blank">GOOGLE COLAB</a>

<img width="743" alt="Screen Shot 2022-11-19 at 5 30 46 PM" src="https://user-images.githubusercontent.com/99461999/202878494-72734e4a-42b0-42ad-8484-f6617790abe3.png">


# FLOWER CLASSIFIER WEBAPP

`Application can receive multiple request at a single time and predict the result`

This neural network web application shows how the network was trained and tested with a `98.6% accuracy rate`. The neural network is trained to categorize photos of flowers using the pretrained resnet152 algorithm. It was created with the Pytorch framework and primarily in Python. Flask is used to build the web application.

## Neural Network used : 
[Resnet152](https://resources.wolframcloud.com/NeuralNetRepository/resources/ResNet-152-Trained-on-ImageNet-Competition-Data)    
[Network Layers in Pytorch](https://github.com/pytorch/vision/blob/master/torchvision/models/resnet.py)        
* You can dowload ResNet152 [here](https://www.kaggle.com/pytorch/resnet152)    
* You can download overall modified model [here](https://github.com/souravs17031999/FLOWER-CLASSIFIER-WEBAPP/blob/master/classifier.pt)    

![resnet152](/static/resnet.gif)   

## Refresher on Neural Network :
[Gradient Descent](https://medium.com/secure-and-private-ai-writing-challenge/playing-with-gradient-descent-intuition-e5bde385078)   
[Backpropogation](https://medium.com/secure-and-private-ai-writing-challenge/playing-with-backpropagation-algorithm-intuition-10c42578a8e8)       

## Flow :
* Input image is fed and transformed using : [commons.py](https://github.com/souravs17031999/FLOWER-CLASSIFIER-WEBAPP/blob/master/commons.py)     
* Inference is done by : [inference.py](https://github.com/souravs17031999/FLOWER-CLASSIFIER-WEBAPP/blob/master/inference.py)         





https://user-images.githubusercontent.com/99461999/202879351-f77937d2-e736-4d02-b69d-3bead75c35da.mov




## Complete flow :    


* `Application can receive multiple request at a single time and predict the result`

https://user-images.githubusercontent.com/99461999/202879871-a07e4e2b-839c-44d3-a814-a47aa046ced9.mov


https://user-images.githubusercontent.com/99461999/202816997-ef2fff87-a1e8-4048-960e-2e07c3369031.mov


## Running Steps - 
Make sure you have installed Python , Pytorch and flask.

* _First download all the folders and files_     
`git clone git@github.com:shubhadapaithankar/255-Bonous-Work.git` 

* _Download pretrained weights and keep it in the same Project directory_ [Download here](https://www.kaggle.com/souravs17031999/flowerclassifierudacitypretrainedweights).       
* _Then open the command prompt (or powershell) and change the directory to the path where all the files are located._       
`cd 255-Bonous-Work`      
*  Download `classifier.pt` file from  https://drive.google.com/file/d/1WqCFwvu-ZiVfYEtiqeTG1ZenOQ62p98q/view?usp=sharing
* _Now run the following commands_ -   
     

`export FLASK_APP=flower.py`   

`python3 -m flask run`      


This will firstly download the models and then start the local web server.

now go to the local server something like this - http://127.0.0.1:5000/ and see the result and explore.

<img width="1440" alt="Screen Shot 2022-11-18 at 2 31 56 PM" src="https://user-images.githubusercontent.com/99461999/202814214-fd51cef3-af91-4b57-9e47-ce983c24a04b.png">

<img width="1439" alt="Screen Shot 2022-11-18 at 3 01 10 PM" src="https://user-images.githubusercontent.com/99461999/202817215-fe3b98d9-cd45-4697-a1ef-5919885cc3fb.png">
