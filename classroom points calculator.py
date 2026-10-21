team_a = 45
team_b = 38
team_c = 52
team_d = 40
team_e = 47

total_points = team_a + team_b + team_c + team_d + team_e
average_points = total_points / 5
print("Total points:", total_points)
print("Average points per team:", average_points)

stars_per_point = 2
total_stars = total_points * stars_per_point
print("Total reward stars:", total_stars)

box_size = 25
full_boxes = total_stars // box_size
leftover_stars = total_stars % box_size
print("Full boxes:", full_boxes)
print("Leftover stars:", leftover_stars)

last_week = 200
print("More than last week?", total_points > last_week)
print("Same as last week?", total_points == last_week)
print("At least as many as last week?", total_points >= last_week)

total_points += 10   
print("Total after bonus:", total_points)
total_points -= 6    
print("Total after penalty:", total_points)