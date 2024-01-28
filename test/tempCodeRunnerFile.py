    contents = csv.DictReader(file)
    for content in contents :
        print(content["name"])