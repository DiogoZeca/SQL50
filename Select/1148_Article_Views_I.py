# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | article_id    | int     |
# | author_id     | int     |
# | viewer_id     | int     |
# | view_date     | date    |
# +---------------+---------+
# There is no primary key (column with unique values) for this table, the table may have duplicate rows.
# Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
# Note that equal author_id and viewer_id indicate the same person.

 

# Write a solution to find all the authors that viewed at least one of their own articles.

# Return the result table sorted by id in ascending order.



import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors_viewed_own_articles = views[views['author_id'] == views['viewer_id']]
    unique_authors = authors_viewed_own_articles['author_id'].unique()
    unique_authors = sorted(unique_authors)
    
    result_df = pd.DataFrame({'id': unique_authors})
    return result_df