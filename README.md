## Deploy Image classification platform

Go to [my personal website](https://dukesky.github.io/app/index.html) and ML platform [page]() to test these functions!

This is a image project I did when I study serverless and apply machine learning in AWS. \
You can check my other serverless project about [price prediction model](https://github.com/dukesky/Tutorial_of_Deploy_Serverless_ML_Model) and [Word Recognition model](https://github.com/dukesky/Deployment_of_word_recognition_nlp_platform) \

In this project, I built several serverless functions to process and classify image. I used [Restnet](https://keras.io/api/applications/resnet/#resnet50-function) and [Inception](https://keras.io/api/applications/inceptionv3/) model from [keras](https://keras.io/) to process and predict images.

### Step1: use Jupyter notebook to create project 
Just like your normal data science project with jupyter notebook, coding with what you used, processing data, build model and analysis result.

### Step2: create serverless framework
go to project folder in command line and type: \
`sls create --template aws-python3 --name project_name`  \
`sls plugin install -n serverless-python-requirements`  \
Make sure you have already install `npm` and `serverless` before. If not, you can click here to install [node.js](https://nodejs.org/en/) and [serverless](https://www.serverless.com/framework/docs/getting-started/)

### Step3: edit handler.py
Add functions we want to used as APIs in AWS server

### Step4: config serverless.yml file
Edit serverless.yml, define functions we used in AWS server


### Step5: add requirements.txt file
add all required pakage in requirements.txt file \
To test if model is worked prooerly in local,  type: \
`sls invoke local --function function-you-want-to-test --path data-you-want-to-input`

### Step6: Deploy
To deploy the serverless framwork, we simply need type `sls deploy`
After deploy,To test if model is worked properly in AWS, we can use invoke function to test input and output by typing:   \
`sls invoke --function function-you-want-to-test --path data-you-want-to-input --log`


### NOT FINISHED YET
currently, this model is not finished yet, I still have some problem with lambda upload size, because tensorflow plus keras are larger than lambda capacity(200M) and tem/ folder capacity(500M), I'm trying to figure out how to upload these packages without fill all space

I learned this project from [udemy](https://www.udemy.com/) course [Deploy Serverless Machine Learning Models to AWS Lambda](https://www.udemy.com/course/deploy-serverless-machine-learning-models-to-aws-lambda/)