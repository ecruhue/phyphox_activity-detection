# phyphox_activity-detection


In summary, given all the issues we found with current poor posture intervention tools and through a pilot study, we designed an interface that could automatically zoom in and out according to the page sizes on the screen based on two scenarios. 
Our evaluation demonstrated the effectiveness of our detection and provided insights into other possible scenarios as well.

In our experiments, we utilize angular velocities measured by the gyroscope in phyphox, due to the following aspects:

1) The gyroscope is more sensitive and more accurate than the accelerometer, especially when wrist rotation and lean-in posture are related to rotation rate;

2) Accelerations suffer from jitters and local minima, whereas angular velocities are smooth.

- Scenario 1: The user’ s hands are occupied with other tasks and he/she intends to zoom the screen using gestures.
(i.e., cooking from a written recipe)

Solution: The user applies wrist rotation gesture to zoom
in the screen.

- Scenario 2: The user is sitting in front of his/her laptop
without noticing his/her bad posture (too close to the
screen).

Solution: The system detect the lean-in posture and zoom in the screen to force the user back to origin.

Also, we might have several small activities in front of the laptop like, 

- Typing on the keyboard or not moving
- Moving items (i.e., grab a coffee cup and drink, switch the placement of your notebook to somewhere else.)


![](rotation.GIF)
![](typing or moving items.GIF)

![demo](lean-in.GIF)
