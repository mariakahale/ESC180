def longest_sequence(search_str, ch):
    tracker = 1
    for i in range(0, len(search_str)-2):
        if search_str[i]==search_str[i-1] and search_str[i]==ch:
            print(tracker, search_str[i]==search_str[i-1], search_str[i]==ch)
            tracker +=1
        else:
            print("NO")
            largest_count = tracker
            tracker = 1
    return largest_count

print(longest_sequence("aababbbbbbabb", "b"))
            
