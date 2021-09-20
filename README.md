# Recruitment Analyser

As recruitment is one of the most important task for student’s & organizations as well. If there could be a model such that, it can predict the possibility of student to get recruited or placed in an organization or not, that can save lots of time of HR Managers , staffs & placement commitee.I focus on the specific point of developing a predictive machine learning model for identifying candidates who are likely to clear the recruitment process based on past data. This way, the recruiters can work only on such candidates, saving countless man-hours that multiple persons from multiple departments would otherwise spend on candidates that would eventually be rejected. This way, Talent Acquisition would not just improve on efficiency, but would also be better aligned with the overall business objectives of the company.

## Live Link

https://xrecruit.herokuapp.com/

## Novelty

1. Designed the complete frontend and backend.
2. Created dummy dataset for testing purpose.
3. Trained for different models.
4. Done hyperparameter tuning for xgboost
5. Only certain extensions allowed so that no invalid file has to be processed.
6. Live project that can be accessed from anywhere. 

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  pip install -r requirements.txt
  ```
### Installation

2. Clone the repo
   ```sh
   git clone https://github.com/zabhitak/recruitData
   ```
3. Install python packages
   ```sh
   pip install -r 
   ```
4. Run the project on localhost
   ```sh
   Visit http://localhost:****
   
   ```


## Technologies Used
1. Flask (Backend) 

![image](https://user-images.githubusercontent.com/42894689/133317407-dc868f47-fbcb-4799-be73-b25313e65b0d.png)

2. HTML (Frontend)

![image](https://user-images.githubusercontent.com/42894689/133317464-d798e31b-8622-46be-909c-a264e34b7d31.png)

3. CSS (Frontend)

![image](https://user-images.githubusercontent.com/42894689/133317498-05875c94-9f66-47c4-b2d3-bc5a09d1361b.png)

4. Heroku (Hosting website)

![image](https://user-images.githubusercontent.com/42894689/133317602-42753fcb-f12e-45b5-8983-715964902754.png)

## Steps Involved:

1. Open the web link
2. The files are pre-processed(removed duplicates and invalid entries) and best trained model is being imported.
3. User put its value for the given input
4. Output result will shown on the same page

## FlowChart Methodology

![image](https://user-images.githubusercontent.com/42894689/133927874-325233e7-5954-4c67-aa4c-ac148425976f.png)

## UI Screenshots

<img src="https://github.com/zabhitak/recruitData/blob/master/Screenshot/ui.PNG"  align="center" alt=""/>



## GIF showing process for one example:

![GP-Finder-Google-Chrome-2021-09](https://user-images.githubusercontent.com/42894689/133877523-f04ef32d-aa69-447d-b071-8f11b96956be.gif)

## Input example:

![image](https://user-images.githubusercontent.com/42894689/133873866-991ccd4e-15b2-4def-a470-a0bc1c6b5823.png)

![image](https://user-images.githubusercontent.com/42894689/133873892-91684f35-768f-43d8-8708-dbd9d6a57489.png)![image](https://user-images.githubusercontent.com/42894689/133873951-7cc75ca7-7e55-4848-95a9-47e0ed80bdbd.png)


## Output example:

![image](https://user-images.githubusercontent.com/42894689/133873803-c3861250-856d-426a-a65a-2880475e1b5d.png)

![image](https://user-images.githubusercontent.com/42894689/133873777-5e40c0d4-5f46-4bce-a255-ae5f05b129c0.png)


## Challenges

1. Google Authentication for third party apps: Allow access in security settings of your account.
2. File upload error for invalid files: Only allow certain extensions to be uploaded.
3. HTML template was not getting extended to other pages correctly: Use "{% block .. %}" and "{% endblock %}" to rectify.

## Future Scope

1. Account authentication for different users who use this website.

## Requirements

1. Working Internet connection (around 2 Mbps)
2. Mail account where you will receive the result.


## Creating dummy dataset to test the code
```
#Creating a csv
rollNumbers = []
marks = []
for i in range(0,357):
  if len(str(i)) == 1:
    rollNumbers.append('10180368' + str(i))
  elif len(str(i)) == 2:
    rollNumbers.append('1018037' + str(i))
  else:
    rollNumbers.append('101803' + str(i))
  marks.append(random.randrange(30, 100))

data = {}
data['roll'] = rollNumbers
data['marks'] = marks

finalDataset = pd.DataFrame.from_dict(data)
finalDataset.to_csv('scores.csv')
```

![image](https://user-images.githubusercontent.com/42894689/133393181-d7a2935f-1cd3-4995-b539-cd8e42279804.png)