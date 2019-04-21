// constant speed in lane
double dist_inc = 0.5;
for (int i = 0; i < 50; ++i) {
  double car_next_s = car_s +  dist_inc*i;
  double car_next_d = car_d;
  vector<double> xy = getXY(car_next_s,car_next_d,map_waypoints_s,map_waypoints_x,map_waypoints_y);
  next_x_vals.push_back(xy[0]);
  next_y_vals.push_back(xy[1]);
}

// smooth out using spline
