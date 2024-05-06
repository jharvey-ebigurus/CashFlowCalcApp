import pandas as pd
import numpy as np

def getFixedCashFlowPV(num_years, pmt_freq, pmt_amt, int_rate):
    num_periods = num_years * pmt_freq
    disc_rate = int_rate / pmt_freq
    df = pd.DataFrame({
        'CurrentPeriod': np.arange(1, num_periods + 1),
        'Payment': [pmt_amt] * num_periods,
        'DiscFact': 1 / (1 + disc_rate) ** np.arange(1, num_periods + 1),
        'PmtPV': (pmt_amt * (1 / (1 + disc_rate) ** np.arange(1, num_periods + 1)))
    })
    return df
