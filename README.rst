=========
sofia-sip
=========

Build RPM for sofia-sip library

Sources
=======

See http://sofia-sip.sourceforge.net/


RPM build options
=================

The build has been tested on CentOS 7 with the devtoolset-9 SCLo bundle installed.

It is possible to set the ``dbgflags`` macro for additional CFLAGS and LDFLAGS.

For instance to compile with ``libasan`` add the following options to ``rpmbuild`` ::

   -D 'dbgflags -O0 -fno-omit-frame-pointer -g3 -ggdb3 -fsanitize=address'

Building a release RPM
======================

1. Fix the .spec file Version and Release tag
2. Write the %changelog entry in the .spec file
3. Commit the above changes
4. Create a git tag that starts with a digit. Do not use any "-" (minus) sign! E.g.: 1.12.11r20
5. Push the tag and the commit to start the automated build on Travis CI

Builds started from a tagged commit are published to "updates"!

More information: https://docs.nethserver.org/projects/nethserver-devel/en/v7/building_rpms.html
