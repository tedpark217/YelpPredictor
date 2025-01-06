import json
import random

# Get Philadelphia Businesses
'''newFile = open("business_dataset.json", "w")
for l in open("yelp_academic_dataset_business.json"):
    if "city\":\"Philadelphia" in l:
        newFile.write(l)
newFile.close()'''

# Get Reviews of Philli Businesses
'''business = []
with open('business_dataset.json') as file:
    for line in file:
        business.append(json.loads(line))

idB = [d['business_id'] for d in business]

newFile = open("review_dataset.json", "w")
with open('yelp_academic_dataset_review.json') as file:
    for line in file:
        js = json.loads(line)
        if js['business_id'] in idB:
            newFile.write(line)
newFile.close()'''

# Get 100,000 random review sample
'''n = 100000
reviews = []
with open('review_dataset.json') as file:
    for line in file:
        reviews.append(line)

newReviews = random.sample(reviews, n)

newFile = open("100k_review_dataset.json", "w")
for l in newReviews:
    newFile.write(l)
newFile.close()'''

# Get users who reviewed
reviews = []
with open('100k_review_dataset.json') as file:
    for line in file:
        reviews.append(json.loads(line))

reviewU = [d['user_id'] for d in reviews]

newFile = open("user_dataset.json", "w")
with open('yelp_academic_dataset_user.json') as file:
    for line in file:
        js = json.loads(line)
        if js['user_id'] in reviewU:
            newFile.write(line)
newFile.close()





 

