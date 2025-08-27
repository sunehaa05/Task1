import requests
import matplotlib.pyplot as plt
import seaborn as sns

# -------- Global Summary --------
url = "https://disease.sh/v3/covid-19/all"
response = requests.get(url)
data = response.json()

labels = ["Cases", "Deaths", "Recovered"]
values = [data["cases"], data["deaths"], data["recovered"]]

plt.figure(figsize=(6,4))
sns.barplot(x=labels, y=values, palette="mako")
plt.title("Global COVID-19 Summary")
plt.ylabel("Number of People")
plt.show()
