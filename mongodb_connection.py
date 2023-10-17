# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017")
# # print(client.admin.command('ping'))   #check connection

# db = client.DemoDB  # getting a database
# # db = client['DemoDB']

# collection = db.Students  # getting a collection
# # collection = db["Students"]
# print(collection)


# import datetime
# print("Insert starting & ending dates to extract news from the database")
# print("="*50)

# starting_date = input("Enter Starting date (YYYY-MM-DD): ")
# start_year, start_month, start_day = map(int, starting_date.split("-"))

# ending_date = input("Enter Ending date (YYYY-MM-DD): ")
# end_year, end_month, end_day = map(int, ending_date.split("-"))

# print("="*50)

# # Validating the dates
# if start_year > end_year or (start_year == end_year and start_month > end_month) or (
#         start_year == end_year and start_month == end_month and start_day > end_day):
#     print("Invalid date range. The starting date should be earlier than the ending date.")
#     print("="*60)
# else:
#     start_date = datetime.datetime(start_year, start_month, start_day, 0, 0, 0)
#     end_date = datetime.datetime(end_year, end_month, end_day, 23, 59, 59, 999999)
# query = {
#         "language": "en",
#         "publishedOn": {
#             "$gte": start_date,
#             "$lte": end_date
#         }
#     }
# documents = collection.find(query).sort("_id", -1)


import pymongo

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["enhedu-news"]
collection = db["newsFeedBackup28Aug"]
import os
# if not os.path.exists("MongoDB"):
#     os.makedirs("MongoDB")
with open("sample_document.txt", "w") as file:
    for i in collection.find()[:2]:
        keys = i.keys()
        print(keys)
        # if "title" in keys:
        #     print("Title:", i.get("title"))
        #     file.write("Title: " + i.get("title")+"\n")
        # if "summary" in keys:
        #     print("Summary:", i["summary"])
        #     file.write("Summary: " + i.get("summary")+"\n")
        # if "url" in keys:
        #     print("Url:", i["url"])
        #     file.write("Url: " + str(i.get("url"))+"\n")
        #     # file.write(f"Url: {i.get('url')}\n")
        # if "publishedAt" in keys:
        #     print("Published At:", i["publishedAt"])
        #     file.write("publishedAt:"+ str(i.get("publishedAt"))+ "\n")
        if "media" in keys:
                print("Image:", ", ".join([x["url"] for x in i["media"]]))
                file.write("Url: " + ", ".join([x["url"] for x in i["media"]])+"\n")

        # if "source" in keys:
        #     print("Source:", i["source"]["name"])
        #     file.write("Source:"+ i["source"]["name"]+ "\n")
        # if "countries" in keys:
        #     print("Countries:", ", ".join(i["countries"]))
        #     file.write("countries:"+ ", ".join(i["countries"])+ "\n")
        # if "cities" in keys:
        #     print("Cities:", ", ".join(i["cities"]))
        #     file.write("cities:"+ ", ".join(i["cities"])+ "\n")
        # if "catagories" in keys:
        #     print("Catagories:", ", ".join(i["cities"]))
        #     file.write("catagories:"+ ", ".join(i["catagories"]))
        # print("#"*50)

# Access the desired database and collection
# db = client["DemoDB"]
# collection = db["Posts"]

# # Create a document to be inserted
# document = {
#     "author": "Mike",
#     "text": "My first blog post!",
#     "tags": ["mongodb", "python", "pymongo"],
#     "date": datetime.datetime.now(tz=datetime.timezone.utc),
# }

# # Insert the document
# result = collection.insert_one(document)

# # Print the inserted document's ID
# print(f"Inserted document ID: {result.inserted_id}")

# MONGO_URI=""
# MONGO_DATABASE=""
# MONGO_COLLECTION=""
