🚗 Fuel-Optimizer — Route & Fuel Cost Planning API

🔎 Project Overview

Fuel-Optimizer is a Django-based web API that helps drivers plan long-distance trips across the USA by calculating:
	•	The optimal driving route between a start and finish location.
	•	Cost-efficient fuel stops along that route, based on fuel price data.
	•	Estimated total fuel cost for the journey, based on vehicle range/efficiency.

It also outputs a map showing the planned route with marked fuel stops, and provides a JSON summary with route, stops, distance, and cost.

✅ Key Features
	•	Route generation between two U.S. locations using a free routing service (e.g., OpenStreetMap / ORS / MapQuest).
	•	Fuel stop optimization — given a dataset of fuel prices, the system selects cheaper refueling points at optimal intervals.
	•	Cost estimation — using fixed vehicle assumptions (500 miles per tank, 10 miles per gallon), computes total fuel cost for the trip.
	•	Map generation — produces a visual map with the route and marked fuel stops.
	•	Simple API interface for easy integration or further front-end development.


🛠️ Getting Started — Setup & Run

Prerequisites
	•	Python 3.7+
	•	A valid routing service / API key if required (depending on the map/routing API used).

Installation Steps

# 1. Clone the repository
git clone https://github.com/sarajdhakal/fuel-optimizer.git
cd fuel-optimizer

# 2. (Optional but recommended) Create a virtual environment
python -m venv my_venv
source my_venv/bin/activate   # Windows: my_venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ensure the fuel price dataset is in place
#    (fuel-prices-for-be-assessment.csv already provided)

# 5. Run the Django server
python manage.py runserver

Example API Usage

Endpoint

POST /api/plan-route/

Request body (JSON):

{
  "start_location": "New York, NY, USA",
  "finish_location": "Los Angeles, CA, USA"
}

Example Response:

{
  "route_coordinates": [ /* list of lat/lng points */ ],
  "map_url": "URL-to-generated-map",
  "fuel_stops": [ /* list of recommended stops */ ],
  "total_cost": [/* generated */],
  "total_distance": [ /* 500.0 */ ]
}

🔧 Configuration & Data
	•	The repo includes a sample fuel price CSV dataset (fuel-prices-for-be-assessment.csv). You can replace or extend this with real or more comprehensive fuel price data.
	•	Vehicle parameters (range per tank, fuel efficiency) are currently fixed (500 miles per tank, 10 mpg). For real-world use, you may want to make these configurable.

📈 Future / Improvement Ideas
	•	Allow user-specified vehicle fuel efficiency and tank range.
	•	Accept more flexible inputs: waypoints, mid-trip breaks, alternate routes.
	•	Integrate real-time fuel price APIs instead of static dataset.
	•	Add error handling for cases when no fuel stops are available within a segment.
	•	Build a UI (frontend) to display