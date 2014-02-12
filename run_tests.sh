#!/bin/bash
INOUT_DIR=$WORKSPACE/Inoutput

pip install --quiet nosexcover
pip install --quiet pylint

nosetests --with-xcoverage --with-xunit --cover-package=means --cover-erase $CODE_DIR
cd $INOUT_DIR
python -m means.tests.regression_tests --xunit | tee $WORKSPACE/regression_tests.xml