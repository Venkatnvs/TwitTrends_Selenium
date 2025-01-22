# TwitTrends 🐦  
A web application to fetch and display real-time X (formerly twitter) trending topics with user authentication. Built using Flask for the backend and Tailwind CSS for a sleek, modern UI.

---
## Demo Video 🎥
[![Watch the video](https://img.youtube.com/vi/onTlC39ON0k/0.jpg)](https://www.youtube.com/watch?v=onTlC39ON0k)

---

## Features 🚀  
- User authentication with Twitter username and password.  
- Fetch and display the top 5 trending topics on X.  
- Dynamic UI with a responsive design using Tailwind CSS.  
- Real-time IP address display for query tracking.  

---

## Tech Stack 💻  
- **Frontend**: HTML, Tailwind CSS, JavaScript (ES6)  
- **Backend**: Flask, Python, Selenium  

---

## Installation 🔧  

### Prerequisites  
- Python 3.8+ 

### Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Venkatnvs/TwitTrends_Selenium.git
   cd TwitTrends_Selenium
   ```
2. Run the Server:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000`.

---

## API Workflow 🌐  

1. **Frontend**:  
   - Accepts a Twitter username and password via a form.  
   - Sends this data as a POST request to the backend (`/run-script`).  
   - Displays the fetched trends dynamically in a styled format.  

2. **Backend**:  
   - Receives the user credentials and validates them.  
   - Fetches top 5 trending topics.  
   - Returns a JSON response containing trends, query datetime, and IP address.  

3. **Output**:  
   - Only displays non-null trends dynamically.  

---

## Example Response 📝  
```json
{
  "datetime": "2025-01-22 12:45:30",
  "trends": [
    "Trend 1",
    "Trend 2",
    "Trend 3",
    "Trend 4",
    "Trend 5"
  ],
  "ip_address": "192.168.1.1"
}
```

---

## How to Use 🖱️  

1. Enter your X username and password in the provided fields.  
2. Click the **Fetch Trends** button.  
3. Wait for the trends to load (loading animation displayed).  
4. View the trends along with the IP address and timestamp. 

---

## Contact 📧  
For any questions or feedback, reach out to:  
- **Email**: venkatnvs2005@gmail.com  
- **GitHub**: [Venkatnvs](https://github.com/Venkatnvs)  

