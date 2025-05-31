# Career Guidance Engine

This project is an AI-powered career guidance engine designed specifically for the Indian education system. It leverages machine learning and natural language processing (NLP) to provide personalized career recommendations based on user aptitude, aspirations, skills, and experience.

## Features

- **Aptitude Estimation**: Utilizes machine learning models to predict user strengths from test data or behavioral patterns.
- **Goal & Interest Extraction**: Analyzes user inputs (text/audio) to extract aspirations and align them with relevant career clusters.
- **Skill & Experience Mapping**: Represents user competencies in vector space and matches them with various career profiles.
- **Career Recommendation Engine**: Suggests optimal career paths aligned with Indian academic streams, competitive exams (e.g., UPSC, NEET, JEE, CA), and job market trends.
- **Skill Gap Analysis**: Identifies missing competencies and recommends learning pathways in accordance with the National Education Policy (NEP) and competitive exams.

## Project Structure

```
career-guidance-engine
├── src
│   ├── app.py
│   ├── models
│   │   ├── aptitude_model.py
│   │   ├── nlp_goal_extractor.py
│   │   ├── skill_embedding.py
│   │   ├── recommendation_engine.py
│   │   └── skill_gap_analyzer.py
│   ├── data
│   │   ├── indian_academic_streams.csv
│   │   ├── exams_list.csv
│   │   └── job_market_trends.csv
│   ├── utils
│   │   ├── preprocessing.py
│   │   └── helpers.py
│   ├── api
│   │   ├── routes.py
│   │   └── schemas.py
│   └── types
│       └── index.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd career-guidance-engine
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```
   python src/app.py
   ```
2. Access the API at `http://localhost:5000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.