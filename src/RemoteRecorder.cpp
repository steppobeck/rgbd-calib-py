#include "RemoteRecorder.hpp"

#include <iostream>

namespace pyrgbdcalib{


  RemoteRecorder::RemoteRecorder(const std::string& socket, const std::string& filename)
    : m_socket(socket),
      m_filename(filename)
  {
    re_init();
  }

  void
  RemoteRecorder::re_init(){
    std::cout << "INFO: RemoteRecorder::re_init()" << std::endl;
    // 1. open zmq socket to recorddaemon from rgbd-calib
    // pass filename
  }

  std::string
  RemoteRecorder::get_filename() const {
    return m_filename;
  }

  void
  RemoteRecorder::set_filename(std::string const & in_filename) {
    if(is_paused()){
      // 1. use zmq socket to tell recorddaemon new filename
      m_filename = in_filename;
    }
  }

  bool
  RemoteRecorder::record(const unsigned num_seconds){
    std::cout << "INFO: RemoteRecorder::record: starting recording for num seconds: " << num_seconds << std::endl;

    // 1. use zmq socket to tell recorddaemon to record for num_seconds....

    return true;
  }


  bool
  RemoteRecorder::stop(){
    // 1. use zmq socket to tell recorddaemon to stop and save....
    return true;
  }


  bool
  RemoteRecorder::is_paused(){
    // 1. use zmq socket to ask recorddaemon if saving of filename is finished....
    return true;
  }


}
