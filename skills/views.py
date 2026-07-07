from django.shortcuts import render

def skills_view(request):
    skills_list = [
        {
            'name': 'Languages',
            'skill': [
                'Python', 'Java', 'C++', 'SQL', 'R'
            ],
        },
        {
            'name': 'Software Development',
            'skill': [
                "REST API Design", "Object-Oriented Programming (OOP)", "System Design", "Agile/Scrum", "Version Control (Git)"
            ],
        },
        {
            'name': 'Frontend',
            'skill': [
                'JavaScript', 'React', 'React Hooks', 'Tailwind CSS', 'HTML', 'CSS'
            ],
        },
        {
            'name': 'Backend',
            'skill': [
                'Node.js', 'Express.js', 'PostgreSQL', 'Django'
            ],
        },
        {
            'name': 'Database',
            'skill': [
                'PostgreSQL', 'MySQL', 'MongoDB', 'SQLite'
            ],
        },
        {
            'name': 'Cloud & DevOps',
            'skill': [
                'AWS S3', 'AWS DynamoDB', 'AWS Glue', 'AWS Redshift', 'AWS IAM', 'Azure Databricks', 'Azure Data Lake Gen2', 'Azure Stream Analytics', 'Azure Event Hubs', 'Snowflake'
            ],
        },
        {
            'name': 'Machine Learning',
            'skill': [
                'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Scikit-learn', 'TensorFlow', 'Keras', 'PyTorch', 'PySpark', 'LangChain'
            ],
        }, 
        {
            'name': 'Data Engineering',
            'skill': [
                'Apache Spark', 'Apache Kafka', 'Apache Airflow', 'ETL Pipelines', 'Data Warehousing', 'Data Lakes', 'Tableau', 'Power BI'
            ],
        },
        {
            'name': 'Tools',
            'skill': [
                'Jupyter Notebook', 'Postman', 'IntelliJ IDEA', 'GitHub Desktop', 'Cursor AI'
            ],
        }
    ]
    return render(request, 'skill.html', {'skills_list': skills_list})
