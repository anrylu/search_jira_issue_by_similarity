from jira import JIRA
import pandas as pd

def fetch(url, token, query):
    ret = []
    jira = JIRA(url, token_auth=token)
    issues = jira.search_issues(
        query, startAt=0, maxResults=1000, fields='key,summary,status,description')
    for issue in issues:
        ret.append({
            'key': issue.key,
            'status': issue.fields.status,
            'summary': issue.fields.summary,
            'description': issue.fields.description
        })
    return ret


if __name__ == '__main__':
    url = input("url: ")
    token = input("token: ")
    query = input("query: ")
    result = fetch(url, token, query)
    df = pd.DataFrame.from_dict(result)
    df.to_csv('jira.csv', index=False, header=True)
