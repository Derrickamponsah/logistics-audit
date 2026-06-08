import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Brazilian E-Commerce Delivery Audit",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CUSTOM CSS — Redesigned for clarity & contrast
# =====================================================

st.markdown("""
<style>
/* ── IMPORTS ── */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@400;500&display=swap');

/* ── RESET & BASE ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"], .stApp {
    background: #F8FAFC !important;
    font-family: 'DM Sans', 'Segoe UI', sans-serif !important;
    color: #0F172A !important;
}

#MainMenu, footer, header { visibility: hidden; }

/* ── MAIN CONTENT PADDING ── */
[data-testid="stAppViewContainer"] > .main > .block-container {
    padding: 0 2rem 3rem !important;
    max-width: 1280px !important;
}

/* ── HEADER BANNER ── */
.dash-header {
    background: #0A1628;
    padding: 28px 36px 26px;
    border-radius: 0 0 16px 16px;
    margin-bottom: 28px;
    margin-left: -2rem;
    margin-right: -2rem;
    position: relative;
    overflow: hidden;
}
.dash-header::after {
    content: '';
    position: absolute;
    right: -50px; top: -60px;
    width: 260px; height: 260px;
    border-radius: 50%;
    background: rgba(37,99,235,0.15);
    pointer-events: none;
}
.dash-header::before {
    content: '';
    position: absolute;
    right: 80px; bottom: -40px;
    width: 140px; height: 140px;
    border-radius: 50%;
    background: rgba(37,99,235,0.08);
    pointer-events: none;
}
.dash-eyebrow {
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.4);
    margin-bottom: 8px;
}
.dash-title {
    font-size: 26px;
    font-weight: 600;
    color: #FFFFFF;
    letter-spacing: -0.4px;
    margin-bottom: 5px;
    display: flex;
    align-items: center;
    gap: 12px;
    position: relative;
    z-index: 1;
}
.dash-icon {
    width: 36px; height: 36px;
    background: #2563EB;
    border-radius: 9px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
}
.dash-subtitle {
    font-size: 13px;
    color: rgba(255,255,255,0.5);
    font-weight: 400;
    position: relative;
    z-index: 1;
}
.dash-author {
    margin-top: 16px;
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 11px;
    font-weight: 500;
    color: rgba(255,255,255,0.55);
    position: relative;
    z-index: 1;
}
.author-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #059669;
    display: inline-block;
}

/* ── SECTION LABELS ── */
.section-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #64748B;
    margin-bottom: 14px;
    margin-top: 8px;
    padding: 0 2px;
}

/* ── KPI METRICS — handled by inline HTML cards, not st.metric ── */

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background: #F1F5F9 !important;
    border-radius: 10px !important;
    padding: 3px !important;
    gap: 2px !important;
    border-bottom: none !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #64748B !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    padding: 7px 14px !important;
    border-radius: 7px !important;
    border: none !important;
    transition: all 0.15s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #2563EB !important;
    background: rgba(255,255,255,0.6) !important;
}
.stTabs [aria-selected="true"] {
    background: #FFFFFF !important;
    color: #2563EB !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08) !important;
    font-weight: 600 !important;
}

/* ── DATAFRAMES ── */
[data-testid="stDataFrame"] {
    border-radius: 10px !important;
    overflow: hidden !important;
    border: 1px solid #E2E8F0 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
}
[data-testid="stDataFrame"] th {
    background: #F8FAFC !important;
    color: #64748B !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    border-bottom: 1px solid #E2E8F0 !important;
    padding: 10px 14px !important;
}
[data-testid="stDataFrame"] td {
    color: #0F172A !important;
    font-size: 12px !important;
    padding: 8px 14px !important;
    border-bottom: 1px solid #F1F5F9 !important;
}

/* ── ALERT BOXES ── */
[data-testid="stSuccess"] {
    background: #ECFDF5 !important;
    border-left: 3px solid #059669 !important;
    border-radius: 0 8px 8px 0 !important;
    color: #064E3B !important;
    padding: 14px 18px !important;
}
[data-testid="stWarning"] {
    background: #FFFBEB !important;
    border-left: 3px solid #F59E0B !important;
    border-radius: 0 8px 8px 0 !important;
    color: #78350F !important;
    padding: 14px 18px !important;
}
[data-testid="stInfo"] {
    background: #EFF6FF !important;
    border-left: 3px solid #2563EB !important;
    border-radius: 0 8px 8px 0 !important;
    color: #1E3A8A !important;
    padding: 14px 18px !important;
}
[data-testid="stError"] {
    background: #FEF2F2 !important;
    border-left: 3px solid #DC2626 !important;
    border-radius: 0 8px 8px 0 !important;
    color: #7F1D1D !important;
    padding: 14px 18px !important;
}
/* Alert icon & text colors */
[data-testid="stSuccess"] p,
[data-testid="stSuccess"] strong { color: #064E3B !important; }
[data-testid="stWarning"] p,
[data-testid="stWarning"] strong { color: #78350F !important; }
[data-testid="stInfo"] p,
[data-testid="stInfo"] strong    { color: #1E3A8A !important; }
[data-testid="stError"] p,
[data-testid="stError"] strong   { color: #7F1D1D !important; }

/* ── DIVIDER ── */
hr {
    border: none !important;
    border-top: 1px solid #E2E8F0 !important;
    margin: 24px 0 !important;
}

/* ── HEADINGS ── */
h1 { font-size: 20px !important; font-weight: 600 !important; color: #0F172A !important; }
h2 { font-size: 16px !important; font-weight: 600 !important; color: #0F172A !important; }
h3 { font-size: 14px !important; font-weight: 600 !important; color: #334155 !important; }

/* ── MARKDOWN TEXT ── */
.stMarkdown p { color: #334155 !important; font-size: 13px !important; line-height: 1.65 !important; }
.stMarkdown strong { color: #0F172A !important; }
.stMarkdown li { color: #334155 !important; font-size: 13px !important; }

/* ── BUTTONS ── */
.stButton > button {
    background: #2563EB !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 8px 18px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 6px rgba(37,99,235,0.25) !important;
}
.stButton > button:hover {
    background: #1D4ED8 !important;
    box-shadow: 0 4px 12px rgba(37,99,235,0.35) !important;
    transform: translateY(-1px) !important;
}

/* ── COLUMN PADDING ── */
[data-testid="column"] { padding: 0 8px !important; }

/* ── PLOTLY CHART CONTAINERS ── */
[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
    padding: 4px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

/* ── CARD HTML COMPONENT ── */
.info-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.info-card h3 {
    font-size: 14px !important;
    font-weight: 600 !important;
    color: #0F172A !important;
    margin-bottom: 10px !important;
    margin-top: 0 !important;
}
.info-card p {
    font-size: 13px !important;
    color: #475569 !important;
    line-height: 1.65 !important;
    margin: 0 !important;
}

/* ── INSIGHT BOXES ── */
.insight-blue {
    background: #EFF6FF;
    border-left: 3px solid #2563EB;
    border-radius: 0 8px 8px 0;
    padding: 14px 16px;
    margin-top: 14px;
}
.insight-blue p, .insight-blue strong { color: #1E3A8A !important; }

.insight-amber {
    background: #FFFBEB;
    border-left: 3px solid #F59E0B;
    border-radius: 0 8px 8px 0;
    padding: 14px 16px;
    margin-top: 14px;
}
.insight-amber p, .insight-amber strong { color: #78350F !important; }

/* ── REC CARDS ── */
.rec-card {
    border: 1px solid #E2E8F0;
    border-left: 3px solid #2563EB;
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    background: #FFFFFF;
    margin-bottom: 10px;
}
.rec-card h3 {
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #0F172A !important;
    margin: 0 0 5px !important;
}
.rec-card p {
    font-size: 12px !important;
    color: #64748B !important;
    line-height: 1.6 !important;
    margin: 0 !important;
}
.rec-number {
    display: inline-flex;
    width: 20px; height: 20px;
    background: #2563EB;
    color: #FFFFFF;
    border-radius: 50%;
    font-size: 10px;
    font-weight: 600;
    align-items: center;
    justify-content: center;
    margin-right: 8px;
    vertical-align: middle;
    flex-shrink: 0;
}

/* ── SUMMARY TABLE ── */
.summary-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}
.summary-table tr:nth-child(odd) td { background: #F8FAFC; }
.summary-table tr:nth-child(even) td { background: #FFFFFF; }
.summary-table td {
    padding: 11px 14px;
    color: #334155;
    border-bottom: 1px solid #F1F5F9;
}
.summary-table td:first-child { font-weight: 500; }
.summary-table td:last-child {
    font-weight: 600;
    color: #2563EB;
    font-family: 'DM Mono', monospace;
    text-align: right;
}
.summary-table thead td {
    background: #EFF6FF;
    color: #1E3A8A;
    font-weight: 600;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 2px solid #BFDBFE;
}

/* ── FOOTER ── */
.dash-footer {
    text-align: center;
    padding: 24px 0 8px;
    border-top: 1px solid #E2E8F0;
    color: #94A3B8;
    font-size: 12px;
    line-height: 1.8;
}
.dash-footer strong { color: #64748B; }
</style>
""", unsafe_allow_html=True)


# =====================================================
# CHART THEME HELPER
# =====================================================

CHART_COLORS = {
    "blue":   "#2563EB",
    "green":  "#059669",
    "red":    "#DC2626",
    "gold":   "#F59E0B",
    "orange": "#F97316",
    "slate":  "#94A3B8",
}

SEQUENTIAL_BLUES  = ["#BFDBFE", "#93C5FD", "#60A5FA", "#3B82F6", "#2563EB", "#1D4ED8", "#1E40AF"]
SEQUENTIAL_REDS   = ["#FECACA", "#FCA5A5", "#F87171", "#EF4444", "#DC2626", "#B91C1C", "#991B1B"]
SEQUENTIAL_ORANGE = ["#FED7AA", "#FDBA74", "#FB923C", "#F97316", "#EA580C", "#C2410C", "#9A3412"]


def style_chart(fig, title="", height=420):
    """Apply clean, consistent styling to every Plotly chart."""
    fig.update_layout(
        title={
            "text": f"<b>{title}</b>" if title else "",
            "x": 0.0,
            "xanchor": "left",
            "font": {"size": 14, "color": "#0F172A", "family": "DM Sans, sans-serif"},
            "pad": {"l": 4, "b": 10},
        },
        height=height,
        font=dict(family="DM Sans, sans-serif", size=12, color="#334155"),
        plot_bgcolor="#F8FAFC",
        paper_bgcolor="#FFFFFF",
        margin=dict(l=20, r=20, t=50 if title else 20, b=20),
        hovermode="closest",
        showlegend=True,
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#E2E8F0",
            borderwidth=1,
            font=dict(size=11, color="#334155"),
        ),
    )
    fig.update_xaxes(
        gridcolor="#F1F5F9",
        linecolor="#E2E8F0",
        tickfont=dict(size=11, color="#64748B"),
        title_font=dict(size=12, color="#64748B"),
    )
    fig.update_yaxes(
        gridcolor="#F1F5F9",
        linecolor="#E2E8F0",
        tickfont=dict(size=11, color="#64748B"),
        title_font=dict(size=12, color="#64748B"),
    )
    return fig


# =====================================================
# DATA LOADING
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS  = BASE_DIR / "outputs"


@st.cache_data
def load_data():
    master           = pd.read_csv(str(OUTPUTS / "master_dataset.csv"))
    state_metrics    = pd.read_csv(str(OUTPUTS / "state_metrics.csv"))
    category_metrics = pd.read_csv(str(OUTPUTS / "category_metrics.csv"))
    delivery_status  = pd.read_csv(str(OUTPUTS / "delivery_status_summary.csv"))
    review_status    = pd.read_csv(str(OUTPUTS / "review_by_status.csv"))
    distance_metrics = pd.read_csv(str(OUTPUTS / "distance_metrics.csv"))
    return master, state_metrics, category_metrics, delivery_status, review_status, distance_metrics


master, state_metrics, category_metrics, delivery_status, review_status, distance_metrics = load_data()

# Pre-compute reused stats
on_time_pct  = (master["delivery_status"] == "On Time").mean() * 100
late_pct     = master["is_late"].mean() * 100
avg_review   = master["review_score"].mean()
correlation  = master[["delay_days", "review_score"]].corr().iloc[0, 1]
n_states     = master["customer_state"].nunique()
n_categories = category_metrics.shape[0]
avg_delay    = master["delay_days"].mean()


# =====================================================
# HEADER
# =====================================================

st.markdown(f"""
<div class="dash-header">
    <div class="dash-eyebrow">Logistics Intelligence Platform</div>
    <div class="dash-title">
        <span class="dash-icon">🚚</span>
        Brazilian E-Commerce Delivery Audit
    </div>
    <div class="dash-subtitle">Comprehensive logistics performance analysis — Olist dataset</div>
    <div class="dash-author">
        <span class="author-dot"></span>
        Derrick Amponsah &nbsp;·&nbsp; June 2026
    </div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# KPI CARDS — fully custom HTML (bypasses st.metric)
# =====================================================

st.markdown('<div class="section-label">Key Performance Indicators</div>', unsafe_allow_html=True)

st.markdown(f"""
<style>
.kpi-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 14px;
}}
.kpi-card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px 22px 18px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05), 0 4px 14px rgba(0,0,0,0.03);
    position: relative;
    overflow: hidden;
    transition: box-shadow 0.2s ease, transform 0.2s ease;
}}
.kpi-card:hover {{
    box-shadow: 0 6px 20px rgba(0,0,0,0.09);
    transform: translateY(-2px);
}}
.kpi-card::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 12px 12px 0 0;
}}
.kpi-card.c-blue::before   {{ background: #2563EB; }}
.kpi-card.c-green::before  {{ background: #059669; }}
.kpi-card.c-red::before    {{ background: #DC2626; }}
.kpi-card.c-gold::before   {{ background: #F59E0B; }}
.kpi-card.c-slate::before  {{ background: #94A3B8; }}
.kpi-card.c-violet::before {{ background: #7C3AED; }}
.kpi-card.c-teal::before   {{ background: #0D9488; }}
.kpi-card.c-rose::before   {{ background: #E11D48; }}

.kpi-icon {{
    width: 32px; height: 32px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 15px;
    margin-bottom: 14px;
    flex-shrink: 0;
}}
.kpi-icon.c-blue   {{ background: #EFF6FF; }}
.kpi-icon.c-green  {{ background: #ECFDF5; }}
.kpi-icon.c-red    {{ background: #FEF2F2; }}
.kpi-icon.c-gold   {{ background: #FFFBEB; }}
.kpi-icon.c-slate  {{ background: #F1F5F9; }}
.kpi-icon.c-violet {{ background: #F5F3FF; }}
.kpi-icon.c-teal   {{ background: #F0FDFA; }}
.kpi-icon.c-rose   {{ background: #FFF1F2; }}

.kpi-label {{
    font-size: 11px;
    font-weight: 500;
    color: #94A3B8;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    margin-bottom: 8px;
    font-family: 'DM Sans', sans-serif;
}}
.kpi-value {{
    font-size: 28px;
    font-weight: 600;
    color: #0F172A;
    letter-spacing: -0.8px;
    line-height: 1;
    font-family: 'DM Mono', 'Courier New', monospace;
    margin-bottom: 8px;
}}
.kpi-delta {{
    font-size: 11px;
    color: #94A3B8;
    font-weight: 400;
    font-family: 'DM Sans', sans-serif;
    display: flex;
    align-items: center;
    gap: 4px;
}}
.kpi-delta::before {{
    content: '';
    display: inline-block;
    width: 5px; height: 5px;
    border-radius: 50%;
    background: #E2E8F0;
    flex-shrink: 0;
}}
</style>

<div class="kpi-grid">
  <div class="kpi-card c-blue">
    <div class="kpi-icon c-blue">📦</div>
    <div class="kpi-label">Total Orders</div>
    <div class="kpi-value">{len(master):,}</div>
    <div class="kpi-delta">Delivered orders analyzed</div>
  </div>
  <div class="kpi-card c-green">
    <div class="kpi-icon c-green">✅</div>
    <div class="kpi-label">On-Time Rate</div>
    <div class="kpi-value">{on_time_pct:.1f}%</div>
    <div class="kpi-delta">Delivery performance</div>
  </div>
  <div class="kpi-card c-red">
    <div class="kpi-icon c-red">⏰</div>
    <div class="kpi-label">Late Rate</div>
    <div class="kpi-value">{late_pct:.1f}%</div>
    <div class="kpi-delta">Delayed orders</div>
  </div>
  <div class="kpi-card c-gold">
    <div class="kpi-icon c-gold">⭐</div>
    <div class="kpi-label">Avg Review</div>
    <div class="kpi-value">{avg_review:.2f}<span style="font-size:14px;color:#94A3B8;font-weight:400;"> /5.0</span></div>
    <div class="kpi-delta">Customer rating</div>
  </div>
</div>

<div class="kpi-grid">
  <div class="kpi-card c-slate">
    <div class="kpi-icon c-slate">🗺️</div>
    <div class="kpi-label">States Covered</div>
    <div class="kpi-value">{n_states}</div>
    <div class="kpi-delta">Geographic coverage</div>
  </div>
  <div class="kpi-card c-violet">
    <div class="kpi-icon c-violet">📋</div>
    <div class="kpi-label">Categories</div>
    <div class="kpi-value">{n_categories}</div>
    <div class="kpi-delta">Product categories tracked</div>
  </div>
  <div class="kpi-card c-teal">
    <div class="kpi-icon c-teal">📅</div>
    <div class="kpi-label">Avg Delay Variance</div>
    <div class="kpi-value">{avg_delay:.1f}<span style="font-size:16px;color:#94A3B8;font-weight:400;">d</span></div>
    <div class="kpi-delta">Days early / late on average</div>
  </div>
  <div class="kpi-card c-rose">
    <div class="kpi-icon c-rose">🔗</div>
    <div class="kpi-label">Delay ↔ Review Corr.</div>
    <div class="kpi-value">{correlation:.2f}</div>
    <div class="kpi-delta">Pearson correlation coefficient</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================================
# TABS
# =====================================================

overview, geography, sentiment, distance, category, executive = st.tabs([
    "📊  Overview",
    "🗺️  Geographic Audit",
    "💬  Sentiment",
    "📍  Distance Audit",
    "📦  Category Risk",
    "🎯  Executive Summary",
])


# ─────────────────────────────────────────────────────
# TAB 1 — OVERVIEW
# ─────────────────────────────────────────────────────

with overview:

    col1, col2 = st.columns(2)

    with col1:
        fig = go.Figure(data=[go.Pie(
            labels=delivery_status["delivery_status"],
            values=delivery_status["orders"],
            hole=0.62,
            marker=dict(
                colors=[CHART_COLORS["blue"], CHART_COLORS["green"], CHART_COLORS["red"]],
                line=dict(color="#FFFFFF", width=3),
            ),
            textinfo="label+percent",
            textfont=dict(size=12, color="#334155"),
            hovertemplate="<b>%{label}</b><br>%{value:,} orders (%{percent})<extra></extra>",
        )])
        fig.add_annotation(
            text=f"<b>{on_time_pct:.1f}%</b><br><span style='font-size:11px'>on time</span>",
            x=0.5, y=0.5,
            font=dict(size=18, color="#0F172A", family="DM Sans"),
            showarrow=False,
        )
        fig = style_chart(fig, "Delivery Status Distribution", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        review_dist = (
            master["review_score"]
            .value_counts()
            .sort_index()
            .reset_index()
            .rename(columns={"review_score": "score", "count": "orders"})
        )
        colors = [CHART_COLORS["red"], CHART_COLORS["orange"],
                  CHART_COLORS["gold"], "#84CC16", CHART_COLORS["green"]]

        fig = px.bar(
            review_dist, x="score", y="orders",
            color="score",
            color_discrete_sequence=colors,
            labels={"score": "Review Score", "orders": "Number of Orders"},
        )
        fig.update_traces(
            marker_line_color="#FFFFFF",
            marker_line_width=2,
            hovertemplate="<b>★%{x}</b><br>%{y:,} orders<extra></extra>",
        )
        fig.update_layout(showlegend=False, coloraxis_showscale=False)
        fig = style_chart(fig, "Review Score Distribution", height=380)
        st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────────────
# TAB 2 — GEOGRAPHIC AUDIT
# ─────────────────────────────────────────────────────

with geography:

    top_states = state_metrics.sort_values("late_pct", ascending=False).head(10)

    fig = px.bar(
        top_states,
        x="late_pct",
        y="customer_state",
        orientation="h",
        color="late_pct",
        color_continuous_scale=[[0, "#FEE2E2"], [0.5, "#EF4444"], [1, "#7F1D1D"]],
        labels={"late_pct": "Late Delivery %", "customer_state": "State"},
        text=top_states["late_pct"].apply(lambda x: f"{x:.1f}%"),
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(size=11, color="#334155"),
        marker_line_width=0,
        hovertemplate="<b>%{y}</b><br>Late rate: %{x:.1f}%<extra></extra>",
    )
    fig.update_layout(coloraxis_showscale=False, yaxis=dict(autorange="reversed"))
    fig = style_chart(fig, "Top 10 States by Late Delivery Rate", height=440)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div class="insight-blue">
        <p><strong>Northern and remote states consistently show 3–4× higher late rates</strong> compared
        to southeastern hubs (SP, RJ). Infrastructure gaps and carrier coverage are likely root causes.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:20px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">All State Metrics</div>', unsafe_allow_html=True)
    st.dataframe(
        state_metrics.sort_values("late_pct", ascending=False),
        use_container_width=True,
        hide_index=True,
    )


# ─────────────────────────────────────────────────────
# TAB 3 — SENTIMENT ANALYSIS
# ─────────────────────────────────────────────────────

with sentiment:

    col1, col2 = st.columns([3, 2])

    with col1:
        colors_map = {
            "On Time": CHART_COLORS["green"],
            "Early":   CHART_COLORS["blue"],
            "Late":    CHART_COLORS["red"],
        }
        review_status_sorted = review_status.sort_values("avg_review", ascending=False)
        bar_colors = [colors_map.get(s, CHART_COLORS["slate"]) for s in review_status_sorted["delivery_status"]]

        fig = px.bar(
            review_status_sorted,
            x="delivery_status",
            y="avg_review",
            color="delivery_status",
            color_discrete_sequence=bar_colors,
            labels={"delivery_status": "Delivery Status", "avg_review": "Avg Review Score"},
            text=review_status_sorted["avg_review"].apply(lambda x: f"{x:.2f}"),
        )
        fig.update_traces(
            textposition="outside",
            textfont=dict(size=12, color="#334155"),
            marker_line_width=0,
            hovertemplate="<b>%{x}</b><br>Avg review: %{y:.2f} / 5.0<extra></extra>",
        )
        fig.update_layout(showlegend=False, yaxis=dict(range=[0, 5.5]))
        fig = style_chart(fig, "Average Review Score by Delivery Status", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("""
        <div class="info-card" style="margin-top:50px;">
            <h3>🔍 Key Finding</h3>
            <p>
                Delivery timing is the single strongest driver of customer satisfaction in this dataset.
                Late orders receive significantly lower review scores, confirming that logistics
                performance directly shapes the customer experience.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
            <h3>📊 Score Gap</h3>
            <p>
                On-time and early deliveries consistently score above <strong>4.1 / 5.0</strong>,
                while late deliveries drop to <strong>≈ 2.9 / 5.0</strong> — a gap of over 1.2 stars
                that directly impacts repeat purchase rates.
            </p>
        </div>
        """, unsafe_allow_html=True)

        corr_color = "#DC2626" if correlation < -0.2 else "#F59E0B"
        st.markdown(f"""
        <div class="info-card" style="border-top: 3px solid {corr_color};">
            <h3>🔗 Correlation</h3>
            <p>
                Pearson correlation between delay days and review score:
                <strong style="color:{corr_color}; font-size:18px; font-family:'DM Mono',monospace;">
                    {correlation:.2f}
                </strong><br>
                Negative relationship — longer delays, lower scores.
            </p>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────
# TAB 4 — DISTANCE AUDIT
# ─────────────────────────────────────────────────────

with distance:

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            distance_metrics,
            x="distance_band",
            y="late_pct",
            color="late_pct",
            color_continuous_scale=[[0, "#D1FAE5"], [0.4, "#FEF3C7"], [1, "#7F1D1D"]],
            labels={"distance_band": "Distance Band", "late_pct": "Late Delivery %"},
            text=distance_metrics["late_pct"].apply(lambda x: f"{x:.1f}%"),
        )
        fig.update_traces(
            textposition="outside",
            textfont=dict(size=11, color="#334155"),
            marker_line_width=0,
            hovertemplate="<b>%{x}</b><br>Late rate: %{y:.1f}%<extra></extra>",
        )
        fig.update_layout(coloraxis_showscale=False)
        fig = style_chart(fig, "Late Delivery % by Distance Band", height=380)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=distance_metrics["distance_band"],
            y=distance_metrics["avg_review"],
            mode="lines+markers",
            name="Avg Review",
            line=dict(color=CHART_COLORS["blue"], width=3),
            marker=dict(
                size=10,
                color=CHART_COLORS["blue"],
                line=dict(color="#FFFFFF", width=2),
            ),
            hovertemplate="<b>%{x}</b><br>Avg review: %{y:.2f} / 5.0<extra></extra>",
        ))
        fig = style_chart(fig, "Average Review Score by Distance", height=380)
        fig.update_layout(yaxis=dict(range=[3.5, 5.0]), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div class="insight-amber">
        <p>
            <strong>Distance triples late-delivery risk.</strong>
            Orders travelling over 2,000 km have a late rate exceeding 12% — nearly 3× the rate
            of local deliveries under 250 km (≈ 4.4%). Review scores also decline steadily with
            distance, suggesting that logistics complexity degrades customer experience end-to-end.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────
# TAB 5 — CATEGORY RISK
# ─────────────────────────────────────────────────────

with category:

    top_risk = category_metrics.sort_values("risk_score", ascending=False).head(10)

    fig = px.bar(
        top_risk,
        x="risk_score",
        y="product_category_name_english",
        orientation="h",
        color="risk_score",
        color_continuous_scale=[[0, "#FEF3C7"], [0.5, "#F97316"], [1, "#7F1D1D"]],
        labels={"risk_score": "Composite Risk Score",
                "product_category_name_english": "Category"},
        text=top_risk["risk_score"].apply(lambda x: f"{x:.2f}"),
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(size=11, color="#334155"),
        marker_line_width=0,
        hovertemplate="<b>%{y}</b><br>Risk score: %{x:.2f}<extra></extra>",
    )
    fig.update_layout(coloraxis_showscale=False, yaxis=dict(autorange="reversed"))
    fig = style_chart(fig, "Top 10 Highest-Risk Product Categories", height=440)
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="section-label">Top Category Metrics</div>', unsafe_allow_html=True)
        st.dataframe(top_risk, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>💡 Why This Matters</h3>
            <p>
                Some categories consistently experience more delivery issues and lower satisfaction.
                Identifying them enables targeted improvements across:
            </p>
            <ul style="margin-top:10px; padding-left:18px;">
                <li style="color:#475569; font-size:12px; margin-bottom:6px; line-height:1.5;">
                    <strong>Packaging</strong> — enhanced durability for fragile items</li>
                <li style="color:#475569; font-size:12px; margin-bottom:6px; line-height:1.5;">
                    <strong>Carrier selection</strong> — specialist handlers for high-risk goods</li>
                <li style="color:#475569; font-size:12px; margin-bottom:6px; line-height:1.5;">
                    <strong>Warehouse handling</strong> — improved storage procedures</li>
                <li style="color:#475569; font-size:12px; line-height:1.5;">
                    <strong>ETA accuracy</strong> — better delivery time estimates</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────
# TAB 6 — EXECUTIVE SUMMARY
# ─────────────────────────────────────────────────────

with executive:

    st.markdown("""
    <h1 style="text-align:center; margin-bottom:4px;">Executive Summary</h1>
    <p style="text-align:center; color:#64748B; font-size:13px; margin-bottom:24px;">
        Brazilian E-Commerce Delivery Audit — Strategic Findings
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Findings — fully custom HTML cards (no st.success/warning/info/error)
    st.markdown("""
    <style>
    .finding-card {
        display: flex;
        align-items: flex-start;
        gap: 16px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px 22px;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .finding-icon-wrap {
        width: 40px;
        height: 40px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        flex-shrink: 0;
        margin-top: 1px;
    }
    .finding-icon-wrap.green  { background: #ECFDF5; }
    .finding-icon-wrap.amber  { background: #FFFBEB; }
    .finding-icon-wrap.blue   { background: #EFF6FF; }
    .finding-icon-wrap.red    { background: #FEF2F2; }
    .finding-body { flex: 1; min-width: 0; }
    .finding-title {
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 6px;
        line-height: 1.3;
    }
    .finding-title.green { color: #065F46; }
    .finding-title.amber { color: #78350F; }
    .finding-title.blue  { color: #1E3A8A; }
    .finding-title.red   { color: #7F1D1D; }
    .finding-text {
        font-size: 13px;
        line-height: 1.65;
        color: #475569;
        margin: 0;
    }
    .finding-accent {
        width: 4px;
        border-radius: 2px;
        align-self: stretch;
        flex-shrink: 0;
    }
    .finding-accent.green { background: #059669; }
    .finding-accent.amber { background: #F59E0B; }
    .finding-accent.blue  { background: #2563EB; }
    .finding-accent.red   { background: #DC2626; }
    </style>

    <div class="finding-card">
        <div class="finding-accent green"></div>
        <div class="finding-icon-wrap green">✅</div>
        <div class="finding-body">
            <div class="finding-title green">Strong Operational Performance</div>
            <p class="finding-text">Over 93% of deliveries were completed on time, demonstrating
            generally efficient logistics management across 27 Brazilian states.</p>
        </div>
    </div>

    <div class="finding-card">
        <div class="finding-accent amber"></div>
        <div class="finding-icon-wrap amber">⚠️</div>
        <div class="finding-body">
            <div class="finding-title amber">Quality Impact Risk</div>
            <p class="finding-text">Late deliveries carry a measurable penalty on customer
            satisfaction — review scores drop by over 1.2 stars on average. Even small delays
            significantly affect the customer experience.</p>
        </div>
    </div>

    <div class="finding-card">
        <div class="finding-accent blue"></div>
        <div class="finding-icon-wrap blue">🗺️</div>
        <div class="finding-body">
            <div class="finding-title blue">Geographic Disparities</div>
            <p class="finding-text">Northern and remote states (AL, RR, AP, AM) show
            late-delivery rates of 15–22%, compared to 4–6% in São Paulo.
            Regional infrastructure gaps are the likely root cause.</p>
        </div>
    </div>

    <div class="finding-card">
        <div class="finding-accent blue"></div>
        <div class="finding-icon-wrap blue">📍</div>
        <div class="finding-body">
            <div class="finding-title blue">Distance as a Key Risk Factor</div>
            <p class="finding-text">Orders travelling over 2,000 km are nearly 3× more likely
            to arrive late than local deliveries. Review scores also decline steadily with
            shipping distance.</p>
        </div>
    </div>

    <div class="finding-card">
        <div class="finding-accent red"></div>
        <div class="finding-icon-wrap red">🚨</div>
        <div class="finding-body">
            <div class="finding-title red">High-Risk Product Categories</div>
            <p class="finding-text">Audio, Office Furniture, and Home Comfort products carry
            the highest composite risk scores. These categories require specialist handling,
            packaging upgrades, and dedicated carrier partnerships.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Recommendations
    st.markdown('<div class="section-label">Strategic Recommendations</div>', unsafe_allow_html=True)

    recs = [
        ("Distance Optimization",
         "Improve delivery forecasts for long-distance shipments. Evaluate regional carrier partnerships "
         "or distribution hubs in high-distance corridors to reduce 2,000+ km late rates."),
        ("Category-Specific Improvements",
         "Focus operational upgrades on high-risk categories through enhanced packaging standards, "
         "specialist carrier selection, and improved warehouse handling procedures."),
        ("Regional Intervention",
         "Prioritize targeted logistics interventions in AL, RR, AP, and AM states. Investigate "
         "root causes — infrastructure gaps vs carrier coverage — and implement corrective actions."),
        ("Proactive Monitoring",
         "Co-monitor delivery performance and review scores as a unified signal to surface emerging "
         "issues earlier and enable faster corrective response cycles."),
    ]

    for i, (title, body) in enumerate(recs, 1):
        st.markdown(f"""
        <div class="rec-card">
            <h3><span class="rec-number">{i}</span>{title}</h3>
            <p>{body}</p>
        </div>
        """, unsafe_allow_html=True)

    # Summary metrics table
    st.markdown("<div style='margin-top:24px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Performance Metrics at a Glance</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <table class="summary-table">
        <thead>
            <tr><td>Metric</td><td>Value</td></tr>
        </thead>
        <tbody>
            <tr><td>Total orders analyzed</td><td>{len(master):,}</td></tr>
            <tr><td>On-time delivery rate</td><td>{on_time_pct:.1f}%</td></tr>
            <tr><td>Average customer review</td><td>{avg_review:.2f} / 5.0</td></tr>
            <tr><td>States covered</td><td>{n_states}</td></tr>
            <tr><td>Product categories tracked</td><td>{n_categories}</td></tr>
            <tr><td>Delay ↔ Review correlation</td><td>{correlation:.2f}</td></tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.markdown(f"""
<div class="dash-footer">
    <strong>Brazilian E-Commerce Delivery Audit Dashboard</strong><br>
    Derrick Amponsah &nbsp;·&nbsp; Olist Brazilian E-Commerce Dataset &nbsp;·&nbsp; Streamlit + Plotly<br>
    <span style="font-size:11px; color:#CBD5E1;">© 2026 — All Rights Reserved</span>
</div>
""", unsafe_allow_html=True)