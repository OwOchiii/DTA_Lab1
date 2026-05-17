import numpy as np
import matplotlib.pyplot as plt

# ── Task 1: Create vector v with values 1 to 50 ──────────────────────────────
v = np.arange(1, 51)          # array([1, 2, 3, ..., 50])
print("Task 1 – Vector v (1 to 50):")
print(v)

# ── Task 2: Total value of all elements in v ─────────────────────────────────
total = v.sum()
print(f"\nTask 2 – Sum of all elements in v: {total}")

# ── Task 3: Elements greater than 10 and less than 40 ────────────────────────
filtered = v[(v > 10) & (v < 40)]
print("\nTask 3 – Elements where value > 10 and < 40:")
print(filtered)

# ── Task 4: New vector – each element is twice the value in v ─────────────────
v2 = v * 2
print("\nTask 4 – New vector (v × 2):")
print(v2)

# ── Task 5: Generate normal data (n=60, mean=0, sd=0.6) and scatterplot ──────
np.random.seed(42)
x = np.random.normal(loc=0, scale=0.6, size=60)
y = np.random.normal(loc=0, scale=0.6, size=60)

fig, ax = plt.subplots(figsize=(6, 5), facecolor='#EBEBEB')
ax.set_facecolor('#EBEBEB')

ax.scatter(x, y, color='black', s=20, zorder=3)

ax.set_title('Scatterplot of X and Y', fontsize=13, fontweight='normal')
ax.set_xlabel('x', fontstyle='italic')
ax.set_ylabel('y', fontstyle='italic', rotation=0, labelpad=10)
ax.grid(color='white', linewidth=0.8)
ax.tick_params(length=0)
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.savefig('scatterplot_xy.jpg', format='jpeg', dpi=150)
plt.show()
print("\nTask 5 – Scatterplot saved to scatterplot_xy.jpg")
print(f"  X (first 5): {x[:5].round(4)}")
print(f"  Y (first 5): {y[:5].round(4)}")