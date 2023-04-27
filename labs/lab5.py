import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(',')
print(grades)

grades = list(map(int, grades))
    
min_value = grades
print(min(min_value))

max_value = grades
print(max(max_value))

average_grade = sum(grades) / len(grades)
average_grade = round(average_grade, 2)
print(average_grade)

av_mean = round(statistics.mean(grades), 2)
print("mean grade: {}".format(av_mean))

av_median = statistics.median(grades)
print("median grade: {}".format(av_median))




