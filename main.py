from cnes import download

def main():
    df = download("ST", "CE", 2021, 1)
    print(df.iloc[0,:])

main()