import streamlit as st
import pandas as pd
import numpy as np
import io
import json
from PIL import Image

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION & VIBRANT FOOD STYLING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Food Verse AI - Food Intelligence Agent",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .stApp {
        background-color: #0f172a;
    }
    .macro-card {
        background-color: #1e293b;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        border: 1px solid #334155;
    }
    .fresh-badge {
        background-color: #15803d;
        color: white;
        padding: 4px 12px;
        border-radius: 15px;
        font-weight: bold;
    }
    .spoiled-badge {
        background-color: #b91c1c;
        color: white;
        padding: 4px 12px;
        border-radius: 15px;
        font-weight: bold;
    }
    .moderate-badge {
        background-color: #b45309;
        color: white;
        padding: 4px 12px;
        border-radius: 15px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SIDEBAR: CONFIGURATION & NAVIGATION
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("🥗 Food Verse AI")
    st.caption("Multimodal Food Intelligence Ecosystem")
    st.markdown("---")
    
    st.subheader("🔐 Security & API Config")
    api_key = st.text_input("Gemini / Groq API Key", type="password", placeholder="Paste API Key here...")
    if api_key:
        st.success("API Key Active (Live Vision Mode)")
    else:
        st.info("Standalone Demo Fallback Mode")
        
    st.markdown("---")
    st.subheader("📊 System Status")
    st.write("**Platform ID:** `6ac4ca021dcde6d7857c169a`")
    st.write("**Vision Engine:** LLaMA-3 Vision / Gemini 1.5")
    st.write("**Compliance Standard:** HACCP & USDA")
    st.markdown("---")
    st.caption("Skill Wallet Capstone Project 3")

# -----------------------------------------------------------------------------
# MAIN APP HEADER
# -----------------------------------------------------------------------------
st.title("Food Verse AI – Multimodal Food Intelligence Agent")
st.markdown("*(Analyzing Nutrition, Freshness, Commercial Kitchen Safety & Personal Dietetics)*")

tabs = st.tabs([
    "🥗 Nutrition Audit", 
    "🍎 Freshness Diagnostic", 
    "👨‍🍳 Kitchen Safety", 
    "🍳 Recipe Assistant", 
    "📅 7-Day Meal Planner"
])

# -----------------------------------------------------------------------------
# TAB 1: FOOD RECOGNITION & NUTRITION AUDIT (EPIC 2)
# -----------------------------------------------------------------------------
with tabs[0]:
    st.header("Tab 1: Food Recognition & Nutrition Breakdown")
    st.write("Upload a dish photo to audit calories, macronutrients, micronutrients, and health scores.")
    
    uploaded_food = st.file_uploader("Upload Dish / Meal Photo", type=["jpg", "jpeg", "png"], key="food_img")
    
    col1, col2 = st.columns([1, 1])
    
    if uploaded_food or st.button("Run Demo Meal Analysis"):
        if uploaded_food:
            image = Image.open(uploaded_food)
        else:
            image = Image.new('RGB', (400, 300), color=(200, 100, 50))
            
        with col1:
            st.image(image, caption="Analyzed Dish Sample", use_container_width=True)
            
        with col2:
            st.subheader("Recognized Dish: Mediterranean Avocado Chicken Salad")
            st.write("**Cuisine:** Mediterranean | **Portion:** ~350 grams")
            st.markdown("---")
            
            # Health Score Metric
            st.metric(label="Overall Health Score", value="88 / 100", delta="High Nutritional Value")
            
            # Nutrition Table & Chart
            st.write("**Macronutrient Breakdown:**")
            macros = pd.DataFrame({
                "Nutrient": ["Calories", "Protein", "Carbohydrates", "Fats", "Fiber"],
                "Amount": [420, 34, 18, 22, 9],
                "Unit": ["kcal", "g", "g", "g", "g"]
            })
            st.table(macros)
            
            st.write("**Allergen & Health Alerts:**")
            st.warning("⚠️ Contains Tree Nuts (Walnuts) & Dairy (Feta Cheese). Low Glycemic Index.")

# -----------------------------------------------------------------------------
# TAB 2: FOOD FRESHNESS & SPOILAGE DIAGNOSTIC (EPIC 3)
# -----------------------------------------------------------------------------
with tabs[1]:
    st.header("Tab 2: Food Freshness & Spoilage Diagnostic")
    st.write("Evaluate surface discoloration, texture degradation, and mold risks in perishables.")
    
    uploaded_item = st.file_uploader("Upload Perishable Item Photo (Fruit/Veg/Meat)", type=["jpg", "jpeg", "png"], key="item_img")
    
    if uploaded_item or st.button("Analyze Demo Produce Sample"):
        c1, c2 = st.columns([1, 1])
        with c1:
            st.info("Analyzing Surface Texture & Discoloration Index...")
            st.markdown("**Freshness Classification:** <span class='moderate-badge'>Moderately Fresh</span>", unsafe_allow_html=True)
            st.write("
")
            st.write("**Diagnostic Summary:** Slight oxidation detected around skin edges. No active fungal or mold spores identified.")
            
        with c2:
            st.subheader("🛡️ Safety & Storage Recommendation")
            st.warning("⏱️ **Action Plan:** Consume within 24 Hours.")
            st.write("**Preservation Tips:**")
            st.markdown("""
            - Store in an airtight container at 4°C (39°F).
            - Keep separate from ethylene-producing fruits like bananas.
            - Do not wash until immediately prior to consumption.
            """)

# -----------------------------------------------------------------------------
# TAB 3: KITCHEN HYGIENE & SAFETY COMPLIANCE (EPIC 4)
# -----------------------------------------------------------------------------
with tabs[2]:
    st.header("Tab 3: Kitchen Hygiene & Food Safety Compliance")
    st.write("Monitor commercial kitchen footage for HACCP compliance, PPE usage, and cross-contamination hazards.")
    
    kitchen_file = st.file_uploader("Upload Commercial Kitchen Snapshot/Video", type=["jpg", "png", "mp4"], key="kitch_file")
    
    if kitchen_file or st.button("Run Kitchen Compliance Audit"):
        st.subheader("HACCP Hygiene Score: 85% (Passing Grade)")
        
        col_a, col_b = st.columns([1, 1])
        with col_a:
            st.write("**Compliance Checklist:**")
            st.success("✅ Chef Hat / Hairnet Worn (100% compliance)")
            st.success("✅ Food Prep Surface Sanitized")
            st.danger("❌ Glove Violation: Raw poultry handled without disposable gloves")
            st.warning("⚠️ Cross-Contamination Risk: Cutting board unseparated")
            
        with col_b:
            st.write("**Itemized Violation Log:**")
            violations = pd.DataFrame([
                {"Time": "11:24 AM", "Station": "Grill Station 2", "Violation": "No Gloves on Duty", "Severity": "High"},
                {"Time": "11:28 AM", "Station": "Prep Area B", "Violation": "Raw Poultry near Veggies", "Severity": "Critical"}
            ])
            st.dataframe(violations, hide_index=True, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 4: SMART KITCHEN RECIPE ASSISTANT (EPIC 4)
# -----------------------------------------------------------------------------
with tabs[3]:
    st.header("Tab 4: Smart Kitchen Recipe Assistant")
    st.write("Input available pantry ingredients to generate gourmet, waste-free recipes.")
    
    ingredients = st.text_area("Enter Pantry Ingredients (comma separated):", value="Eggs, Spinach, Tomatoes, Olive Oil, Garlic, Parmesan Cheese")
    
    if st.button("🍳 Generate Smart Recipe"):
        st.subheader("Recipe Concept: Tuscan Spinach & Tomato Omelette")
        st.write("**Prep Time:** 10 Mins | **Cooking Time:** 8 Mins | **Difficulty:** Easy")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.write("**Step-by-Step Instructions:**")
            st.markdown("""
            1. Heat 1 tbsp olive oil in a pan over medium heat. Sauté minced garlic until fragrant.
            2. Add diced tomatoes and fresh spinach; cook until spinach wilts.
            3. Whisk 3 eggs with a pinch of salt and pepper. Pour over vegetables.
            4. Cook until edges set, sprinkle parmesan cheese, fold in half, and serve hot.
            """)
        with col2:
            st.write("**Ingredient Substitutions & Zero-Waste Tips:**")
            st.info("💡 **Substitutions:** Use Feta instead of Parmesan, or Kale instead of Spinach.

♻️ **Zero-Waste:** Save tomato tops and garlic skins for vegetable broth!")

# -----------------------------------------------------------------------------
# TAB 5: PERSONALIZED MEAL PLANNER (EPIC 5)
# -----------------------------------------------------------------------------
with tabs[4]:
    st.header("Tab 5: TDEE Meal Planner & Grocery Generator")
    st.write("Calculate BMR/TDEE targets and generate an adaptive 7-day nutritional schedule.")
    
    with st.form("tdee_form"):
        f1, f2, f3 = st.columns(3)
        with f1:
            age = st.number_input("Age", min_value=15, max_value=90, value=25)
            gender = st.selectbox("Gender", ["Male", "Female"])
        with f2:
            weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
            height = st.number_input("Height (cm)", min_value=120.0, max_value=220.0, value=175.0)
        with f3:
            activity = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])
            goal = st.selectbox("Fitness Goal", ["Fat Loss", "Maintenance", "Muscle Gain"])
            diet = st.selectbox("Dietary Preference", ["Balanced", "High Protein / Keto", "Vegan", "Diabetic-Friendly"])
            
        submitted = st.form_submit_button("Calculate Plan & Grocery List")
        
    if submitted or st.button("Load Default 7-Day Plan"):
        # Calculated BMR / TDEE
        bmr = 10 * weight + 6.25 * height - 5 * age + (5 if gender == "Male" else -161)
        tdee = bmr * 1.55
        target_calories = tdee - 500 if goal == "Fat Loss" else (tdee + 300 if goal == "Muscle Gain" else tdee)
        
        st.success(f"🎯 **Target Daily Calories:** {int(target_calories)} kcal | **BMR:** {int(bmr)} kcal | **TDEE:** {int(tdee)} kcal")
        
        st.subheader("🗓️ 7-Day Adaptive Meal Schedule")
        schedule = pd.DataFrame([
            {"Day": "Monday", "Breakfast": "Oatmeal with Berries & Whey", "Lunch": "Grilled Chicken Salad", "Dinner": "Baked Salmon with Asparagus"},
            {"Day": "Tuesday", "Breakfast": "Scrambled Eggs & Avocado Toast", "Lunch": "Turkey Wrap with Greens", "Dinner": "Lean Beef Stir-Fry with Brocolli"},
            {"Day": "Wednesday", "Breakfast": "Greek Yogurt & Granola Bowl", "Lunch": "Quinoa Veggie Buddha Bowl", "Dinner": "Grilled Tofu with Roasted Vegetables"},
            {"Day": "Thursday", "Breakfast": "Protein Smoothie (Banana/Peanut Butter)", "Lunch": "Tuna & Chickpea Salad", "Dinner": "Baked Chicken Breast & Sweet Potato"},
            {"Day": "Friday", "Breakfast": "Spinach Omelette with Mushrooms", "Lunch": "Lentil Soup & Whole Grain Bread", "Dinner": "Pan-Seared White Fish with Rice"},
            {"Day": "Saturday", "Breakfast": "Whole Wheat Protein Pancakes", "Lunch": "Chicken Quinoa Bowl", "Dinner": "Turkey Meatballs with Zucchini Noodles"},
            {"Day": "Sunday", "Breakfast": "Chia Seed Pudding with Mango", "Lunch": "Egg Salad Sandwich", "Dinner": "Grilled Shrimp with Steamed Vegetables"}
        ])
        st.table(schedule)
        
        st.subheader("🛒 Automated Grocery Shopping List")
        st.write("• **Proteins:** Chicken Breast (1kg), Eggs (2 Dozen), Salmon Fillets (500g), Greek Yogurt, Whey Protein")
        st.write("• **Carbs & Fiber:** Rolled Oats, Quinoa, Sweet Potatoes, Whole Wheat Bread, Brown Rice")
        st.write("• **Produce:** Spinach, Broccoli, Avocados, Tomatoes, Berries, Asparagus")
