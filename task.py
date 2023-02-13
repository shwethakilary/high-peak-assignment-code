def job_scheduling(n, jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    result = [0, 0]
    end_time = 0
    for i in range(n):
        if jobs[i][0] >= end_time:
            end_time = jobs[i][1]
            result[0] += 1
            result[1] += jobs[i][2]
    return result

if __name__ == "__main__":
    n = int(input("Enter the number of Jobs: ").strip())
    jobs = []
    for i in range(n):
        start_time = int(input("Enter job start time: ").strip())
        end_time = int(input("Enter job end time: ").strip())
        profit = int(input("Enter job earnings: ").strip())
        jobs.append([start_time, end_time, profit])
    result = job_scheduling(n, jobs)
    print("Number of tasks and earnings available for others task: ", n - result[0])
    print("Earnings: ", result[1])
