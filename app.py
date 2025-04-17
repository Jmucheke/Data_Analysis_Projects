import numpy
from matplotlib import pyplot

def data_to_dict(data):
    data_dict = {}
    for i in range(1, len(data)):
        row = data[i]
        name = row[0]
        steps = numpy.array(row[1:], dtype = int)
        data_dict[name] = steps
    return data_dict

def hourly_to_daily(hourly_steps):
    daily_steps = []
    for i in range(0, len(hourly_steps), 24):
        day_steps = hourly_steps[i:i+24]
        daily_step_count = sum(day_steps)
        daily_steps.append(daily_step_count)
    return daily_steps

def compute_stats(step_dict):
    stats_dict = {}
    for key, value in step_dict.items():
        stats_dict[key] = {"min": min(value), "max": max(value), "average": numpy.mean(value)}
    return stats_dict

def choose_categories(avg_list):
    categories = {"concerning":0, "average":0, "excellent":0}
    for avg_steps in avg_list:
        if avg_steps < 5000:
            categories["concerning"] = categories["concerning"] + 1
        elif 5000 < avg_steps < 10000:
            categories["average"] = categories['average'] + 1
        else:
            categories["excellent"] = categories["excellent"] + 1
    return categories

def daily_to_total(daily_steps):
    total_dict = {}
    for name, steps in daily_steps.items():
        total_dict[name] = sum(steps)
    return total_dict

def find_min_index(input_list): # helper function for mySort 
    current_min = input_list[0]
    index = 0
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]
            index = i
    return index

def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    for i in range(len(user_steps)):
        min_index = find_min_index(user_steps)
        sorted_user_names.append(user_names[min_index])
        sorted_user_steps.append(user_steps[min_index])
        user_steps[min_index] = float("inf")
    return sorted_user_names, sorted_user_steps

def plot_line(steps):
    hour_list = range(24)
    pyplot.title("Performance over the day")
    pyplot.xlabel("Hour of the day")
    pyplot.ylabel("Number of steps")
    pyplot.plot(hour_list, steps)
    pyplot.savefig("plot4.png")
    pyplot.close()

def plot_pie(categories):
    pyplot.pie(categories.values(), labels=categories.items())
    pyplot.title("Pie chart for categories")
    pyplot.savefig("plot3.png")
    pyplot.close()

def plot_bar(sorted_names, sorted_steps):
    pyplot.bar(sorted_names, sorted_steps)
    pyplot.xticks(rotation=45)
    pyplot.tight_layout()
    pyplot.savefig("plot2.png")
    pyplot.close()

def plot_bubbles(daily_step_dict):
    # Making a list to represent the number of days.
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Code to plot data for all the users in a bubble plot.
    for name in daily_step_dict:
        pyplot.scatter(days, [name]*7, numpy.array(daily_step_dict[name])/30)
    # Adding the requried title and labels
    pyplot.title("Bubble plot for all members")
    pyplot.xlabel("Day of the week")
    pyplot.ylabel("User name")
    pyplot.savefig("plot1.png")
    pyplot.close()

def main():
    
    data = numpy.loadtxt("steps.csv", delimiter = ",", dtype = str)
    data_dict = data_to_dict(data)

    daily_step_dict = {}
    for key in data_dict.keys():
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    stats_dict = compute_stats(daily_step_dict)

    avg_list = []
    for name in stats_dict:
        stats = stats_dict[name]
        avg_list.append(stats["average"])

    categories = choose_categories(avg_list)

    total_step_dict = daily_to_total(daily_step_dict)

    unsorted_names = list(total_step_dict.keys())
    unsorted_steps = list(total_step_dict.values())
    sorted_names, sorted_steps = my_sort(unsorted_names, unsorted_steps)

    steps = data_dict["Juliana"][0:24]
    plot_line(steps)

    plot_pie(categories)

    plot_bar(sorted_names, sorted_steps)

    # Function call to plot the bubble plot
    plot_bubbles(daily_step_dict)

main()