def reward_function(params):
    # Example of rewarding the agent to follow center line

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 0.1
    elif distance_from_center <= marker_2:
        reward = 1
    elif distance_from_center <= marker_3:
        reward = 0.5
    else:
        reward = 1e-3 # likely crashed/ close to off track
    abs_steering = abs(params['steering_angle']) # We don't care whether it is left or right steering

    # Penalize if car steer too much to prevent zigzag
    ABS_STEERING_THRESHOLD = 15.0
    


    # Set the speed threshold based your action space
    SPEED_THRESHOLD = 1.0

    if all_wheels_on_track and (0.5*track_width - distance_from_center)>=0.05:
	  reward *= 1.0


    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward *= 1e-3
    elif speed < SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward *= 0.5
    else:
        # High reward if the car stays on track and goes fast
        reward *= 1.0
    
    
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)
