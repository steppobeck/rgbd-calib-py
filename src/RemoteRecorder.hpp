#ifndef REMOTERECORDER_HPP
#define REMOTERECORDER_HPP



#include <string>

class udpconnection;

namespace pyrgbdcalib{

  class RemoteRecorder{

  public:

    RemoteRecorder(const std::string& client_ip, const unsigned int client_port);
    ~RemoteRecorder();
    void start();
    void stop();


  private:

    udpconnection* m_con;

  };

}

#endif //#ifndef REMOTERECORDER_HPP