import pandas as pd
import numpy as np
import analysis_functions as af

def test_count_birds_small_table():
    input_df = pd.read_csv('birds_sm.csv', index_col='Species')
    results_df = af.avg_count_birds(input_df)
    np.testing.assert_array_equal(results_df['2010'], 24.5)

def test_count_birds_simulated_data():
    input_df = pd.DataFrame([[1,2],[3,4]],
        index=['Sp1', 'Sp2'], columns=['2010', '2011'])
    results_df = af.avg_count_birds(input_df)
    np.testing.assert_array_equal(results_df, [[2, 3]])

def test_count_birds_zero_species():
    input_df = pd.DataFrame([[1,2,0],[3,4,0]],
        index=['Sp1', 'Sp2'], columns=['2010', '2011', '2012'])
    results_df = af.avg_count_birds(input_df)
    np.testing.assert_array_equal(results_df, [[2, 3, 0]])