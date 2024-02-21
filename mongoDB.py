from pymongo import MongoClient
import os
import logging
from constants import MONGODB_DIRECTORY



def fetchFromMongoDB(
        MONGO_URI: str,
        MONGO_DATABASE: str,
        MONGO_COLLECTION: str
) -> str:

    client = MongoClient(MONGO_URI)
    try:
        client.admin.command('ping')
        logging.info(
            "Successfully connected to MongoDB....")
    except Exception as e:
        logging.info(e)
    db = client[MONGO_DATABASE]
    collections = db[MONGO_COLLECTION]

    if not os.path.exists(MONGODB_DIRECTORY):
        os.makedirs(MONGODB_DIRECTORY)

    with open(f"{MONGODB_DIRECTORY}/{MONGO_COLLECTION}.txt", "w") as file:
        for i in collections.find()[:20]:
            keys = i.keys()
            # print(keys)

            # print("Title:", i.get("title"))
            file.write("Title: " + i.get("title")+"\n")

            # print("Summary:", i["summary"])
            file.write("Summary: " + i.get("summary")+"\n")

            # print("Url:", i["url"])
            file.write("Url: " + str(i.get("url"))+"\n")

            # print("Published At:", i["publishedAt"])
            file.write("publishedAt: " + str(i.get("publishedAt")) + "\n")

            # print("Image:", i["media"][0]["url"])
            file.write("Image: " + i["media"][0]["url"] + "\n")

            # print("Source:", i["source"]["name"])
            file.write("Source: " + i["source"]["name"] + "\n")

            # print("Source Nationality:", i["source"]["name"])
            file.write("Source Nationality: " +
                       i["source"]["sourceNationality"] + "\n")

            # print("Countries:", ", ".join(i["countries"]))
            if len(i["countries"]):
                file.write("countries: " + ", ".join(i["countries"]) + "\n")
            else:
                file.write("countries: N/A"+"\n")

            # print("Cities:", ", ".join(i["cities"]))
            if len(i["cities"]):
                file.write("cities: " + ", ".join(i["cities"]) + "\n")
            else:
                file.write("cities: N/A"+"\n")

            # print("Categories:", i["categories"]["parent"]["name"],i["categories"]["id"])
            file.write("categories: "+i["categories"]["parent"].get("name",'N/A') +
                       "\n\t\t\t"+"IPTCCode: "+i["categories"].get("id","N/A")+"\n")

            # print("Language: ", i["language"])
            file.write("Language: "+i['language'] + "\n")

            # print("Companies: ", 'N/A' if len(i['companies'])==0 else i['companies'])
            file.write(
                f"Companies: {'N/A' if len(i['companies'])==0 else i['companies']}")

            # print("#"*50)
            file.write("\n"*3)
    logging.info("Completed!!!!!!!!!!!!!")
    return MONGODB_DIRECTORY
