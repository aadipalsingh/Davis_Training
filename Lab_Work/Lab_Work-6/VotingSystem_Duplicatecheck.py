'''Voting System with Duplicate Check

Input:

List of votes
Tasks:
Count votes
Prevent duplicate voting using set
Declare winner
'''
# Sample list of votes (can be replaced with user input or file input)
votes=['Aditya','Sonia','Rohan','Rahul','Nikita','Yuvraj','Shivam','Aditya','Sonia' ,'Rohan']
# Create a set to track unique voters
unique_voters = set()
# Create a dictionary to count votes for each candidate
vote_count = {}
# Process each vote
for vote in votes:
    # Check if the voter has already voted
    if vote in unique_voters:
        print(f"Duplicate vote detected from {vote}. This vote will be ignored.")
        continue
    # Add the voter to the set of unique voters
    unique_voters.add(vote)
    # Count the vote for the candidate
    vote_count[vote] = vote_count.get(vote, 0) + 1
# Determine the winner (candidate with the most votes)
winner = max(vote_count, key=vote_count.get)
# Print the vote counts and the winner
print("Vote Counts:")
for candidate, count in vote_count.items():
    print(f"{candidate}: {count} votes")
print(f"The winner is: {winner} with {vote_count[winner]} votes.")  
