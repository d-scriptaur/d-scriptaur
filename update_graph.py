import pandas as pd
import matplotlib.pyplot as plt

# --- 1. DATA SECTION (Update this part daily) ---
data = {
    'Problem Solving': [1,10,10], 
    'Python':          [5,10,10],
    'Linux Shell':     [1,2,1],
    'SQL':             [10,10,10],  
    'Databases':       [5,5,5]        
}

# --- 2. PROCESSING ---
# Handle unequal lengths by converting to Series
df = pd.DataFrame({k: pd.Series(v) for k, v in data.items()})
df['Day'] = range(1, len(df) + 1)

# --- 3. PLOTTING ---
plt.style.use('dark_background') # Looks "authentic" on GitHub's dark mode
plt.figure(figsize=(10, 5))

for col in df.columns:
    if col != 'Day':
        valid_series = df[col].dropna()
        days = df['Day'][:len(valid_series)]
        plt.plot(days, valid_series, label=col, marker='o', linewidth=2.5, markersize=6)

# Aesthetics for GitHub
plt.title('HackerRank Progress Tracker', fontsize=16, fontweight='bold', color='#58a6ff')
plt.xlabel('Days of Practice', fontsize=12)
plt.ylabel('Score / Marks', fontsize=12)
plt.xticks(df['Day'])
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Move legend to the side
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# Save the file (Crucial for README)
plt.tight_layout()
plt.savefig('progress_graph.png', dpi=300, transparent=True)
