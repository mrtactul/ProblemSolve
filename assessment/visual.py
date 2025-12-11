"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import matplotlib.pyplot as plt


def plot_reviews_pie_chart(counts):
    """
    Create a pie chart showing the number of reviews per park.
    
    What: Visualizes the proportion of reviews for each park
    Why: Task 10 requirement
    
    Args:
        counts (dict): Dictionary with park names as keys and counts as values
    """
    if not counts:
        print("No data to visualize.")
        return
        
    labels = list(counts.keys())
    values = list(counts.values())
    
    plt.figure(figsize=(10, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('Distribution of Reviews per Park')
    plt.show()


def plot_top_locations_bar_chart(locations, ratings, park_name):
    """
    Create a bar chart of the top locations by average rating.
    
    What: Visualizes which locations give the highest ratings
    Why: Task 11 requirement
    
    Args:
        locations (list): List of location names
        ratings (list): List of average ratings
        park_name (str): Name of the park being analyzed
    """
    if not locations:
        print("No data to visualize.")
        return
        
    plt.figure(figsize=(12, 6))
    plt.bar(locations, ratings, color='skyblue')
    plt.xlabel('Reviewer Location')
    plt.ylabel('Average Rating')
    plt.title(f'Top {len(locations)} Locations by Average Rating for {park_name}')
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 5.5)  # Rating is out of 5
    plt.tight_layout()
    plt.show()


def plot_monthly_ratings_bar_chart(months, ratings, park_name):
    """
    Create a bar chart of average ratings by month.
    
    What: Visualizes seasonal trends in ratings
    Why: Task 12 requirement
    
    Args:
        months (list): List of month names
        ratings (list): List of average ratings
        park_name (str): Name of the park being analyzed
    """
    plt.figure(figsize=(12, 6))
    plt.bar(months, ratings, color='lightgreen')
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.title(f'Average Monthly Rating for {park_name}')
    plt.ylim(0, 5.5)  # Rating is out of 5
    plt.tight_layout()
    plt.show()

