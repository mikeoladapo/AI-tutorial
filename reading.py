import pandas as pd

df = pd.read_csv("riders.csv")
lagos_rider = df[df["city"]=="Lagos"]
earnings = df["daily_earnings_ngn"].mean()
active_riders = df[df["status"] == "active"]
print(lagos_rider)
#print(active_riders)
#print(earnings)

