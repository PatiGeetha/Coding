def find_invalid_comments(df):
    result = df[df['content'].str.len() > 20][['comment_id']]
    return result
    