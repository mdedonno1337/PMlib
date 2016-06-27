#!/usr/bin/env python

import numpy as np

################################################################################
# 
################################################################################

def medianXY( data ):
    x, y = zip( *data )
    return np.median( x ), np.median( y )

################################################################################
#    Matrix manipulation
################################################################################

def matrixApply( point, matrix ):
    inputx, inputy = point
    return np.dot( np.matrix( "%f %f 1" % ( inputx, inputy ) ), np.matrix( matrix ) ).ravel().tolist()[0][0:2]

def matrixListApply( list, matrix ):
    ret = []

    for p in list:
        ret.append( matrixApply( p, matrix ) )

    return ret

def matrixMatrixApply( a, b ):
    ret = []
    for p in a.tolist():
        ret.append( matrixApply( p, b ) )
    
    return np.matrix( ret )

def multiDot( *argv ):
    ret = argv[0]
    
    for m in argv[1:]:
        ret = np.dot( 
            ret,
            m
        )
    
    return ret

def rotMatrix( theta, degree = True ):
    if degree:
        theta = theta / 180.0 * np.pi
    
    c = np.cos( theta )
    s = np.sin( theta )
    
    return np.array( [[ c, -s, 0 ], [ s, c, 0 ], [ 0, 0, 1 ] ] ).T

