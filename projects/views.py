from django.shortcuts import render

def projects(request):
    projects = [
        {
            'img': 'project_images/mitigrate.png',
            'title': 'Autonomous Threat Detection & Mitigation System',
            'description': [
                "Architected a multi-layer security framework combining Isolation Forests, Linear Regression, and Character-level LSTMs to detect injection and zero-day attacks from live HTTP traffic streams.", "Built an autonomous Reasoning Engine using LangChain to classify intent and fuse anomaly scores from multiple detectors via a weighted scoring formula and confidence-based gating policy.", "Achieved 98% volumetric accuracy, 95% isolation accuracy, and a median end-to-end automated response latency of 185 milliseconds in production-like conditions."
            ],
            'stacks': [
                'Python', 'PyTorch', 'LangChain', 'Scikit-learn', 'Pandas', 'NumPy', 'YAML'
            ],
            'github_link': 'https://github.com/Iaryanyadav/DETECT-AND-AUTONOMOUSLY-MITIGATE-INJECTION-AND-ZERO-DAY-ATTACKS',
        },
        {
            'img': 'project_images/face.png',
            'title': 'Face Recognition Access Control System',
            'description': [
                "Engineered a real-time video processing pipeline integrating FaceNet and MTCNN for face detection and feature embedding, achieving 98% recognition accuracy in real-world scenarios.", "Designed a secure access control backend to authenticate users against an embedded feature store from live high-resolution video streams with minimal latency.", "Led a team of 2 engineers through full software development lifecycle (SDLC): requirements, architecture, prototyping, testing, and long-term maintenance."
            ],
            'stacks': [
                'Python', 'TensorFlow', 'OpenCV', 'MTCNN', 'FaceNet', 'NumPy'
            ],
            'github_link': 'https://github.com/Iaryanyadav/FaceRecognitionSecuritySystem',
        },
        {
            'img': 'project_images/web.png',
            'title': 'Automated Web Scraping & NLP Classification System',
            'description': [
                "Developed scalable, modular scraping pipelines using Selenium and BeautifulSoup to automate content extraction across multiple digital platforms with structured output formatting.",
                "Built a text classification engine using Random Forest and TF-IDF vectorization to identify and categorize sponsored content and brand mentions with high precision.",
                "Integrated OCR capabilities via Tesseract and NLTK-powered NLP preprocessing to handle unstructured media data at scale."
            ],
            'stacks': [
                'Python', 'Selenium', 'BeautifulSoup', 'Scikit-learn', 'Tesseract OCR', 'NLTK', 'Pandas'
            ],
            'github_link': 'https://github.com/Iaryanyadav/Web_Scrapping_Automated_Sponsor_Model'
        },
    ]
    
    return render(request, 'projects.html', {'projects': projects})
