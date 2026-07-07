from django.shortcuts import render

def experience(request):
    experiences = [
        {
            'company': 'Sequentum India Pvt Ltd',
            'position': 'Agent Development Intern',
            'duration': 'May 2025 = June 2025',
            'location': 'Gurugram, Haryana',
            'description': [
                "Designed and developed 3 automated data pipeline systems in Python, reducing manual data extraction effort and integrating outputs into cloud storage and downstream processing workflows.", "Built and deployed cloud-connected backend scripts interfacing with AWS S3 and Snowflake, enabling structured data ingestion and transformation for Myntra and SBD business units.", "Implemented data validation and quality assurance modules using SQL and SSMS, improving data reliability and accuracy for analytics consumers.", "Developed live monitoring dashboards in Sequentum to surface real-time system health and operational metrics for internal stakeholders."
            ],
            'tools': [
                'Python', 'SQL', 'AWS S3', 'AWS IAM'
            ],
            'technologies': [
                'AWS', 'Snowflake', 'SQL Server Management Studio'
            ],
        },
        {
            'company': 'Synchubb Innovations Pvt Ltd',
            'position': 'Frontend Intern',
            'duration': 'Sept 2024 - Feb 2025',
            'location': 'Vellore, TN',
            'description': [
                "Promoted to Frontend Team Lead within 3 months, owning end-to-end component architecture, UI/UX design, and cross-team delivery coordination for a production web application.", "Engineered performant UI components using React and React Hooks, implementing robust state management and error boundaries to reduce runtime failures.", "Collaborated with backend engineers to integrate and test REST APIs using Postman, ensuring reliable data flow between frontend and server layers.", "Contributed to a MERN stack codebase (MongoDB, Express.js, React, Node.js), maintaining code quality through Git-based version control and peer reviews."
            ],
            'tools': [
                'React', 'Node.js', 'Express.js', 'MongoDB', 'Git'
            ],
            'technologies': [
                'AWS', 'Postman', 'GitHub Desktop', 'Visual Studio Code'
            ],
        }
    ]
    return render(request, 'experience.html', {'experiences': experiences})
