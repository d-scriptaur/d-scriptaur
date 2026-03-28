import pandas as pd
import matplotlib.pyplot as plt

# --- 1. DATA SECTION ---
data = {
    'Problem Solving': [10, 20, 35, 50, 65], 
    'Python':          [5, 15, 25, 40],       
    'Linux':           [2, 10, 15],           
    'SQL':             [10, 10, 20, 35, 50],  
    'DBMS':            [5, 12, 12, 25]        
}

# --- 2. PROCESSING ---
# Get only the LATEST value for each skill
latest_status = {skill: values[-1] for skill, values in data.items()}
df_latest = pd.Series(latest_status)

# --- 3. PLOTTING (Bar Chart) ---
plt.style.use('dark_background')
plt.figure(figsize=(10, 6))

# Create the bars
colors = ['#58a6ff', '#3fb950', '#d29922', '#f85149', '#bc8cff'] # GitHub-style colors
bars = plt.bar(df_latest.index, df_latest.values, color=colors, alpha=0.8)

# Add the actual number on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, yval, 
             ha='center', va='bottom', fontweight='bold', color='white')

# Aesthetics
plt.title('HackerRank: Current Skill Levels', fontsize=16, fontweight='bold', color='#58a6ff')
plt.ylabel('Current Marks / Level', fontsize=12)
plt.ylim(0, max(df_latest.values) + 10) # Give some space at the top
plt.grid(axis='y', linestyle='--', alpha=0.2)

# Save for README
plt.tight_layout()
plt.savefig('progress_graph.png', dpi=300, transparent=True)
