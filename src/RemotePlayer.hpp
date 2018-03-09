#ifndef REMOTEPLAYER_HPP
#define REMOTEPLAYER_HPP



#include <string>

class udpconnection;

namespace pyrgbdcalib{

  class RemotePlayer{

  public:

    RemotePlayer(const std::string& client_ip, const unsigned int client_port);
    ~RemotePlayer();
    void start();
    void stop();

    void pause();
    void unpause();
    void loop();

  private:

    udpconnection* m_con;

  };

}

#endif //#ifndef REMOTEPLAYER_HPP