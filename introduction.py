from __future__ import division
# Under DATA SCIENTISTS YOU MAY KNOW we import the following:
from collections import Counter
# Under SALARIES AND EXPIERENCE we import the following:
from collections import defaultdict


## FINDING KEY CONNECTORS pp. 3
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Add the users friends to the list `users`:

# First set the item friends to an empty list
for user in users:
    user["friends"] = []

for user in users:
    print user

print friendships

# The below code didn't provide the right details:
# Then populate the lists using the `friendships` data
# for i, j in friendships:
#     users[i]["friends"].append(users[j])
#     users[j]["friends"].append(users[i])

# CORRECTED CODE:
for friend in friendships:
    users[friend[0]]["friends"].append(friend[1])
    users[friend[1]]["friends"].append(friend[0])

# show the new structure of the users list, so that it's clear that it's been updated
for user in users:
    print user


def number_of_friends(user):
    """how many friends does a _user_ have"""
    return len(user["friends"])

total_conncetions = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_conncetions / num_users

print avg_connections

# sorting users with the most firends to the least

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
# sort the list
sorted_list = sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends, reverse=True)
print sorted_list

## DATA SCIENTISTS YOU MAY KNOW pp. 6


def friends_of_friend_ids_bad(user, users):
    # "foaf" is short for "friend of a friend"
    # return [foaf["id"]
    #         for friend in user["friends"]
    #         for foaf in friend["friends"]]
    # CORRECTED CODE:
    f = []
    foaf = []
    for friend in user["friends"]:
        f.append(friend)
        foaf.append(friend)
    for l in f:
        for l_friend in users[l]["friends"]:
            foaf.append(l_friend)
    return foaf


friend_of_friends = friends_of_friend_ids_bad(users[0], users)
print friend_of_friends

# Raising a TypeError: 'int' object has no attribute '__getitem__'
# print [friend["id"] for friend in users[1]["friends"]]
# print [friend["id"] for friend in users[0]["friends"]]
# print [friend["id"] for friend in users[2]["friends"]]

# CORRECTED CODE:
print [friend for friend in users[0]["friends"]]
print [friend for friend in users[1]["friends"]]
print [friend for friend in users[2]["friends"]]


def not_the_same(user, other_user):
    """Two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    """`other_user` is not a friend if he's not in `user["friends"]`;
     that is, if he's not_the_same as all the people in `user["friends"]`"""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf)
                   and not_friends(user, foaf))

# TODO: Commented out, while this errors out.
# print friends_of_friend_ids(users[3])

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "Java"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"),
    (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
    (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"),
    (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
    (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"),
    (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


# Keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


def most_common_interest_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])


## SALARIES AND EXPIERENCE pp. 8

salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6.0), (69000, 6.5),
    (76000, 7.5), (60000, 2.5), (83000, 10.0), (48000, 1.9), (63000, 4.2)
]

# keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# keys are tenure buckets, vlaues are average salary for that bucket
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}


## PAID ACCOUNTS p. 11

years_experience = [
    (0.7, 'paid'), (1.9, 'unpaid'), (2.5, 'paid'), (4.2, 'unpaid'), (6.0, 'unpaid'),
    (6.5, 'unpaid'), (7.5, 'unpaid'), (8.1, 'unpaid'), (8.7, 'paid'), (10.0, 'paid')
]

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


## TOPICS OF INTEREST pp 11

words_and_counts = Counter(word
                           for user, interest in interests
                           for word, in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print word, count
