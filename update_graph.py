import pandas as pd
import matplotlib.pyplot as plt

# --- 1. DATA SECTION (Update this part daily) ---
data = {
    'Problem Solving': [1,10,10,10], 
    'Python':          [5,10,10,10],
    'Linux Shell':     [1,2,1,2],
    'SQL':             [10,10,10,10],  
    'Databases':       [5,5,5,5]        
}

# --- 2. PROCESSING ---
# 1. Handle unequal lengths
df = pd.DataFrame({k: pd.Series(v) for k, v in data.items()}).fillna(0)

# 2. CUMULATIVE SUM: This turns daily marks into total marks
# Day 1: [1, 5, 1] -> Day 2: [11, 15, 3] etc.
df_cumulative = df.cumsum()

# 3. Add a Day column for the X-axis
df_cumulative['Day'] = range(1, len(df_cumulative) + 1)

# --- 3. PLOTTING ---
plt.style.use('dark_background')
plt.figure(figsize=(10, 6))

# Plot each skill as a line
for col in df_cumulative.columns:
    if col != 'Day':
        plt.plot(df_cumulative['Day'], df_cumulative[col], 
                 label=col, marker='o', linewidth=2.5, markersize=8)

# --- 4. AESTHETICS ---
plt.title('HackerRank: Cumulative Skill Growth', fontsize=16, fontweight='bold', color='#58a6ff')
plt.xlabel('Day Number', fontsize=12)
plt.ylabel('Total Accumulated Marks', fontsize=12)
plt.grid(axis='both', linestyle='--', alpha=0.2)

# Legend placement
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# Save for README
plt.tight_layout()
plt.savefig('progress_graph.png', dpi=300, transparent=True)
