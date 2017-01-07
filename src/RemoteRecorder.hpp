#include <string>

namespace pyrgbdcalib{

  class RemoteRecorder{

  public:

    RemoteRecorder(const std::string& socket, const std::string& filename);

    std::string get_filename() const;

    void set_filename(std::string const & in_filename);

    bool record(const unsigned num_seconds);

    bool stop();

    bool is_paused();

  private:

    std::string m_socket;
    std::string m_filename;

    void re_init();

  };


}
