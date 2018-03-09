import avango
import avango.script
import avango.gua
from examples_common.GuaVE import GuaVE
import sys
import pyrgbdcalib

class TimedRotate(avango.script.Script):
    TimeIn = avango.SFFloat()
    live_avatar_matrix = avango.gua.SFMatrix4()
    recorded_avatar_matrix = avango.gua.SFMatrix4()    
    record_object = pyrgbdcalib.RemoteRecorder("141.54.147.40",8000)
    play_object = pyrgbdcalib.RemotePlayer("141.54.147.40",8001)
    state = 0

    def evaluate(self):
        self.live_avatar_matrix.value = avango.gua.make_trans_mat(
            -0.5, -1.0, -2.0) * avango.gua.make_rot_mat(10 * self.TimeIn.value *
                                                       2.0, 0.0, 1.0, 0.0)
        self.recorded_avatar_matrix.value = avango.gua.make_trans_mat(
             0.5, -1.0, -2.0) * avango.gua.make_rot_mat(10 * self.TimeIn.value *
                                                       2.0, 0.0, 1.0, 0.0)
        if (self.TimeIn.value > 5) and self.state == 0:
                print("start recording") # live_kinect_socket
                self.record_object.start()
                self.state = 1

        if (self.TimeIn.value > 10) and self.state == 1:
                print("stop recording")
                self.record_object.stop()
                self.state = 2


        if (self.TimeIn.value > 15) and self.state == 2:
                print("start loop") # daemon_play_socket
                self.play_object.loop()
                self.state = 3

        if (self.TimeIn.value > 20) and self.state == 3:
                print("pause") # daemon_play_socket
                self.play_object.pause()
                self.state = 4

        if (self.TimeIn.value > 25) and self.state == 4:
                print("unpause")
                self.play_object.unpause()
                self.state = 5

        if (self.TimeIn.value > 30) and self.state == 5:
                print("stop")
                self.play_object.stop()
                self.state = 6

        if (self.TimeIn.value > 40) and self.state == 6:
                print("start play")
                self.play_object.start()
                self.state = 7

        if (self.TimeIn.value > 50) and self.state == 7:
                print("start recording") # live_kinect_socket
                self.play_object.stop()
                self.record_object.start()
                self.state = 8

        if (self.TimeIn.value > 52) and self.state == 8:
                print("stop recording")
                self.record_object.stop()
                self.state = 9

        if (self.TimeIn.value > 55) and self.state == 9:
                print("start play")
                self.play_object.start()
                self.state = 10

        if (self.TimeIn.value > 60) and self.state == 10:
                self.play_object.stop()
                print("END of test")
                self.state = 11
def start():
    # setup scenegraph
    graph = avango.gua.nodes.SceneGraph(Name="scenegraph")
    loader = avango.gua.nodes.TriMeshLoader()

    videoloader = avango.gua.nodes.Video3DLoader()

    live_avatar_node = videoloader.load("live_avatar", "/opt/kinect-resources/rgbd-framework/rgbd-daemon/kinect_recordings/surface_23_24_25_26_hades.ks")
    live_avatar_transform = avango.gua.nodes.TransformNode(Children=[live_avatar_node])

    recorded_avatar_node = videoloader.load("recorded_avatar", "/opt/kinect-resources/rgbd-framework/rgbd-daemon/kinect_recordings/surface_23_24_25_26_hades_playback.ks")
    recorded_avatar_transform = avango.gua.nodes.TransformNode(Children=[recorded_avatar_node])


    light = avango.gua.nodes.LightNode(
        Type=avango.gua.LightType.POINT,
        Name="light",
        Color=avango.gua.Color(1.0, 1.0, 1.0),
        Brightness=100.0,
        Transform=(avango.gua.make_trans_mat(1, 1, 5) *
                   avango.gua.make_scale_mat(30, 30, 30)))

    size = avango.gua.Vec2ui(1024, 768)

    window = avango.gua.nodes.GlfwWindow(Size=size, LeftResolution=size)

    avango.gua.register_window("window", window)

    cam = avango.gua.nodes.CameraNode(
        LeftScreenPath="/screen",
        SceneGraph="scenegraph",
        Resolution=size,
        OutputWindowName="window",
        Transform=avango.gua.make_trans_mat(0.0, 0.0, 3.5))

    res_pass = avango.gua.nodes.ResolvePassDescription()
    res_pass.EnableSSAO.value = True
    res_pass.SSAOIntensity.value = 4.0
    res_pass.SSAOFalloff.value = 10.0
    res_pass.SSAORadius.value = 7.0

    #res_pass.EnableScreenSpaceShadow.value = True

    res_pass.EnvironmentLightingColor.value = avango.gua.Color(0.1, 0.1, 0.1)
    res_pass.ToneMappingMode.value = avango.gua.ToneMappingMode.UNCHARTED
    res_pass.Exposure.value = 1.0
    res_pass.BackgroundColor.value = avango.gua.Color(0.45, 0.5, 0.6)

    anti_aliasing = avango.gua.nodes.SSAAPassDescription()

    pipeline_description = avango.gua.nodes.PipelineDescription(
        Passes=[
            avango.gua.nodes.TriMeshPassDescription(),
            avango.gua.nodes.LightVisibilityPassDescription(),
            avango.gua.nodes.Video3DPassDescription(),
            res_pass,
            anti_aliasing,
        ])

    cam.PipelineDescription.value = pipeline_description

    screen = avango.gua.nodes.ScreenNode(
        Name="screen",
        Width=2,
        Height=1.5,
        Children=[cam])

    graph.Root.value.Children.value = [live_avatar_transform, recorded_avatar_transform, light, screen]

    #setup viewer
    viewer = avango.gua.nodes.Viewer()
    viewer.SceneGraphs.value = [graph]
    viewer.Windows.value = [window]

    frame_updater = TimedRotate()

    timer = avango.nodes.TimeSensor()
    frame_updater.TimeIn.connect_from(timer.Time)

    live_avatar_transform.Transform.connect_from(frame_updater.live_avatar_matrix)
    recorded_avatar_transform.Transform.connect_from(frame_updater.recorded_avatar_matrix)

    guaVE = GuaVE()
    guaVE.start(locals(), globals())

    viewer.run()


if __name__ == '__main__':
    start()
