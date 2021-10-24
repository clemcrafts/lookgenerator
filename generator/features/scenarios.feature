Feature: MAB outfit generator

  Scenario: Shoppers reward the cosy look the most with specific items dominance
     Given the outfit generator is live on the website
     When users buy the hipster outfit 250 times with top 60536077, trousers 60519768 and shoes 60478094
     And users buy the formal outfit 50 times with top 60476826, trousers 22531116 and shoes 60168873
     Then we generate a HTML scenario_formal_1 file with a new outfit
