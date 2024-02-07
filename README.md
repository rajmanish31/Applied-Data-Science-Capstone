# Applied Data Science Capstone
This Capstone project is part of [IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science) specialization on coursera, and it actually summarizes in the form of project all materials that have been learned during this specialization.

## Project Overview
The most prosperous business of the commercial space era, SpaceX has reduced the cost of space travel. On its website, the firm promotes Falcon 9 rocket flights, which start at 62 million dollars; in comparison, other suppliers charge up to 165 million dollars per launch; a large portion of the cost savings are attributable to SpaceX's ability to reuse the first stage. Thus, we can calculate the cost of a launch if we can ascertain if the first stage will land. We are going to make a prediction about whether SpaceX will reuse the first stage based on publicly available data and learning models.

## Questions to be answered
- How do variables such as payload mass, launch site, number of flights, and orbits affect the success of the first stage landing?
- Does the rate of successful landings increase over the years?
- What is the best algorithm that can be used for binary classification in this case?

## Methodology
**1. Data collection**
- Using SpaceX Rest API
- Web Scraping from [Wikipedia](https://en.wikipedia.org/w/index.php?title=List_of_Falcon_9_and_Falcon_Heavy_launches&oldid=1027686922) using Beautiful Soup

**2. Perform Data Wrangling**
- Filtering the data
- Dealing with missing values
- Using One Hot Encoding to prepare the data to a binary classification

**3. Perform EDA using SQL and Visualization,**

**4. Performed interactive visual analytics using Folium and Plotly Dash.**

**5. Performed predictive analysis using machine learning models**
- Building, tuning and evaluation of Logistic Regression, SVM, Decision Tree and KNN models to ensure the best results
- Achieved accuracy of 83% for Logistic Regression, SVM and KNN and 88% for Decesion Tree model.
