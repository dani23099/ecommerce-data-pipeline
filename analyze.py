import pandas as pd

# 1. Load the dataset
print("Loading the e-commerce database...")
df = pd.read_csv("ecommerce_data.csv")

# 2. Calculate market medians to establish our baselines
median_price = df['current_price'].median()
median_reviews = df['review_count'].median()
rating = 4.0
median_price = df['current_price'].median()
median_reviews = df['review_count'].median()

# 3. Business Intelligence: The Risk and Investment Matrix

# Category A: Hidden Gems (High satisfaction, popular, affordable)
# Strategy: Increase marketing budget for these products to drive volume sales
hidden_gems = df[
    (df['customer_rating'] >= rating) &
    (df['review_count'] >= median_reviews) &
    (df['current_price'] <= median_price)
]

# Category B: High-Risk Inventory (Expensive, poor satisfaction)
# Strategy: Review product quality with suppliers or consider delisting
high_risk = df[
    (df['customer_rating'] < rating) &
    (df['current_price'] > median_price)
]

# 4. Display the Actionable Insights
print("\n" + "="*50)
print("📊 MARKET INTELLIGENCE REPORT")
print("="*50)

print(f"\n💎 HIDDEN GEMS (Strategy: Promote heavily):")
if not hidden_gems.empty:
    # Displaying the top 3 best-rated hidden gems
    top_gems = hidden_gems.sort_values(by='customer_rating', ascending=False)
    for index, row in top_gems.iterrows():
        print(
            f"- {row['product_name'][:40]}... | Price: ${row['current_price']} | Rating: ⭐ {row['customer_rating']} ({row['review_count']} reviews)")
else:
        print("- No hidden gems found with current criteria.")

print(f"\n⚠️ HIGH-RISK INVENTORY (Strategy: Quality review):")
if not high_risk.empty:
    # Displaying the top 3 most expensive high-risk items
    top_risk = high_risk.sort_values(by='current_price', ascending=False).head(3)
    for index, row in top_risk.iterrows():
        print(
             f"- {row['product_name'][:40]}... | Price: ${row['current_price']} | Rating: ⭐ {row['customer_rating']} ({row['review_count']} reviews)")
else:
        print("- No high-risk products found. Great inventory health!")

print("\n" + "=" * 50)