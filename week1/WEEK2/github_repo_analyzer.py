
import requests   # library used to make HTTP requests to APIs


# ask the user to enter a GitHub username
username = input("Enter GitHub username: ")


# construct API endpoint to fetch repositories of that user
# this endpoint returns a list of repositories in JSON format
url = f"https://api.github.com/users/{username}/repos"


# send GET request to GitHub server
response = requests.get(url)


# convert JSON response into Python data structure
# this will become a LIST of dictionaries
repos = response.json()


# print total number of repositories
print("\nTotal repositories:", len(repos))


# variable to track repository with highest stars
max_stars = 0

# variable to store repo name with highest stars
top_repo = ""


# loop through each repository in the list
for repo in repos:

    # get number of stars of this repository
    stars = repo["stargazers_count"]

    # check if this repo has more stars than previous maximum
    if stars > max_stars:

        # update highest star count
        max_stars = stars

        # update repository name
        top_repo = repo["name"]


# print repository with most stars
print("Most starred repository:", top_repo)
print("Stars:", max_stars)


# create a set to store unique languages used
languages = set()


# loop through repositories again
for repo in repos:

    # get programming language used in the repository
    language = repo["language"]

    # ensure language is not None
    if language:

        # add language to set (set automatically removes duplicates)
        languages.add(language)


# print languages used
print("\nLanguages used:")
for lang in languages:
    print("-", lang)