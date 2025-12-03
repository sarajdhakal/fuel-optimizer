# 🚗 Fuel-Optimizer — Route & Fuel Cost Planning API

Fuel-Optimizer is a Django-based API that helps users plan long-distance trips across the USA by computing the optimal driving route, selecting cost-efficient fuel stops, and estimating total fuel expense based on vehicle fuel efficiency and range.  
The system also generates an interactive map showing the full route and the recommended fuel stops.

---

## ⭐ Key Features

- **Optimal Route Generation** using a free routing API (OpenStreetMap/ORS/MapQuest).
- **Fuel Stop Optimization** based on fuel prices from a provided dataset.
- **Total Fuel Cost Estimation** using:
  - Vehicle Range: **500 miles per tank**
  - Fuel Efficiency: **10 miles per gallon**
- **Interactive Map Output** showing the route and fuel stops.
- **Simple JSON API** for easy integration into other apps.

---

---

## 🚀 Getting Started

### **Prerequisites**
- Python 3.7+
- Internet connection for routing API
- Fuel dataset (included in repo)

### **Installation**

```bash
# Clone the repository
git clone https://github.com/sarajdhakal/fuel-optimizer.git
cd fuel-optimizer

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver


### ***🔥 API Usage *** 
Endpoint

POST /api/plan-route/

Request Body
{
    "start_location": "New York, NY, USA",
    "finish_location": "Los Angeles, CA, USA"
}

Sample Response
{
    "start_location": "New York, NY, USA",
    "finish_location": "Los Angeles, CA, USA"
    "start_lon": "....",
    'start_lan": "...",
    "end_lon": "...",
    "end_lat:"..."
    "map_url": "URL-to-generated-map",
    "fuel_stops": ["Recommended fuel stop locations"],
    "total_cost": 123.45,
    "total_distance": 500.0
}
```

# 🛢️ Fuel Price Dataset

The project includes a CSV file containing fuel prices across multiple U.S. locations.
You may replace or extend the dataset as needed.
Location-based fuel stop selection is done using this file.

# 🧩 How It Works

User Input: Start and end locations.

Route Calculation: Using a free routing API.

Segment Splitting: Route divided into 500-mile segments (vehicle range).

Fuel Stop Selection: Cheapest fuel stop chosen per segment.

Cost Calculation: Based on fuel efficiency and selected stops.

Output: Map + JSON response with full summary.

# 📈 Future Enhancements

User-provided vehicle range & fuel efficiency

Integration with real-time fuel price APIs

Better route map UI

Error handling for extreme cases

Multi-route & waypoint support
