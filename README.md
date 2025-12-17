# MAX_PROFIT_ALGORITHM
# 🚧 Build Mars Smart: Max Profit Planner

**Live Demo:** [Open the Streamlit App](https://maxprofitalgorithm-fseymxrmcr5pwyztfstnd8.streamlit.app/)  

**An interactive Streamlit app to calculate maximum earnings for building Theatres, Pubs, and Commercial Parks on Mars.**  

This project helps users determine the **optimal combination of properties** given a fixed construction time. It is designed with a **gold-on-black futuristic theme** and interactive UI elements.

---

## 🏗️ Features

- Calculates **maximum potential earnings** based on available time units.
- Suggests **all optimal building combinations** for the given time.
- Interactive **Streamlit interface** with custom CSS styling.
- Sidebar displays **property details and feedback panel**.
- Results shown in **gold cards and strategy boxes**.
- Easy to use for **portfolio or recruiter presentations**.

---

## 🏢 Property Details

| Property            | Time Cost (units) | Earnings (per unit) | Notes                |
|--------------------|-----------------|-------------------|--------------------|
| 🎭 Theatre          | 5               | $1500             | Covers 2x1 parcel   |
| 🍺 Pub             | 4               | $1000             | Covers 1x1 parcel   |
| 🏢 Commercial Park  | 10              | $2000             | Covers 3x1 parcel   |

> Only one building can be developed at a time.

---

## 🚀 How the App Works

1. User enters **total available construction time (n units)**.
2. App computes **all possible combinations** of Theatres, Pubs, and Commercial Parks that fit within the time.
3. Each combination is evaluated for **profit** based on operational time and earnings per unit.
4. Displays:
   - **Maximum earnings** in a gold card.
   - **All optimal strategies** in separate strategy boxes.
5. Users can submit **feedback** through the sidebar panel.

---

## 💻 Technology Stack

- Python 3.x  
- Streamlit for interactive web interface  
- HTML & CSS for custom styling  

---

## 🖼️ UI Layout

- **Header:** Main title and subtitle with gold-on-black futuristic styling.  
- **Instruction Box:** Step-by-step guide for first-time users.  
- **Input Section:** Enter total available time units.  
- **Action Button:** Generates optimal strategies.  
- **Result Cards:**
  - **Gold Card:** Displays maximum potential earnings.
  - **Strategy Boxes:** Shows number of Theatres, Pubs, and Commercial Parks for each optimal combination.
- **Sidebar:**  
  - Property details (time cost, earnings)  
  - Feedback panel for suggestions  

> Fully styled with custom CSS to match the gold-on-black theme.

---

## 🧪 Example Usage

1. Run the app:

```bash
streamlit run max_profit_builder_app.py

2. Enter total construction time, e.g., 7 units.

3. Click ✨ Generate Optimal Strategies.

## Feedback Section

Users can submit suggestions in the sidebar text area.

Clicking Submit Feedback shows a confirmation message.

## Benefits

Demonstrates algorithmic optimization and problem-solving skills.

Interactive and visually appealing UI/UX with Streamlit and CSS.

Perfect for showcasing in portfolio or recruiter interviews.
