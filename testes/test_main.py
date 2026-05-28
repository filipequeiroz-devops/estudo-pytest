from app.main import main
import pandas as pd


def testa_se_e_um_dataframe():

    df = main()
    assert isinstance(df, pd.DataFrame)

def testa_se_tem_dados():

    df = main()
    assert not df.empty