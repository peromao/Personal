def reward_function(params):
    abs_steering = abs(params['steering_angle'])
    is_offtrack = params["is_offtrack"]
    speed = params["speed"]
    steps = params["steps"]
    progress = params["progress"]
    if is_offtrack:
        return float(1e-3)
    reward = progress/steps*10
    if speed < 1:
        speed = 1
    reward *= speed
    if abs_steering != 0:
        reward *= 0.95
    return float(reward)