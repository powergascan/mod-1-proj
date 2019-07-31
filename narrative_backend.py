import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



def profitability_distibution_by_year():
    plt.figure(figsize=(12,10))
    plot2 = sns.boxplot(x="year", y="profit_margin", data=bydate_temp)
    plot2.set(xlabel='Release Year', ylabel='Profit Percentage')
    plot2.set_title('Distribution of Profit Percentage by Year')
    return

def plot_competition_profitability():
    plt.clf()
    plt.figure(figsize=(18, 12))
    sns.boxplot('competition_size','profit_margin', data=movie_budget, hue="budget_size", showfliers=False)
    plt.xlabel("Competition Level", size=20)
    plt.ylabel("Profitability", size=20)
    plt.legend(fontsize="xx-large")
    plt.title("Competition and Profitability for Independent vs Mass Production Movies", size=30)
    return
    
def plot_market_profitability():
    plt.clf()
    plt.figure(figsize=(18, 12))
    sns.boxplot('market_condition','domestic_margin', data=movie_budget, hue="budget_size", showfliers=False)
    plt.xlabel("Market Condition", size=20)
    plt.ylabel("Profitability", size=20)
    plt.legend(fontsize="xx-large")
    plt.title("Market Condition and Profitability for Independent vs Mass Production Movies", size=30)
    return

def plot_seasonality_profitability():
    movie_budget['month']=movie_budget.view_date.dt.strftime("%B")
    movie_budget['month_num']=movie_budget.view_date.dt.month
    movie_budget_agg=movie_budget.groupby("month").\
        agg({"title":"count","profit_margin":"mean","month_num":"min"}).reset_index()
    movie_budget_agg=movie_budget_agg.sort_values("month_num")
    
    plt.clf()
    plt.figure(figsize=(18,12))
    bottom = 8
    max_height = 4
    N=12
    theta = [n / float(N) * 2 * pi for n in range(N)]
    width = (2*pi) / N

    radii=movie_budget_agg["title"].to_list()
    radiii=movie_budget_agg["profit_margin"].to_list()
    ax = plt.subplot(111, polar=True)

    bars = ax.bar(theta, radii, width=width, bottom=bottom, label='# of Movie Release')
    ax.plot(theta, radiii, linewidth=2, linestyle='solid',color="orange", label='Average Movie Profitability')
    ax.plot([theta[-1],theta[0]], [radiii[-1],radiii[0]], linewidth=2, linestyle='solid', color="orange")
    plt.xticks(theta, movie_budget_agg["month"], color='grey', size=20)
    plt.fill(theta, radiii, 'b', alpha=0.1)

    # Use custom colors and opacity
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.7)

    ax.legend(fontsize="xx-large")
    plt.title("Number of Movie Release vs. Profitability", size=30)
    plt.savefig("..//release_profitability_month.png")
    return



