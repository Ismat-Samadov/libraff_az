# libraf_az Web Scraping Project


## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview

The `libraf_az` project is a web scraping tool developed using Scrapy, a Python web scraping framework. It is designed to extract book information from the website "libraff.az." The spider, named "main," scrapes book details such as book names and images and can handle pagination to scrape multiple pages of book listings.

## Project Structure

The project has the following structure:

```
libraf_az/
│   scrapy.cfg
│
└── libraf_az/
    │   __init__.py
    │   items.py
    │   middlewares.py
    │   pipelines.py
    │   settings.py
    │   spiders/
    │       main_spider.py
│
└── images/
│       # Directory where scraped book images are stored
│
└── README.md
```

- `libraf_az`: The main project directory.
- `scrapy.cfg`: Scrapy project configuration file.
- `libraf_az`: The Python package for the project.
- `spiders`: The directory containing Scrapy spider scripts.
- `images`: The directory where scraped book images are stored.
- `README.md`: This file providing project documentation.

## Prerequisites

Before using this web scraping tool, ensure that you have the following dependencies installed:

- Python 3.x
- Scrapy
- Other dependencies specified in the `requirements.txt` file

You can install Scrapy and other dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Getting Started

To start using this web scraping tool, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/libraf_az.git
cd libraf_az
```

2. Install the required dependencies as mentioned in the Prerequisites section.

3. Customize the spider settings in `libraf_az/settings.py` to match your web scraping requirements.

4. Run the spider using the following command:

```bash
scrapy crawl main
```

The spider will start scraping book data from the specified URL(s) and store the images in the `images` directory.

## Usage

The spider is named "main" and is set to scrape the "libraff.az" website for book information. It extracts book names and images. You can customize the spider to scrape additional information as needed.

## Customization

You can customize the spider's behavior by modifying the following:

- Adjusting the CSS selectors in the `main_spider.py` script to scrape different data elements.
- Configuring pagination handling for websites with multiple pages.
- Modifying the item pipeline to store data in a different format or location.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Please follow the project's coding standards and provide clear documentation for your contributions.

## License

---
---

Happy web scraping!
```
