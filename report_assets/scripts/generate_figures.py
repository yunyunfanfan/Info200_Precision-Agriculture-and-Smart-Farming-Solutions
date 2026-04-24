from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch


ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = ROOT / "report_assets" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(FIG_DIR / name, dpi=220, bbox_inches="tight")
    plt.close(fig)


def add_box(ax, x, y, w, h, text, fc="#EAF4F4", ec="#264653", fontsize=10, text_color="black"):
    rect = Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, linewidth=1.8)
    ax.add_patch(rect)
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize, color=text_color)


def add_arrow(ax, start, end, color="#555555", text=None, text_pos=None, connectionstyle="arc3,rad=0.0"):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="->",
        mutation_scale=12,
        linewidth=1.5,
        color=color,
        connectionstyle=connectionstyle,
    )
    ax.add_patch(arrow)
    if text and text_pos:
        ax.text(text_pos[0], text_pos[1], text, fontsize=9, color=color, ha="center", va="center")


def draw_problem_chart():
    labels = [
        "Water waste",
        "Fertilizer overuse",
        "Slow decisions",
        "Low traceability",
        "High labor pressure",
    ]
    scores = [78, 72, 69, 63, 58]
    colors = ["#2A9D8F", "#E9C46A", "#F4A261", "#E76F51", "#577590"]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(labels, scores, color=colors, edgecolor="#1f1f1f", linewidth=0.8)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Estimated severity score / 100")
    ax.set_title("Figure 1. Major Weaknesses in the Current Farming Model")
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)

    for bar, score in zip(bars, scores):
        ax.text(bar.get_x() + bar.get_width() / 2, score + 2, str(score), ha="center", fontsize=10)

    fig.tight_layout()
    save(fig, "figure_1_problem_chart.png")


def draw_architecture():
    fig, ax = plt.subplots(figsize=(13, 6.4))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6)
    ax.axis("off")

    add_box(ax, 0.5, 3.8, 2.2, 1.1, "Field Sensors\nSoil moisture\nTemperature\npH", fc="#D8F3DC")
    add_box(ax, 0.5, 2.1, 2.2, 1.1, "Drone Imaging\nCrop health\nPest detection", fc="#D8F3DC")
    add_box(ax, 0.5, 0.4, 2.2, 1.1, "External Data\nWeather API\nMarket price feed", fc="#D8F3DC")

    add_box(ax, 3.4, 2.2, 2.4, 1.6, "IoT Gateway\nData validation\nEdge buffering", fc="#CDE7F0")
    add_box(ax, 6.6, 2.2, 2.7, 1.6, "Smart Farming Platform\nAnalytics engine\nDecision rules\nAlerts", fc="#FCECC9")
    add_box(ax, 10.1, 3.5, 2.4, 1.0, "Farmer App\nTasks & alerts", fc="#F1D5DA")
    add_box(ax, 10.1, 2.0, 2.4, 1.0, "Cooperative Dashboard\nYield, water, logistics", fc="#F1D5DA", fontsize=9)
    add_box(ax, 10.1, 0.5, 2.4, 1.0, "Manager Portal\nReports & planning", fc="#F1D5DA")

    add_arrow(ax, (2.7, 4.35), (3.4, 3.4))
    add_arrow(ax, (2.7, 2.65), (3.4, 2.95))
    add_arrow(ax, (2.7, 0.95), (3.4, 2.5))
    add_arrow(ax, (5.8, 3.0), (6.6, 3.0), text="clean data", text_pos=(6.2, 3.38))
    add_arrow(ax, (9.3, 3.3), (10.1, 4.0))
    add_arrow(ax, (9.3, 3.0), (10.1, 2.5))
    add_arrow(ax, (9.3, 2.7), (10.1, 1.0))

    ax.set_title("Figure 2. Proposed Smart Farming System Architecture", fontsize=14, pad=12)
    save(fig, "figure_2_architecture.png")


def draw_dfd():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis("off")

    add_box(ax, 0.5, 5.0, 2.3, 1.0, "Farmers", fc="#E8F1F2")
    add_box(ax, 0.5, 2.9, 2.3, 1.0, "Agronomists", fc="#E8F1F2")
    add_box(ax, 0.5, 0.8, 2.3, 1.0, "Logistics Providers", fc="#E8F1F2")

    add_box(ax, 3.5, 4.5, 3.0, 1.3, "1.0 Collect Farm Data", fc="#D9ED92")
    add_box(ax, 3.5, 2.5, 3.0, 1.3, "2.0 Analyse Conditions", fc="#D9ED92")
    add_box(ax, 3.5, 0.5, 3.0, 1.3, "3.0 Coordinate Operations", fc="#D9ED92")

    add_box(ax, 7.6, 4.7, 2.6, 1.0, "D1 Sensor Data Store", fc="#FFF3B0")
    add_box(ax, 7.6, 2.7, 2.6, 1.0, "D2 Farm Records", fc="#FFF3B0")
    add_box(ax, 7.6, 0.7, 2.6, 1.0, "D3 Logistics Schedule", fc="#FFF3B0")

    add_box(ax, 11.2, 2.25, 2.3, 1.8, "Decision Dashboard\nAlerts\nRecommendations\nReports", fc="#F7D6E0")

    add_arrow(ax, (2.8, 5.5), (3.5, 5.15), text="field inputs", text_pos=(3.15, 5.8))
    add_arrow(ax, (2.8, 3.4), (3.5, 3.15), text="expert advice", text_pos=(3.2, 3.75))
    add_arrow(ax, (2.8, 1.3), (3.5, 1.15), text="delivery status", text_pos=(3.25, 1.65))

    add_arrow(ax, (6.5, 5.15), (7.6, 5.2))
    add_arrow(ax, (6.5, 3.15), (7.6, 3.2))
    add_arrow(ax, (6.5, 1.15), (7.6, 1.2))

    add_arrow(ax, (10.2, 5.2), (6.5, 3.8), color="#6C757D", connectionstyle="arc3,rad=0.0")
    add_arrow(ax, (10.2, 3.2), (6.5, 3.8), color="#6C757D", connectionstyle="arc3,rad=0.0")
    add_arrow(ax, (10.2, 1.2), (6.5, 1.8), color="#6C757D", connectionstyle="arc3,rad=0.0")

    add_arrow(ax, (6.5, 3.15), (11.2, 3.15), text="insights", text_pos=(8.9, 3.48))
    add_arrow(ax, (11.2, 3.95), (2.8, 5.55), color="#BC4749", connectionstyle="arc3,rad=0.28")
    add_arrow(ax, (11.2, 3.15), (2.8, 3.4), color="#BC4749", connectionstyle="arc3,rad=0.12")
    add_arrow(ax, (11.2, 2.35), (2.8, 1.25), color="#BC4749", connectionstyle="arc3,rad=-0.22")

    ax.set_title("Figure 3. Level-1 Data Flow Diagram for the Proposed Information System", fontsize=14, pad=12)
    save(fig, "figure_3_dfd.png")


def draw_dashboard_mockup():
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    add_box(
        ax,
        0.2,
        6.2,
        11.4,
        0.6,
        "Unified Dashboard: Precision Agriculture Monitoring",
        fc="#264653",
        ec="#264653",
        fontsize=13,
        text_color="white",
    )

    add_box(ax, 0.4, 4.6, 2.5, 1.2, "KPI Card\nWater use: -18%\nYield forecast: +12%", fc="#E9F5DB")
    add_box(ax, 3.2, 4.6, 2.5, 1.2, "KPI Card\nSensor uptime: 96%\nRisk alerts: 4", fc="#E9F5DB")
    add_box(ax, 6.0, 4.6, 2.5, 1.2, "KPI Card\nFertilizer saving: 14%\nOn-time delivery: 91%", fc="#E9F5DB")
    add_box(ax, 8.8, 4.6, 2.5, 1.2, "Action Panel\nIrrigate field B\nInspect pest risk", fc="#FAEDCD")

    add_box(ax, 0.4, 2.2, 5.2, 1.8, "Field Map Panel\nZones by soil moisture and crop stress", fc="#DDEAF6")
    add_box(ax, 6.0, 2.2, 5.3, 1.8, "Trend Panel\n7-day weather, water use, NDVI trend", fc="#DDEAF6")

    add_box(ax, 0.4, 0.4, 3.3, 1.3, "Alert Feed\nLow moisture\nDisease anomaly\nTruck delay", fc="#F8D7DA")
    add_box(ax, 4.0, 0.4, 3.3, 1.3, "Task Queue\nAssign technician\nSchedule fertilizer run", fc="#FFF3BF")
    add_box(ax, 7.6, 0.4, 3.7, 1.3, "Quick Links\nWeather API\nSensor logs\nMarket prices", fc="#D8F3DC")

    ax.set_title("Figure 4. Dashboard Wireframe for Farmers and Cooperative Managers", fontsize=14, pad=10)
    save(fig, "figure_4_dashboard.png")


def draw_gantt():
    phases = [
        ("Requirements study", 1, 2, "#8ECAE6"),
        ("Interviews and survey", 2, 3, "#219EBC"),
        ("System analysis", 4, 2, "#90BE6D"),
        ("Prototype and DFD design", 5, 2, "#F9C74F"),
        ("Evaluation and ethics review", 6, 2, "#F9844A"),
        ("Report writing", 7, 2, "#F94144"),
    ]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    y_positions = list(range(len(phases)))

    for y, (label, start, duration, color) in enumerate(phases):
        ax.barh(y, duration, left=start, height=0.55, color=color, edgecolor="#333333")
        ax.text(start + duration / 2, y, label, ha="center", va="center", fontsize=9, color="#1f1f1f")

    ax.set_yticks(y_positions)
    ax.set_yticklabels([f"Task {i + 1}" for i in y_positions])
    ax.set_xticks(range(1, 10))
    ax.set_xlabel("Project Week")
    ax.set_title("Figure 5. Suggested Project Timescale for the Team Assignment")
    ax.grid(axis="x", linestyle="--", alpha=0.35)
    ax.invert_yaxis()
    fig.tight_layout()
    save(fig, "figure_5_gantt.png")


if __name__ == "__main__":
    draw_problem_chart()
    draw_architecture()
    draw_dfd()
    draw_dashboard_mockup()
    draw_gantt()
    print(f"Generated figures in: {FIG_DIR}")
