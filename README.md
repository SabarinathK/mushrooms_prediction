Mushrooms Prediction
==============================
The Audubon Society Field Guide to North American Mushrooms contains descriptions
of hypothetical samples corresponding to 23 species of gilled mushrooms in the
Agaricus and Lepiota Family Mushroom (1981). Each species is labelled as either
definitely edible, definitely poisonous, or maybe edible but not recommended. This last
category was merged with the toxic category. The Guide asserts unequivocally that
there is no simple rule for judging a mushroom's edibility, such as "leaflets three, leave it
be" for Poisonous Oak and Ivy.
The main goal is to predict which mushroom is poisonous & which is edible.

About Dataset
-------------------------
This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one. The Guide clearly states that there is no simple rule for determining the edibility of a mushroom; no rule like "leaflets three, let it be'' for Poisonous Oak and Ivy.

URL: https://www.kaggle.com/uciml/mushroom-classification

 Approach:
-------------------------
- Data Description
    - We will be using Mushrooms Prediction Data Set present in Kaggle Repository. This Data set is 
    satisfying our data requirement. Total 8120 instances present in different batches of data.
    Export Data from DB to CSV for training
    We used MongoDB to push and pull over data for our model.
- Data Splitting 
   - We split the data here for our train and test data for further uses.
- Data Preprocessing
    - As our data is full of categorical values, so we convert all those to numerical values by label       encoding.
- Model Training 
    - We trained various model in our notebook and SVC was good on it. We trained with our processed 
    data.
- Model Evaluation 
    - Model evaluation done by classification and report was saved to .json file.
- Model Saving
    - we will save our modelsso that we can use them for prediction purpose.
- Push to app
   - Here we also create our Streamlit app and user interface and integrate our model with Streamlit and UI
- Data from client side for prediction purpose 
   - Now our application on cloud is ready for doing prediction. The prediction data which we receive from client side. 
- Data processing and Prediction
   - Client data will also go along the same process Data pre-processing and according to that we will 
    predict those data.
- Export Prediction to CSV
    - Finally, when we get all the prediction for client data, then our final task is toexport prediction to csv file and hand over it to client

Web Deployment
-------------------------
Mushrooms Prediction Web App : https://mushrooms--prediction.herokuapp.com/

Screenshots
-------------------------
- UI:
![Screenshot 2021-10-27 222214](https://user-images.githubusercontent.com/71809455/139208957-39844cca-9614-4ec8-bf39-a7e9f2750762.png)

- Prediction:
  ![Screenshot 2021-10-27 222411](https://user-images.githubusercontent.com/71809455/139209167-43be586a-b2b8-4d24-87ff-4fde0519a1f9.png)

High level design
-------------------------
URL : https://drive.google.com/file/d/1N8T-jlg5-ZyCgc3QWyFERe9TFpcwvPd7/view?usp=sharing
Low level design
-------------------------
URL :https://drive.google.com/file/d/1u7reWs63lQq2Bx9b9ojE_oeCwK4UR4-4/view?usp=sharing
Architecture
-------------------------
URL :https://drive.google.com/file/d/15FiOgBy9O9kp2dF1uXWHfgXiNlvGUdVd/view?usp=sharing
Detailed project report
-------------------------
URL :https://drive.google.com/file/d/1M9vuP95z0SMG180xEbfZhOiMOLMWQxmm/view?usp=sharing
Wireframe document
-------------------------
URL :https://drive.google.com/file/d/1xRCR-IUoTVoSX30oqZOyHpPVo75W33Up/view?usp=sharing
Demo video
-------------------------
URL : https://youtu.be/2rzbDF_cc88
Author
-------------------------
 - Sabarinath K [Linkedin](https://www.linkedin.com/in/sabarinath-k-bio/)







