import pandas as pd
import matplotlib.pyplot as plt

# Load files
students = pd.read_csv("data.csv")
answer_key = pd.read_csv("answer_key.csv")

correct_answers = answer_key.iloc[0]

results = []

for index, row in students.iterrows():

    correct = 0
    total = 5

    for q in range(1, 6):

        if row[f"Q{q}"] == correct_answers[f"Q{q}"]:
            correct += 1

    incorrect = total - correct
    percentage = (correct / total) * 100

    results.append({
        "Name": row["Name"],
        "Correct": correct,
        "Incorrect": incorrect,
        "Percentage": percentage
    })

# Result DataFrame
result_df = pd.DataFrame(results)

print("\n========== QUIZ ANALYTICS ==========\n")
print(result_df)

# =========================
# BAR CHART
# =========================

plt.figure(figsize=(8, 5))

plt.bar(result_df["Name"], result_df["Percentage"], color="skyblue")

plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Percentage")

plt.savefig("bar_chart.png")
plt.close()

# =========================
# PIE CHART
# =========================

total_correct = result_df["Correct"].sum()
total_incorrect = result_df["Incorrect"].sum()

plt.figure(figsize=(6, 6))

plt.pie(
    [total_correct, total_incorrect],
    labels=["Correct", "Incorrect"],
    autopct="%1.1f%%",
    colors=["green", "red"]
)

plt.title("Overall Quiz Analysis")

plt.savefig("pie_chart.png")
plt.close()

print("\nGraphs generated successfully!")
