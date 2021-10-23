# cardano-blockfrost-api

## Introduction

    Blockfrost (https://blockfrost.io/) provides an API to access data stored on the Cardano blockchain. 
    Python is used to communicate, extract, manipulate, and store data fetched from the API. Our stored data 
    is illustrated via webpage. Technologies used to output the webpage include: Django Web Framework, Django 
    REST Framework, HTML, CSS, Javascript (CanvasJS for charting). Here is a link to my Github repository: 
    https://github.com/psilosanctum/cardano-blockfrost-api. The repository will be updated at the end of each 
    Cardano epoch (i.e. 5 days) to account for staking rewards distributions.

## Illustrations - Background Information

    **Figure 1 - Gross Income vs. Staking Rewards**
    
    $ADA token holders can contribute to network security and operations on the Cardano blockchain by holding 
    their funds in a crypto wallet and delegating to a stake pool. Token holders are rewarded for their services 
    (in $ADA) every 5 days (i.e. one epoch) via staking rewards. Consequently, gross income is recognized upon 
    distribution of rewards at the end of each epoch. Since rewards are distributed in $ADA, token holders must 
    convert their rewards to USD by multiplying rewards (in $ADA) and the market price at distribution. The 
    converted amount is recognized as gross income and represents the cost basis of tokens.

    Rewards tracking is tedious, especially if investors hold $ADA in multiple crypto wallets. Our project uses 
    the Cardano API and Python to extract the history of rewards among multiple wallets, combine wallet data to 
    sum rewards by epoch, convert epoch rewards to USD, and store the manipulated data in a separate file. The 
    effect is an automated rewards tracking process with formatted data that serves as inputs to our graphic 
    illustrations. Additionally, our manipulated data is stored effectively to facilitate tax compliance.
    
![Gross Income](https://github.com/psilosanctum/cardano-blockfrost-api/blob/main/graph_screenshots/gross_income_vs_staking.png)

    **Figure 2 & 3 - Transactions**

    Transaction data provides key insights on the growth of the Cardano network over time and the blockchain's 
    tokenomics. Our graphics illustrate stability in fees as transaction volume increases significantly. 
    Despite the increase in network activity, the cost to transact (i.e. the cost to do business) on Cardano's
    blockchain remains relatively predictable. Ethereum cannot claim similar transaction fee stability; 
    therefore, Cardano's network currently offers both superior tokenomics and technology.

![Fees vs. Transactions](https://github.com/psilosanctum/cardano-blockfrost-api/blob/main/graph_screenshots/fees_vs_transactions.png)

![Average Cost](https://github.com/psilosanctum/cardano-blockfrost-api/blob/main/graph_screenshots/avg_cost.png)
