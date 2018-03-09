Open 3 terminals

1.) start stream which is later "live"
ssh hades
cd /opt/kinect-resources/rgbd-framework/rgbd-daemon/kinect_recordings &&  /opt/kinect-resources/rgbd-framework/rgbd-calib/install/bin/play -f 20 -k 4 -c -s 141.54.147.40 -p 7000 user_andre.stream


2.) start remote_recorder which is controlled from Avango
ssh hades
cd /home/steppo/Desktop/my-git/rgbd-calib/install/bin && ./remote_recorder -k 4 -c -a 8000 /tmp/8000.stream 141.54.147.40:7000

2.) start remote_player which is controlled from Avango
ssh hades
cd /home/steppo/Desktop/my-git/rgbd-calib/install/bin && ./remote_player -k 4 -c -a 8001 /tmp/8000.stream 141.54.147.40:7001


4.) start Avango example on hades
./start.sh

