[kf-gaussian]: ./images/kf-gaussian.png "more certainty"
[kf-math]: ./images/kf-math.png "math behind"

1. Gaussian distribution
  - high variance means flat curve and means more uncertainty
  - we want more certainty

2. The new belief will be somewhere between the previous belief and the new measurement.
but the new peak will NOT be between the heights of the other two. In fact, it will be higher!
This is because more measurements always gives us more certainty.
![alt text][kf-gaussian]
![alt text][kf-math]
