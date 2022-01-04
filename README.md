# Ranker.com Scraper

Implementation based on [this repository](https://github.com/johnwmillr/trucks-and-beer).

## How to use this Scraper

 1. Find the appropriate class names to extract text from. Use your favorite browser's inspection tools.
 2. Specify .env file
    - store the class name from 1. in variable CLASS_IDENTIFIER e.g.
        
        ```python
        CLASS_IDENTIFIER=custom_class_example
        ```
    - store the target site in variable DEST e.g.
        
        ```python
        DEST=the-greatest-rappers-of-all-time
        ```
 3. Run `pip install -r requirements.txt`
 4. A file with the scraped data will be created in the same directory.

## Further Information

It can be defined how long the scraper waits for the website and how many times the scraper will
scroll down until the scrape is eventually finished. Both properties can be customized by defining each 
parameter respectively through the command line arguments `--sleep <time>` and `--scroll <scroll>`.
