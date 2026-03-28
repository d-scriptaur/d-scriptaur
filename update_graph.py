import pandas as pd
import matplotlib.pyplot as plt

# --- 1. DATA SECTION ---
# Each list index represents Day 1, Day 2, etc.
data = {
    'Problem Solving': [10, 20, 35, 50], 
    'Python':          [5, 15, 25],       # Shorter length
    'Linux':           [2, 10],           # Shorter length
    'SQL':             [10, 10, 20, 35],  
    'DBMS':            [5, 12, 12, 25]        
}

# --- 2. PROCESSING ---
# Handle unequal lengths and fill missing days with 0 for stacking
df = pd.DataFrame({k: pd.Series(v) for k, v in data.items()}).fillna(0)
df.index = [f"Day {i+1}" for i in range(len(df))]

# --- 3. PLOTTING (Stacked Bar) ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the stacked bars
df.plot(kind='bar', stacked=True, ax=ax, color=['#58a6ff', '#3fb950', '#d29922', '#f85149', '#bc8cff'])

# Aesthetics for GitHub README
plt.title('HackerRank: Daily Cumulative Progress', fontsize=16, fontweight='bold', color='#58a6ff')
plt.xlabel('Progress Timeline', fontsize=12)
plt.ylabel('Total Combined Marks', fontsize=12)
plt.xticks(rotation=0) # Keeps "Day 1", "Day 2" horizontal
plt.grid(axis='y', linestyle='--', alpha=0.2)

# Legend placement
plt.legend(title="Skills", loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# Save for README
plt.tight_layout()
plt.savefig('progress_graph.png', dpi=300, transparent=True)
