"""
This module contains classes for exporting data in various formats.
It demonstrates Object-Oriented Programming (OOP) principles including:
- Inheritance: Subclasses inherit from the base DataExporter class
- Polymorphism: Different classes implement the same method (export) differently
- Encapsulation: Grouping related data and methods into classes
"""
import csv
import json


class DataExporter:
    """
    Base class for data export functionality.
    This class defines the interface that all exporters must follow.
    """
    def export(self, data, filename):
        """
        Export data to a file. This method should be overridden by subclasses.
        
        Args:
            data (dict): The data to export
            filename (str): The name of the file to save to
        """
        raise NotImplementedError("Subclasses must implement export method")
    
    def prepare_aggregate_data(self, reviews_data):
        """
        Prepare aggregate data for export (Task 14 requirement).
        Calculates:
        - Number of reviews per park
        - Number of positive reviews (rating >= 4)
        - Average review score
        - Number of countries that reviewed each park
        
        Args:
            reviews_data (list): List of all reviews
            
        Returns:
            dict: Aggregated statistics per park
        """
        stats = {}
        
        for review in reviews_data:
            branch = review.get('Branch', 'Unknown')
            location = review.get('Reviewer_Location', 'Unknown')
            
            try:
                rating = int(review.get('Rating', 0))
            except ValueError:
                rating = 0
            
            if branch not in stats:
                stats[branch] = {
                    'total_reviews': 0,
                    'positive_reviews': 0,
                    'total_rating': 0,
                    'countries': set()
                }
            
            # Update stats
            stats[branch]['total_reviews'] += 1
            if rating >= 4:
                stats[branch]['positive_reviews'] += 1
            stats[branch]['total_rating'] += rating
            stats[branch]['countries'].add(location)
            
        # Final processing (calculate averages, convert sets to counts)
        final_stats = {}
        for branch, data in stats.items():
            if data['total_reviews'] > 0:
                avg_rating = data['total_rating'] / data['total_reviews']
            else:
                avg_rating = 0
                
            final_stats[branch] = {
                'total_reviews': data['total_reviews'],
                'positive_reviews': data['positive_reviews'],
                'average_rating': round(avg_rating, 2),
                'country_count': len(data['countries'])
            }
            
        return final_stats


class TXTExporter(DataExporter):
    """
    Export data to a plain text file.
    """
    def export(self, data, filename):
        """
        Save aggregate data to a .txt file in a readable format.
        """
        if not filename.endswith('.txt'):
            filename += '.txt'
            
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("DISNEYLAND REVIEWS ANALYSIS REPORT\n")
                f.write("=" * 40 + "\n\n")
                
                for park, stats in data.items():
                    f.write(f"PARK: {park}\n")
                    f.write("-" * 30 + "\n")
                    f.write(f"Total Reviews: {stats['total_reviews']}\n")
                    f.write(f"Positive Reviews: {stats['positive_reviews']}\n")
                    f.write(f"Average Rating: {stats['average_rating']}\n")
                    f.write(f"Number of Countries: {stats['country_count']}\n")
                    f.write("\n")
            return True, f"Successfully exported to {filename}"
        except Exception as e:
            return False, f"Export failed: {str(e)}"


class CSVExporter(DataExporter):
    """
    Export data to a CSV file.
    """
    def export(self, data, filename):
        """
        Save aggregate data to a .csv file.
        """
        if not filename.endswith('.csv'):
            filename += '.csv'
            
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # Write header
                writer.writerow(['Park Name', 'Total Reviews', 'Positive Reviews', 
                               'Average Rating', 'Country Count'])
                
                # Write data rows
                for park, stats in data.items():
                    writer.writerow([
                        park,
                        stats['total_reviews'],
                        stats['positive_reviews'],
                        stats['average_rating'],
                        stats['country_count']
                    ])
            return True, f"Successfully exported to {filename}"
        except Exception as e:
            return False, f"Export failed: {str(e)}"


class JSONExporter(DataExporter):
    """
    Export data to a JSON file.
    """
    def export(self, data, filename):
        """
        Save aggregate data to a .json file.
        """
        if not filename.endswith('.json'):
            filename += '.json'
            
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            return True, f"Successfully exported to {filename}"
        except Exception as e:
            return False, f"Export failed: {str(e)}"

