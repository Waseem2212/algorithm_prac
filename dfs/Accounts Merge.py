from collections import defaultdict

def accountsMerge(accounts):
    email_graph = defaultdict(list)
    email_to_name = {}

    # Build graph and map emails to names
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            email_to_name[email] = name
            email_graph[account[1]].append(email)
            email_graph[email].append(account[1])

    visited = set()
    merged_accounts = []

    def dfs(email, emails):
        emails.append(email)
        visited.add(email)
        for neighbor in email_graph[email]:
            if neighbor not in visited:
                dfs(neighbor, emails)

    for email in email_graph:
        if email not in visited:
            emails = []
            dfs(email, emails)
            merged_accounts.append([email_to_name[email]] + sorted(emails))

    return merged_accounts

# Example Execution
accounts_example = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"]
]
print("Accounts Merge Result:", accountsMerge(accounts_example))
