# Python_Fifa_Dataset


There was no time to refactor the code this time! So a lot could have been done smarter and more pretty, we know!
SEE CODE: https://github.com/menjaw/Python_Fifa_Datasets/blob/master/Fifa%20questions.ipynb

#### QUESTION 1: The 3 most expensive teams according to player value.
    - ANSWER: Paris Saint-Germain and FC Barcelona is the most expensive teams 

| Club    		| Player        	   | Value 	    |
|:--------------------:	|:------------------------:| :-------------:|
|Paris Saint-Germain 	|Neymar da Silva Santos Jr.| 123000000.0    |
|FC Barcelona		|Lionel Messi		   | 105000000.0    |
|FC Barcelona 		|Luis Suárez		   | 97000000.0	    |



#### QUESTION 1: The 3 cheapest teams according to player value.
    - ANSWER: Need help or MORE TIME to put more information and conditions together and to remove result if the value is 0 

| Club    		| Player        	   | Value  | Python ID |
|:--------------------:	|:------------------------:| :-----:|:----------:
|NaN		 	|Oscar dos Santos Emboaba  | 0.0    | 163	|
|NaN		 	|Adrien S. Perruchet Silva | 0.0    | 168	|
|NaN		 	|Luis Suárez		   | 0.0    | 271	|



#### QUESTION 2: Which nationality is the most frequent amongst all players
    - ANSWER: England is the most frequent with 1631 players
    - Top 10 most frequent nationality amongst all players

| Nationality		| Amount   |
|:--------------------:	|:--------:|
|England         	|1631      |
|Germany        	|1147	   | 
|Spain          	|1020	   |
|France          	|966	   |
|Argentina       	|962	   |
|Brazil          	|806	   |
|Italy			|800	   |
|Colombia        	|593	   |
|Japan           	|471	   |
|Netherlands     	|430	   |



#### Question 3: What is the difference between the release clause and the value of top 10 most valuable players

    - ANSWER: Some of the cells didn't contained a number/value and that is the reason way we only show 7

| Club    		| Player        	       | Eur Value  | Release Clause | Difference |
|:--------------------:	|:----------------------------:|:----------:|:--------------:|:----------:|
|Real Madrid CF		|C. Ronaldo dos Santos Aveiro  | 95.500.000 | 195.800.000    |100.300.000 |
|FC Barcelona		|Lionel Messi		       | 105.000.000| 215.300.000    |110.300.000 |
|Paris Saint-Germain	|Neymar da Silva Santos Jr.    | 123.000.000| 236.800.000    |113.800.000 |
|FC Barcelona		|Luis Suárez		       | 97.000.000 | 198.900.000    |101.900.000 |
|FC Bayern Munich	|Robert Lewandowski	       | 92.000.000 | 151.800.000    |59.800.000  |
|Chelsea		|Eden Hazard		       | 90.500.000 | 174.200.000    |83.700.000  |
|Real Madrid CF		|Toni Kroos		       | 79.000.000 | 162.000.000    |83.000.000  |


#### Question 4: What is the frequency of age, height and weight for all players
 
| Frequency | Value   | Amount |
|:---------:|:-------:|:------:|
|Age 	    |25 years | 1515   |
|Height	    |178 cm   | 1204   |
|Weight	    |70 kg    | 1386   |


#### Question 5: How big is the average difference between value and wage of the players
   -ANSWER: We have used the values from the columns 'eur_value and eur_wage' and decided to show 10 results

| Player        	       | Eur Value  | Eur Wage       | Difference (value, wage)|Average (value, wage)|
|:----------------------------:|:----------:|:--------------:|:-----------------------:|:-------------------:|
|C. Ronaldo dos Santos Aveiro  | 95.500.000 | 565.000	     |94.935.000	       |48.032.500	     |
|Lionel Messi		       | 105.000.000| 565.000	     |104.435.000	       |52.782.500	     |
|Neymar da Silva Santos Jr.    | 123.000.000| 280.000	     |122.720.000	       |61.640.000	     |
|Luis Suárez		       | 97.000.000 | 510.000	     |96.490.000	       |48.755.000	     |
|Manuel Neuer		       | 61.000.000 | 230.000	     |60.770.000	       |30.615.000	     |
|Robert Lewandowski	       | 92.000.000 | 355.000	     |91.645.000	       |46.177.500	     |
|David De Gea Quintana	       | 64.500.000 | 215.000	     |64.285.000	       |32.357.500	     |
|Eden Hazard		       | 90.500.000 | 295.000	     |90.205.000	       |45.397.500	     |
|Toni Kroos		       | 79.000.000 | 340.000	     |78.660.000	       |39.670.000	     |
|NaN			       | 77.000.000 | 275.000	     |76.725.000	       |38.637.500	     |




