#!/bin/sh

rpmbuild -ba *.spec \
  --define "_sourcedir $(pwd)" \
  --define "_specdir $(pwd)" \
  --define "_builddir $(pwd)" \
  --define "_srcrpmdir $(pwd)" \
  --define "_rpmdir $(pwd)"
