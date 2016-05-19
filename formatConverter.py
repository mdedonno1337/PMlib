#!/usr/bin/env python
#  *-* coding: cp850 *-*

from lib.points import matrixApply

import numpy as np


def cooPIL2NIST( data, height, res ):
    if type( data ) == list:
        return map( lambda x: cooPIL2NIST( x, height, res ), data )
    else:
        return matrixApply( 
            data,
            np.dot( 
                np.matrix( "1 0 0; 0 -1 0; 0 %.6f 1" % height ),
                np.matrix( "%.6f 0 0; 0 %.6f 0; 0 0 1" % ( 25.4 / res, 25.4 / res ) )
            )
        )
        