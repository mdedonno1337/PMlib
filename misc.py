#!/usr/bin/env python

from numpy import median


################################################################################
# 
################################################################################

def medianXY( data ):
    x, y = zip( *data )
    return median( x ), median( y )
