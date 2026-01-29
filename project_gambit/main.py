import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("Hi, I am Gambit!")
st.markdown("Your smart personal finance assistant")

# Upload CSV
uploaded_file = st.file_uploader("Upload your bank statement CSV", type=["csv"])

if uploaded_file:

    # Read CSV
    df = pd.read_csv(uploaded_file)
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    # Categorize transactions based on Description
    def categorize(description):
        desc = description.lower()
        #specific keywords for categorization (changable)
        food = ["jollibee","mcdo","baga burger","chowking","mn","kfc","yumgyeopsal","starbucks",
                "groceries","pizza","chick-fil-a","restaurant","cafe","foodpanda","ubereats"]
        transpo = ["grab","angkas","fare","gas"]
        utilities = ["meralco","water","converge","phone","mortgage","credit"]
        shopping = ["shopee","lazada","amazon"]
        entertainment = ["netflix","spotify","hulu"]

        if any(word in desc for word in food):
            return "Food"
        elif any(word in desc for word in transpo):
            return "Transport"
        elif any(word in desc for word in utilities):
            return "Utilities"
        elif any(word in desc for word in shopping):
            return "Shopping"
        elif any(word in desc for word in entertainment):
            return "Entertainment"
        else:
            return "Other"

    # Convert Date and Month
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    df["Category"] = df["Description"].apply(categorize)

    # Search/filter
    search_term = st.text_input("Search Description (e.g., 'gas', 'netflix')")
    filtered_df = df[df["Description"].str.contains(search_term, case=False, na=False)] if search_term else df
    st.subheader("Raw Data")
    st.dataframe(filtered_df)

    # Monthly summary
    monthly_summary = df.groupby("Month")["Amount"].sum().reset_index()

    # Plotly Overview Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Monthly Breakdown", "Category Breakdown", "Predictions", "Insights"])

    with tab1:
        st.subheader("Monthly Spending Summary")
        fig_overview = px.line(monthly_summary, x='Month', y='Amount', markers=True, title="Monthly Spending Trend")
        fig_overview.update_traces(hovertemplate='Month: %{x}<br>Amount: ₱%{y:,.0f}')
        st.plotly_chart(fig_overview, use_container_width=True)

    # Monthly Breakdowns
    with tab2:
        st.subheader("Monthly Expenses Breakdown")
        selected_month = st.selectbox("Select a month", sorted(df["Month"].unique()))
        monthly_data = df[df["Month"] == selected_month]
        monthly_category_summary = monthly_data.groupby("Category")["Amount"].sum().reset_index()
        total_amount = monthly_category_summary["Amount"].sum()

        fig_month = px.pie(monthly_category_summary, names='Category', values='Amount',
                           title=f"{selected_month} Expense Breakdown\nTotal: ₱{total_amount:,.0f}")
        fig_month.update_traces(textinfo='percent+label', hovertemplate='%{label}: ₱%{value:,.0f} (%{percent})')
        st.plotly_chart(fig_month, use_container_width=True)

        # Month-over-month change arrow
        months_sorted = sorted(df["Month"].unique())
        selected_index = months_sorted.index(selected_month)
        if selected_index > 0:
            prev_month = months_sorted[selected_index - 1]
            change = monthly_summary.loc[monthly_summary['Month']==selected_month, 'Amount'].values[0] - \
                     monthly_summary.loc[monthly_summary['Month']==prev_month, 'Amount'].values[0]
            if change > 0:
                delta_arrow = '&#9650;'
                delta_color = 'red'
            elif change < 0:
                delta_arrow = '&#9660;'
                delta_color = 'green'
            else:
                delta_arrow = '–'
                delta_color = 'gray'
            delta_amount = f"₱{abs(change):,.0f}"
        else:
            delta_arrow, delta_color, delta_amount = "", "gray", ""
            prev_month = "N/A"

        st.markdown(
            f"<h2>Spending Change from {prev_month}: "
            f"<span style='color:{delta_color}; font-size:36px;'>{delta_arrow}</span> "
            f"<span style='font-size:28px;'>{delta_amount}</span></h2>",
            unsafe_allow_html=True
        )

    #Category Breakdown
    with tab3:
        st.subheader("Per-Category Breakdown")
        categories = df["Category"].unique().tolist()
        selected_category = st.selectbox("Select a Category", categories)
        category_data = df[df["Category"] == selected_category]
        category_summary = category_data.groupby("Description")["Amount"].sum().reset_index()

        fig_cat = px.pie(category_summary, names='Description', values='Amount',
                         title=f"{selected_category} Breakdown\nTotal: ₱{category_summary['Amount'].sum():,.0f}")
        fig_cat.update_traces(textinfo='percent+label', hovertemplate='%{label}: ₱%{value:,.0f} (%{percent})')
        st.plotly_chart(fig_cat, use_container_width=True)

    #Predictions
    with tab4:
        st.subheader("Spending Trend Prediction")
        monthly_df = monthly_summary.copy()
        monthly_df["MonthIndex"] = range(len(monthly_df))
        X = monthly_df[["MonthIndex"]]
        y = monthly_df["Amount"]
        model = LinearRegression()
        model.fit(X, y)
        next_month_index = [[len(monthly_df)]]
        predicted_amount = model.predict(next_month_index)[0]

        fig_pred = px.line(monthly_df, x='Month', y='Amount', markers=True, title="Spending Trend & Prediction")
        monthly_df['Predicted'] = model.predict(X)
        fig_pred.add_scatter(x=monthly_df['Month'], y=monthly_df['Predicted'], mode='lines', name='Trend', line=dict(dash='dash'))
        fig_pred.update_traces(hovertemplate='Month: %{x}<br>Amount: ₱%{y:,.0f}')
        st.metric("Predicted Spending", f"₱{predicted_amount:,.0f}")
        st.plotly_chart(fig_pred, use_container_width=True)

    #Insights
    with tab5:
        st.subheader("Insights")
        category_totals = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
        top_category = category_totals.index[0]
        top_category_amount = category_totals.iloc[0]
        st.markdown(f"**Top Spending Category:** {top_category} (₱{top_category_amount:,.0f})")

        # Top 3 transactions
        top_transactions = df.nlargest(3, "Amount")[["Date","Description","Amount"]]
        st.markdown("**Top 3 Biggest Transactions:**")
        st.table(top_transactions)

        # Personalized advice
        total_spent = df["Amount"].sum()
        advice_list = []

        high_spending = category_totals[category_totals / total_spent > 0.3]
        for cat, amt in high_spending.items():
            advice_list.append(f"Your spending on **{cat}** is high (₱{amt:,.0f}), consider reducing it next month.")

        large_txns = df[df["Amount"] > total_spent * 0.1]
        for _, row in large_txns.iterrows():
            advice_list.append(f"Noticeable large transaction: **{row['Description']}** of ₱{row['Amount']:,.0f} on {row['Date'].date()}.")

        low_spending = category_totals[category_totals / total_spent < 0.05]
        for cat, amt in low_spending.items():
            advice_list.append(f"You spent very little on **{cat}** (₱{amt:,.0f}), review if you are missing any essential payments.")

        if advice_list:
            for advice in advice_list:
                st.markdown(f"- {advice}")
        else:
            st.markdown("Your spending looks balanced this month. Great job! ✅")
