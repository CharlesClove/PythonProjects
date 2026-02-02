import pandas as pd
def pandas_function_to_prase_logs():
    df = pd.read_csv("sample-log.log",
                     sep=" ",
                     usecols=[0, 1, 2],
                     names=["DATE", "HOUR", "MSG", "info", "info2"],
                     engine="python")
    errors = df[df['MSG'] == "ERROR"]
    print(errors)
    print(f"TOTAL ERRORS: {len(errors)}")