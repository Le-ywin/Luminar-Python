with open("new.txt","r") as std:

    # result = {}

    # marks = std.readlines()

    # for line in marks:

    #     details = line.split()[::-1]

    #     names = [details.pop()]

    #     sum = 0

    #     for i in details:

    #         sum += int(i)

    #         avg = sum / len(details)

    #         for j in names:

    #             result[j] = avg

    # print(result)




    # result = {}

    # new = []

    # for line in std:

    #     details = line.split()

    #     for i in details:

    #         names = details[0]

    #         marks =  details[1::]

    #         result[names] = (sum(int(i) for i in marks) / len(marks))
        
    # print(result)




    result = []

    for line in std:

        details = line.split()

        name = details[0]

        scores = list(map(int, details[1:]))

        avg = sum(scores) / len(scores)

        result.append({"name": name, "average": avg})

print(result)
