import numpy as np
import pandas as pd
import polars as pl
import time

# Generate random data
def generate_data(rows=100000):
    np.random.seed(42)
    data = {
        'A': np.random.rand(rows),
        'B': np.random.randint(0, 100, size=rows)
    }
    return data

# Process data using pandas
def process_with_pandas(data):
    df = pd.DataFrame(data)
    result = df.groupby('B').agg({'A': 'mean'})
    return result

# Process data using polars
def process_with_polars(data):
    df = pl.DataFrame(data)
    result = df.group_by('B').agg(pl.col('A').mean().alias('mean_A'))
    return result

if __name__ == "__main__":
    data = generate_data()
    
    start_time = time.time()
    pd_result = process_with_pandas(data)
    print(f"Pandas processing time: {time.time() - start_time:.2f} seconds")
    
    start_time = time.time()
    pl_result = process_with_polars(data)
    print(f"Polars processing time: {time.time() - start_time:.2f} seconds")
