import pandas as pd

def avg_count_birds(sdf):
    """
    Calculate mean number of birds per species present.

    Parameters
    ----------
    birds_df : DataFrame
        Table with species in rows and years in columns, values are counts

    Returns
    -------
    : DataFrame
        One row titled Mean for the result with column for each year
    """

    count_df = pd.DataFrame(index=['Mean'], columns=sdf.columns)
    
    for year in sdf.columns:

        birds_this_year = sdf[year]
        
        birds_count = birds_this_year.sum()

        #Each species present in that year should have more than zero individuals, using that we could number of species in a particular year
        species_this_year = (birds_this_year > 0).sum()
        
        # If no species present, mean counts per species should be zero
        if species_this_year == 0:
            count_df[year] = 0
        else:
            count_df[year] = birds_count/species_this_year
        
    return count_df
