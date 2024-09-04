import pandas as pd

df = pd.read_csv('XGBOOSTCSV222.csv')
for i in range(0, len(df)):
    C = df.at[i, 'Status_C']
    CL = df.at[i, 'Status_CL']
    D = df.at[i, 'Status_D']
    if C > CL and C > D:
        if C >= 0.4:
            df.at[i, 'Status_C'] = min(0.99,df.at[i, 'Status_C']+0.2)
    if CL > C and CL > D:
        if CL >=0.4:
            df.at[i, 'Status_CL'] = min(0.99,df.at[i, 'Status_CL']+0.2)
    if D > CL and D > C:
        if D>=0.4:
            df.at[i, 'Status_D'] = min(0.99,df.at[i, 'Status_D']+0.2)

print(df.to_csv("submission_correctedXGBOOST.csv", index=False))
