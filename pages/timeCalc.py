def calculate_maneuverTime(vehicle):
  x=vehicle.get_location().x;
  y=vehicle.get_location().y;
  orientAngl=vehicle.get_transform().rotation.yaw;
  ts=0;
  cond = True;
  while cond:
    for ts in numpy.arange(0,config.T,config.sampling_period):
        s_angle = steeringAngle(ts);
        velo = velocity(ts);
        if(s_angle == 0):
          orientAngl_lastStep = orientAngl;
          orientAngl = orientAngl;
          x = x + (velo * config.sampling_period * math.cos(orientAngl));
          y = y + (velo * config.sampling_period * math.sin(orientAngl));
        else:
          orientAngl_lastStep = orientAngl;
          orientAngl = orientAngl + (((velo * config.sampling_period)/
             config.vehicle_length)*math.sin(s_angle));
          x =  x + ((config.vehicle_length / math.tan(s_angle)) * (math.sin(orientAngl)
            - math.sin(orientAngl_lastStep)));
          y =  y - ((config.vehicle_length / math.tan(s_angle)) * (math.cos(orientAngl) 
           - math.cos(orientAngl_lastStep)));
        cond=longitudinal_condition(vehicle.get_location().x,x,vehicle.get_location().
           y,y,vehicle.get_transform().rotation.yaw);
        print('longitudinal cond:', cond);
        config.T += config.sampling_period;
        print('T calc values',config.T);
    config.T -= config.sampling_period;