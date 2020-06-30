=========
sofia-sip
=========

Build RPM for sofia-sip library

Sources
-------

See http://sofia-sip.sourceforge.net/


RPM build options
-----------------

The build has been tested on CentOS 7 with the devtoolset-9 SCLo bundle installed.

It is possible to set the ``dbgflags`` macro for additional CFLAGS and LDFLAGS.

For instance to compile with ``libasan`` add the following options to ``rpmbuild`` ::

   -D 'dbgflags -O0 -fno-omit-frame-pointer -g3 -ggdb3 -fsanitize=address'

