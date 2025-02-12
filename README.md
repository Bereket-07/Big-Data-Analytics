# 🗺️ Big Data Analysis using power BI

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Folder Organization](#folder-organization)
- [Setup](#setup)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Overview: Key Functionalities


## Project Overview
### Key Features:

- ### Data Extraction:

Large-scale e-commerce dataset (1M+ rows) from Kaggle/UCI ML Repository.

Web scraping using Telethon (to extract messages from Ethiopian Telegram channels related to e-commerce).

- ### Data Transformation:

Data cleaning (handling missing values, removing duplicates, formatting columns).

Sentiment analysis on Telegram messages.

- ### Data Storage:

PostgreSQL for structured data storage.

Designed a relational schema to link e-commerce and Telegram datasets.

- ### Data Visualization:

Power BI/Looker dashboards for business insights.

Analysis of sales trends, customer behavior, and social media sentiment impact on e-commerce.
# Tools & Libraries Used

1. **Programming Language**: [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=yellow)](https://www.python.org/)
2. **Logging**: [![Logger](https://img.shields.io/badge/Logging-4B8BBE?style=flat&logo=python&logoColor=yellow)](https://docs.python.org/3/howto/logging.html)
3. **Database**: [![Postgres](https://img.shields.io/badge/postgres-4479A1?style=flat&logo=poatgres&logoColor=white)](https://www.mysql.com/)
4. **Version Control**: [![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/)| [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/)
5. **Code Formatting & Linting**: [![Black](https://img.shields.io/badge/Black-000000?style=flat&logo=python&logoColor=white)](https://github.com/psf/black)
6. **Continuous Integration (CI)**: [![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=github-actions&logoColor=white)](https://github.com/features/actions)
7. **Environment Management**: [![Pip](https://img.shields.io/badge/Pip-005A8B?style=flat&logo=pypi&logoColor=white)](https://pip.pypa.io/en/stable/)
## Folder Organization

```

📁.github
│   └── 📁workflows
│        └── 📃unittests.yml
📁data
│   ├── raw_data
│   ├── cleaned_data
│   ├── db_schema.sql
📁src
│   ├── 📃extract.py  # Data extraction scripts
│   ├── 📃transform.py  # Data cleaning & sentiment analysis
│   ├── 📃load.py  # Database schema creation & data insertion
│   ├── 📃config.py  # API Keys & DB Configs
📁visualizations
│   ├── power_bi_dashboard.pbix
📁tests
│   ├── 📃test_etl.py
📜 .gitignore
📜 README.md
📜 requirements.txt

```

## License

This project is licensed under the MIT License

### Summary

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It is a simple and easy-to-understand license that places very few restrictions on reuse, making it a popular choice for open source projects.

By using this project, you agree to include the original copyright notice and permission notice in any copies or substantial portions of the software.
