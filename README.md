# Outfit Generator
A non-deterministic Baysian-based  MAB outfit generator for clothes.


## Install the requirements

```
virutalenv env -p python3.8
source env/bin/activate
pip install -r requirements.txt 
export FLASK_APP=app
```

## Launch the service

```
flask run
```


## Launch a live scenario

```
cd generator
behave
```

will trigger a scenario like:

```
Scenario: Users reward the "hipster" outfit the most with heavy dominance on specific items

 Given the outfit generator is live on the website

 When users buy the "hipster" outfit 250 times with top 60536077, trousers 60519768 and shoes 60478094
 And users buy the "formal" outfit 50 times with top 60476826, trousers 22531116 and shoes 60168873
 Then we generate a HTML scenario_formal_1 file with a new outfit
```

It generates a HTML with exploitation/exploration colour code for both outfit (title) and articles (borders).
Red is for exploitation, blue exploration.

Often, the scenario above will give exploitation cases with a bit of exploration:

![alt tag](https://i.ibb.co/sPQfSDT/Screenshot-2021-10-24-at-01-09-33.png)

Occasionally, we get a full exploitation case:

![alt tag](https://i.ibb.co/8rKzMJw/Screenshot-2021-10-24-at-01-36-20.png)

Less often, a full exploration case:

![alt tag](https://i.ibb.co/Y8krSMM/Screenshot-2021-10-24-at-01-26-11.png)