import pandas as pd
import matplotlib.pyplot as plt

# 1. Data with different lengths
# Day 1  Day 2  Day 3  Day 4  Day 5
data = {
    'Problem Solving': [10, 20, 30, 40, 50], # 5 entries
    'Python':          [5, 15, 25],           # 3 entries
    'Linux':           [2, 4],                 # 2 entries
    'SQL':             [10, 10, 20, 30],       # 4 entries
    'DBMS':            [5, 5, 5, 10, 15]       # 5 entries
}

# 2. Convert to Series first to handle unequal lengths
# This creates a DataFrame where missing values are 'NaN'
df = pd.DataFrame({k: pd.Series(v) for k, v in data.items()})

# 3. Add a 'Day' column based on the longest list
df['Day'] = range(1, len(df) + 1)

def plot_uneven_data(df):
    plt.figure(figsize=(10, 6))
    
    for col in df.columns:
        if col != 'Day':
            # .dropna() tells matplotlib to ignore the missing days for that specific line
            valid_data = df[col].dropna()
            days = df['Day'][:len(valid_data)]
            
            plt.plot(days, valid_data, label=col, marker='o', linewidth=2)

    plt.title('HackerRank Progress (Adaptive Lengths)', fontsize=14)
    plt.xlabel('Day Number')
    plt.ylabel('Marks')
    plt.xticks(df['Day'])
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig('graph.png', dpi=300)

plot_uneven_data(df)
