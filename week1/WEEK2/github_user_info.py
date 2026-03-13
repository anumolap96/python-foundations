
import requests   # library used to make API requests


# ask user to enter a GitHub username
username = input("Enter GitHub username: ")


# construct API URL dynamically
url = f"https://api.github.com/users/{username}"


# send GET request to GitHub server
response = requests.get(url)


# convert JSON response into Python dictionary
data = response.json()


# print important fields from the dictionary
print("\nGitHub User Information")
print("-----------------------")

print("Name:", data["name"])
print("Public Repositories:", data["public_repos"])
print("Followers:", data["followers"])
print("Following:", data["following"])
print("Profile URL:", data["html_url"])