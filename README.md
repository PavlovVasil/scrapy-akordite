# scrapy-akordite

The scraper uses pipelines in order to store the scraped data in to an SQLite DB.
The website being scraped is [this one](http://akordite.com/). There are roughly 1500 items that get scraped, each of them containing the chords for a popular pop song. The data then gets stored in Firebase, and would be used in a newly recreated version of the website later on, which would use React.js, Material UI, and service workers, in order to be a PWA and offer fully functional offline user experience.

## How to run the scraper
To restore the environment do the following:

1. [Download](https://www.anaconda.com/distribution/) and install Anaconda
2. Open Anaconda terminal (or Anaconda Powershell)
3. Navigate to the root project directory
4. Run ```conda env create -f environment.yml``` - this would restore the enviroment and dependencies
5. Run ```conda activate scrapyEnv``` in order to activate the environment
6. Run ```scrapy crawl akordite_crawler``` - this would actually run the crawler and generate an .csv file containing the data scraped from akordite.com

## How to debug the scraper if you are using VS Code
Use the provided launch.json debug configuration. 