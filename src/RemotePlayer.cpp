#include "RemotePlayer.hpp"

#include <RemoteCommands.hpp>
#include <udpconnection.hpp>

#include <iostream>

namespace pyrgbdcalib{


    RemotePlayer::RemotePlayer(const std::string& client_ip, const unsigned int client_port)
    : m_con(new udpconnection)
    {
      bool ret = m_con->open_sending_socket(client_ip.c_str(), client_port);
      if(!ret){
        std::cerr << "ERROR in RemotePlayer::RemotePlayer: could not open_sending_socket for " << client_ip << " on port " << client_port << std::endl;
      }
    }

    RemotePlayer::~RemotePlayer(){
      // close m_con
      delete m_con;
    }


    void
    RemotePlayer::start(){
      int command = RemoteCommands::PLAY;
      m_con->send(&command, sizeof(command));
    }


    void
    RemotePlayer::stop(){
      int command = RemoteCommands::STOP;
      m_con->send(&command, sizeof(command));
    }

    void
    RemotePlayer::pause(){
      int command = RemoteCommands::PAUSE;
      m_con->send(&command, sizeof(command));
    }

    void
    RemotePlayer::unpause(){
      int command = RemoteCommands::UNPAUSE;
      m_con->send(&command, sizeof(command));
    }

    void
    RemotePlayer::loop(){
      int command = RemoteCommands::LOOP;
      m_con->send(&command, sizeof(command));
    }    
}
