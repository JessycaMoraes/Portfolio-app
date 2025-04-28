css = """
.cards-hire-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 60px;
    margin-top: 25px;
    font-family: Roboto, sans-serif;
}
.card-hire {
    background-color: transparent;
    width: 220px;
    height: 300px;
    perspective: 1000px;
}
.inner-card-hire {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.6s;
    transform-style: preserve-3d;
}
.card-hire:hover .inner-card-hire {
    transform: rotateY(180deg);
}
.hire-front, .hire-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    font-family: Roboto, sans-serif;
}
.hire-front {
    background: linear-gradient(145deg, #d1d5db, #374151);
    color: white;
    transition: background 0.3s ease;
}
.card-hire:hover .hire-front {
    background: linear-gradient(145deg, #e5e7eb, #4b5563);
}
.hire-front img {
    width: 80px;
    height: 80px;
    margin-bottom: 15px;
}
.hire-front h3 {
    font-size: 16px;
    margin: 0;
    font-family: Roboto, sans-serif;
}
.hire-back {
    background: white;
    color: #333;
    transform: rotateY(180deg);
    font-size: 16px;
    padding: 20px;
    justify-content: center;
    font-family: Roboto, sans-serif;
}
"""

card_data = [
    {
        "img": "https://cdn-icons-png.flaticon.com/128/16990/16990376.png", 
        "title": "Data End-to-End", 
        "back": "I have hands-on experience across the full data lifecycle – from ingestion and transformation to analysis and dashboarding. This gives me flexibility to work as a Data Analyst, Analytics Engineer or Data Engineer."
    },

    {
        "img": "https://cdn-icons-png.flaticon.com/128/12663/12663338.png",
        "title": "Master Key Tools",
        "back": "I build scalable ETL pipelines using Python, SQL, and BigQuery and create effective visualizations with tools like Looker Studio. My solutions are production-ready and efficient."
    },

    {
        "img": "https://cdn-icons-png.flaticon.com/128/2172/2172891.png", 
        "title": "Bridge Data & ML", 
        "back": "I’ve collaborated directly with ML and product teams, preparing and adapting datasets for predictive modeling and ensuring alignment between business needs and data pipelines."
    },

    {
        "img": "https://cdn-icons-png.flaticon.com/128/16089/16089855.png", 
        "title": "Business-Driven", 
        "back": "I don't just build pipelines — I create impact. I’ve developed strategic KPIs and helped optimize processes in different areas through data insights."
    },

    {
        "img": "https://cdn-icons-png.flaticon.com/128/3050/3050525.png", 
        "title": "Translate Insights", 
        "back": "I have strong communication skills that help translate technical results into clear, actionable insights for stakeholders across the business."
    },

    {
        "img": "https://cdn-icons-png.flaticon.com/128/1674/1674958.png", 
        "title": "Global Collaboration", 
        "back": "I’ve worked closely with international teams (e.g., from the U.S.), successfully delivering results in distributed environments and building trust across time zones and cultures."
    }
]