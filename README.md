# Outfit Generator
A non-deterministic Baysian-based  MAB outfit generator for clothes.


## Install the requirements

```
virutalenv env -p python3.8
source env/bin/activate
pip install -r requirements.txt 
```

## Launch the service

```
export FLASK_APP=app
fask run
cd outfitgenerator
behave
```

## Example of scenario


```
Scenario: Users reward the "hipster" and "formal" outfits the most with 3 specific items prefered

 Given the outfit generator is live on the website
 When users reward the "hipster" outfit 3 times with top 60536077, trousers 60519768 and shoes 60478094
 And users reward the "formal" outfit 2 times with top 60476826, trousers 22531116 and shoes 60168873
 Then we generate a HTML scenario_formal_1 file with a new outfit
```

It generates a HTML with exploitation(red)/exploration(blue) colour code


### Common result: a hybrid exploration(products)/exploitation(outfit)


![alt tag](https://i.ibb.co/sPQfSDT/Screenshot-2021-10-24-at-01-09-33.png)

### Occasional result: a full exploitation for outfit and products

![alt tag](https://i.ibb.co/8rKzMJw/Screenshot-2021-10-24-at-01-36-20.png)

### Rare result: a full exploitation for both outfit and products

![alt tag](https://i.ibb.co/Y8krSMM/Screenshot-2021-10-24-at-01-26-11.png)