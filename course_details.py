def get_details_from_csv(id, type):
    with open('data.csv', 'r') as f:
        data = []
        score_record = []
        for line in f:
            if str(id) in line:
                data.append(line.rstrip('\n'))

        if type == 'student':
            score = 0
            for line in data:
                score += int(line.split(',')[2])
                score_record.append(int(line.split(',')[2]))
            return [score, data, score_record]

        elif type == 'course':
            max_score = 0
            average_score = 0
            total_score = 0
            count = 0  # Corrected initialization to 0

            for line in data:
                values = line.split(',')
                score = int(values[2])  # Use split and access by index
                score_record.append(score)
                total_score += score
                count += 1
                if score > max_score:
                    max_score = score
            average_score = total_score / count  # Corrected division by count

            return [max_score, average_score, data, score_record]

if __name__ == '__main__':
    # Example usage:
    student_id = 102  # Replace with actual ID
    student_data = get_details_from_csv(student_id, 'student')
    course_id = 205  # Replace with actual ID
    course_data = get_details_from_csv(course_id, 'course')

    print(f"Student ID: {student_id}, Total Score: {student_data[0]}, Details: {student_data[2]}")
    # Access student details from student_data[1] if needed
    print(f"Course ID: {course_id}, Max Score: {course_data[0]}, Average Score: {course_data[1]}, Details: {course_data[3]}")
    # Access course details from course_data[2] if needed
