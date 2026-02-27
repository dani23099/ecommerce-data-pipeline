import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading data for visualization...")
df = pd.read_csv("ecommerce_data.csv")

# 1. Set a professional corporate style for the chart
sns.set_theme(style="whitegrid")

# 2. Create the canvas (Width: 10, Height: 6)
plt.figure(figsize=(10, 6))

# 3. Build the Scatter Plot (Market Matrix)
# - x and y define the axes
# - size makes dots larger based on review_count
# - hue colors the dots by category
sns.scatterplot(
    data=df,
    x='current_price',
    y='customer_rating',
    size='review_count',
    sizes=(50, 500), # Minimum and maximum dot sizes
    hue='product_category',
    alpha=0.7 # Slight transparency to see overlapping products
)

# 4. Add professional titles and labels
plt.title("Market Intelligence: Price vs. Customer Satisfaction", fontsize=14, fontweight='bold')
plt.xlabel("Price ($)", fontsize=12)
plt.ylabel("Customer Rating (Stars)", fontsize=12)

# 5. Adjust the legend so it doesn't cover data points
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout() # Ensures everything fits perfectly inside the image

# 5. Adjust the legend so it looks professional and bold
leyenda = plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

for texto in leyenda.get_texts():
    if texto.get_text() in ['product_category', 'review_count']:
        texto.set_weight('bold')

        texto_limpio = texto.get_text().replace('_', ' ').title()
        texto.set_text(texto_limpio)

plt.tight_layout()

# 6. Save the chart as a high-resolution image
plt.savefig("market_matrix.png", dpi=300)
print("Success! The chart has been saved as 'market_matrix.png' in your folder.")