# scrapy-akordite

Moving an old spider into a new repository and finishing it. I would improve it by enabling pipelines in order to store the scraped data in an SQLite DB. There are roughly 1500 items to be scraped, which contain chords for some popular pop songs. I might later turn the project into a mobile app using React Native.

## How to run the scraper
To restore the environment do the following:

1. [Download](https://www.anaconda.com/distribution/) and install Anaconda
2. Open Anaconda terminal (or Anaconda Powershell)
3. Navigate to the root project directory
4. Run ```conda env create -f environment.yml``` - this would restore the enviroment and dependencies
5. Run ```conda activate scrapyEnv``` in order to activate the environment
6. Run ```scrapy crawl akordite_crawler``` - this would actually run the crawler and generate an .csv file containing the data scraped from Alibaba, as shown in the tutorial

## How to debug the scraper if you are using VS Code
Use the provided launch.json debug configuration. 