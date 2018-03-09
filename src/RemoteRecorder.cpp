#include "RemoteRecorder.hpp"

#include <RemoteCommands.hpp>
#include <udpconnection.hpp>

#include <iostream>

namespace pyrgbdcalib{


    RemoteRecorder::RemoteRecorder(const std::string& client_ip, const unsigned int client_port)
    : m_con(new udpconnection)
    {
      bool ret = m_con->open_sending_socket(client_ip.c_str(), client_port);
      if(!ret){
        std::cerr << "ERROR in RemoteRecorder::RemoteRecorder: could not open_sending_socket for " << client_ip << " on port " << client_port << std::endl;
      }
    }

    RemoteRecorder::~RemoteRecorder(){
      // close m_con
      delete m_con;
    }


    void
    RemoteRecorder::start(){
      int command = RemoteCommands::RECORD;
      m_con->send(&command, sizeof(command));
    }


    void
    RemoteRecorder::stop(){
      int command = RemoteCommands::STOP;
      m_con->send(&command, sizeof(command));
    }

}
